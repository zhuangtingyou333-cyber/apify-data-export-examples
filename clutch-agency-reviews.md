# Export a Clutch Agency with Reviews and Insights

Export Clutch company profiles, project reviews and buyer-company evidence for agency comparison and vendor research. A delivered company bundle includes requested public reviews, buyer leads and deterministic review insights.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/clutch-companies-reviews-scraper/examples/export-clutch-agency-profile?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/clutch-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/clutch-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 1 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Replace `startUrls` with a Clutch profile or directory URL. The starter explicitly enables `includeCompanyReviews`, `extractBuyerLeads` and `reviewInsights`; no AI provider key is needed for deterministic insights.

```json
{
  "startUrls": [
    {
      "url": "https://clutch.co/profile/ddnyc-0"
    }
  ],
  "maxItems": 1,
  "maxPages": 1,
  "maxReviewsPerCompany": 5,
  "proxy": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ]
  },
  "includeCompanyReviews": true,
  "extractBuyerLeads": true,
  "reviewInsights": true
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py clutch
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py clutch --run --format csv --output results-clutch.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $1.4 | $1.4 | $1.26 | $1.12 |

Rates per **1,000 delivered company bundles**. The result fee includes requested public reviews, buyer leads and deterministic insights for that company. Runtime/residential proxy are additional; optional AI provider charges are separate.

At the Free-plan result rate, this 1-record sample adds $0.00140 in event fees. The owner check recorded $0.000115 in resources, giving an illustrative **$0.00152 combined** at that result rate and resource usage. Actual costs vary with retries, proxy traffic, storage and exports.

The Console example has a $0.15 Actor-event cap, 512 MB memory and a 240-second timeout. The event cap does not cap separate platform resources.

The starter uses an Apify residential proxy; your account needs access and proxy traffic costs extra. Profiles, review depth and buyer-company fields depend on public source access. Five reviews are a bounded sample, not the agency history.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/clutch-companies-reviews-scraper) · [All ten workflows](actor-workflows.md)
