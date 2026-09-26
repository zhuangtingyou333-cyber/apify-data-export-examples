#!/usr/bin/env python3
"""Bounded Apify examples. Dry-run by default; Python standard library only."""
import argparse
import csv
import io
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
API = 'https://api.apify.com/v2'

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

class Api:
    def __init__(self, token):
        self.token = token
        self.opener = urllib.request.build_opener(NoRedirect)

    def request(self, path, method='GET', body=None):
        if not path.startswith('/') or path.startswith('//'):
            raise ValueError('Expected a fixed Apify API path')
        payload = None if body is None else json.dumps(body).encode()
        request = urllib.request.Request(API + path, data=payload, method=method,
            headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'})
        # A run-start POST is never automatically retried: it could create and bill a duplicate run.
        try:
            with self.opener.open(request, timeout=35) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(f'Apify HTTP {error.code}; check your token, credits and input. No automatic retry was made.') from None
        except urllib.error.URLError:
            raise RuntimeError('Network error. Check Console before restarting: a submitted run may already exist.') from None


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-zA-Z0-9]+', value):
        raise RuntimeError('Unexpected resource identifier from Apify')
    return value


def collect(api, example, sleep=time.sleep, monotonic=time.monotonic):
    actor = example['actor']
    if not re.fullmatch(r'peerless_columbine~[a-z0-9-]+', actor):
        raise ValueError('Example must target the documented publisher')
    query = urllib.parse.urlencode({'timeout': 180, 'maxTotalChargeUsd': 0.15})
    run = api.request('/acts/' + actor + '/runs?' + query, 'POST', example['input'])['data']
    run_id = identifier(run['id'])
    print('Run: https://console.apify.com/actors/runs/' + run_id, file=sys.stderr)
    deadline = monotonic() + 240
    while run['status'] in {'READY', 'RUNNING', 'TIMING-OUT', 'ABORTING'}:
        if monotonic() >= deadline:
            raise RuntimeError('Polling deadline reached. Check the run link before starting another run.')
        sleep(2)
        run = api.request('/actor-runs/' + run_id)['data']
    if run['status'] != 'SUCCEEDED':
        raise RuntimeError('Run ended with ' + run['status'] + '; inspect its log and OUTPUT in Console.')
    dataset = identifier(run['defaultDatasetId'])
    rows = []
    while True:
        batch = api.request('/datasets/' + dataset + '/items?clean=true&limit=1000&offset=' + str(len(rows)))
        if not isinstance(batch, list):
            raise RuntimeError('Unexpected dataset response')
        rows.extend(batch)
        if len(batch) < 1000:
            return rows


def csv_text(rows):
    out = io.StringIO()
    fields = list(dict.fromkeys(k for row in rows for k in row))
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        converted = {}
        for key, value in row.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=False)
            if isinstance(value, str) and value.lstrip().startswith(('=', '+', '-', '@')):
                value = "'" + value  # Avoid executing source text as a spreadsheet formula.
            converted[key] = value
        writer.writerow(converted)
    return out.getvalue()


def main():
    presets = sorted(p.stem for p in (ROOT / 'examples').glob('*.json'))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('example', choices=presets)
    parser.add_argument('--run', action='store_true', help='Start one metered cloud run; default only prints input')
    parser.add_argument('--format', choices=['json', 'csv'], default='json')
    parser.add_argument('--output', type=Path, help='Create a new output file; existing files are not overwritten')
    args = parser.parse_args()
    example = json.loads((ROOT / 'examples' / (args.example + '.json')).read_text())
    if not args.run:
        print(json.dumps(example, ensure_ascii=False, indent=2))
        print('Dry-run only. Add --run to start one metered run ($0.15 event limit; platform costs extra).', file=sys.stderr)
        return
    if args.output and args.output.exists():
        parser.error('Output file already exists; choose a new path before starting a paid run')
    token = os.environ.get('APIFY_TOKEN', '').strip()
    if not token:
        parser.error('Set APIFY_TOKEN in your environment; never paste it into a public issue')
    rows = collect(Api(token), example)
    text = csv_text(rows) if args.format == 'csv' else json.dumps(rows, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        with args.output.open('x', encoding='utf-8', newline='') as handle:
            handle.write(text)
    else:
        print(text, end='')

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
