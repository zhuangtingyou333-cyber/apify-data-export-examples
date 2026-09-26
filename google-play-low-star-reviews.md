# Export 1- and 2-Star Google Play Reviews

Export Google Play reviews with ratings, dates, app versions and available developer replies for Android release monitoring. Batch apps and locales, filter low-star reviews, and export CSV or JSON.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/google-play-reviews-scraper-api/examples/export-low-star-google-play-reviews?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/google-play-low-star-reviews-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/google-play-low-star-reviews-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 5 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Replace `appIds` with package IDs, then choose `country`, `language` and `ratingFilter`. The sample requests only scores 1 and 2, with a total limit of five.

```json
{
  "appIds": [
    "com.whatsapp"
  ],
  "country": "us",
  "language": "en",
  "ratingFilter": [
    1,
    2
  ],
  "maxReviews": 5
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py google-play-low-star-reviews
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py google-play-low-star-reviews --run --format csv --output results-google-play-low-star-reviews.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $0.08 | $0.07 | $0.06 | $0.05 |

Rates per **1,000 delivered reviews**. Actor-run resources are included. No separate Actor-start fee or monthly rental. Later storage/export and external services can have account-level charges.

Five delivered reviews cost **$0.00040** at the Free-plan rate, including Actor-run resources and with no separate start fee.

The Console example has a $0.03 Actor-event cap, 256 MB memory and a 240-second timeout. Actor-run resources are included; downstream services can charge separately.

Country and language select query locales; they do not translate or classify each review. Reply/version fields may be absent. Low-star exports are not representative of all customers; filtering may require extra source requests.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/google-play-reviews-scraper-api) · [All ten workflows](actor-workflows.md)
