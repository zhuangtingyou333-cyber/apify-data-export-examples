# Export Workday Jobs with Descriptions and Salaries

Export jobs from public Workday career sites, including descriptions, locations, posting dates and salaries where published. Search keywords and collect multiple employer boards into CSV or JSON.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/workday-public-jobs-data/examples/export-workday-jobs-with-details?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/workday-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/workday-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 5 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Replace `startUrls` with a public Workday career-site URL. Keep `includeDetails: true` for descriptions and salary evidence; use `searchText` and date filters for narrower collections.

```json
{
  "startUrls": [
    {
      "url": "https://workday.wd5.myworkdayjobs.com/Workday"
    }
  ],
  "maxJobsPerSite": 5,
  "includeDetails": true
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py workday
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py workday --run --format csv --output results-workday.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $0.08 | $0.08 | $0.072 | $0.064 |

Rates per **1,000 delivered jobs**. Actor-run resources are included. An Actor-start event costs $0.0005 per GB of run memory, minimum one event, including empty or failed runs. Later storage/export services can charge separately.

Five delivered jobs cost $0.00040 at the Free-plan result rate, plus the minimum $0.0005 start event: **$0.00090 for this 256 MB starter**. Actor-run resources are included.

The Console example has a $0.15 Actor-event cap, 256 MB memory and a 240-second timeout. Actor-run resources are included; downstream services can charge separately.

Public recruiting sites are supported; internal HR portals are not. Salary values depend on employer disclosures and may be null. Result caps bound output, not every source request.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/workday-public-jobs-data) · [All ten workflows](actor-workflows.md)
