# Export Greenhouse Jobs with Descriptions | 6 ATS

Export jobs from Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters and Personio into one schema. Collect descriptions, locations and available salaries for job feeds and hiring research.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/multi-ats-jobs-scraper/examples/export-greenhouse-jobs-with-descriptions?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ats-aggregation-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/ats-aggregation-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 5 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Replace the company/provider in `companies`, or use supported board URLs. Keep `includeDescriptions: true` and `outputProfile: "full"` when you need description fields.

```json
{
  "companies": [
    {
      "ats": "greenhouse",
      "company": "stripe"
    }
  ],
  "maxJobsPerCompany": 5,
  "includeDescriptions": true,
  "outputProfile": "full"
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py ats-aggregation
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py ats-aggregation --run --format csv --output results-ats-aggregation.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $1 | $0.9 | $0.8 | $0.7 |

Rates per **1,000 delivered jobs**. Company hiring reports use a separate event. Check Pricing before enabling reports or combined workflows.

At the Free-plan result rate, this 5-record sample adds $0.00500 in event fees. The owner check recorded $0.000199 in resources, giving an illustrative **$0.00520 combined** at that result rate and resource usage. Actual costs vary with retries, proxy traffic, storage and exports.

The Console example has a $0.15 Actor-event cap, 256 MB memory and a 240-second timeout. The event cap does not cap separate platform resources.

This sample checks Greenhouse, not all providers at once. Salary, seniority and dates may be absent; derived fields include evidence. Incomplete snapshots must not be treated as proof of closed jobs.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/multi-ats-jobs-scraper) · [All ten workflows](actor-workflows.md)
