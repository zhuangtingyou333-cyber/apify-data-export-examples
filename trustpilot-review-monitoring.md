# Export Recent Trustpilot Reviews and Company Replies

Export public Trustpilot reviews, ratings, dates and available company replies for reputation monitoring. Filter language, rating and publication boundaries, and retain company context with the review.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/trustpilot-reviews-data-scraper/examples/export-trustpilot-reviews-and-replies?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/trustpilot-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/trustpilot-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 5 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Replace `companyUrls` with domains or Trustpilot company URLs. Use the input fields for language, star and date filters; URL query parameters are ignored.

```json
{
  "companyUrls": [
    "pipedrive.com"
  ],
  "maxReviewsPerCompany": 5,
  "languages": [
    "all"
  ],
  "sort": "recency",
  "includeCompanyInfo": true
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py trustpilot
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py trustpilot --run --format csv --output results-trustpilot.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $0.3 | $0.27 | $0.22 | $0.1 |

Rates per **1,000 delivered reviews**. No custom start fee. Browser runtime and other platform resources are additional.

At the Free-plan result rate, this 5-record sample adds $0.00150 in event fees. The owner check recorded $0.001197 in resources, giving an illustrative **$0.00270 combined** at that result rate and resource usage. Actual costs vary with retries, proxy traffic, storage and exports.

The Console example has a $0.15 Actor-event cap, 1024 MB memory and a 240-second timeout. The event cap does not cap separate platform resources.

Complete historical coverage is not guaranteed. Replies are included only when published. Source totals and filtered feeds may disagree. Keep browser memory at 1 GB for this starter; a 256 MB trial crashed during navigation.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/trustpilot-reviews-data-scraper) · [All ten workflows](actor-workflows.md)
