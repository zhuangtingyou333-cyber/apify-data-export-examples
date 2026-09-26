# Export App Store reviews by country to CSV or JSON

Compare the same app across Apple storefronts while retaining the country on every review. This walkthrough starts with Instagram (app ID `389801252`) in the US, UK and Germany.

Maintained by the publisher of this paid Actor; created with AI assistance. This is a small integration example, not a representative study of users or an independent recommendation.

## Inspect the output without an account

[View JSON](app-store-countries-preview-20260927.json) · [Download CSV](app-store-countries-preview-20260927.csv)

The preview contains one selected review from each country from an owner-run check on September 27, 2026 (UTC+8). It is a dated sample, not a live feed. Reviewer names are omitted. `textExcerpt` is a shortened preview-only field; the actual Actor returns the review body in `text` and additional fields. Unknown source metadata stays null.

## Run a small export

[Open the prefilled country example](https://apify.com/peerless_columbine/apple-app-store-reviews-scraper-api/examples/export-app-store-reviews-by-country?utm_source=github&utm_medium=tutorial&utm_campaign=country_reviews_20260927).

1. Sign in to your own Apify account and review the input.
2. Change `appIds` and `countries` if needed, keeping the small limits for the first run.
3. Start, then open the dataset and export CSV, Excel or JSON.

```json
{
  "appIds": [
    "389801252"
  ],
  "countries": [
    "us",
    "gb",
    "de"
  ],
  "sourceMode": "archive",
  "maxReviewsPerAppCountry": 5,
  "maxItems": 15,
  "maxPages": 1
}
```

`maxReviewsPerAppCountry: 5` applies separately to each app/storefront. `maxItems: 15` is the total cap for this one-app, three-country sample. Keep the total cap at least as large as the number of app/country combinations times the per-combination cap if you want room for every target. This does not guarantee a target has enough available reviews. `maxPages: 1` deliberately bounds the initial scan.

This exact preset returned 15 reviews: five each from US, GB and DE. Country selects a storefront, not a translation language. The source may include reviews in other languages. See `OUTPUT` and source diagnostics for partial or failed targets; a truncated sample is not full history.

## Cost before you run

The current Free/Bronze/Silver/Gold+ result prices are $0.08/$0.07/$0.06/$0.05 per 1,000 delivered reviews, plus platform resources. Fifteen results cost $0.00120 in result fees on the Free plan. The owner test used about $0.000437 in resources, giving an illustrative Free-plan total of about $0.00164 for the same usage. This is not a fixed quote; plan rates, retries and later storage/exports affect costs. The public task has a $0.03 event cap and 180-second timeout; the event cap excludes separate platform resources. Check the live [Pricing tab](https://apify.com/peerless_columbine/apple-app-store-reviews-scraper-api/pricing).

## Use the same input from Python

Download [the workflow starter](apify-workflow-starter-20260927.zip), unzip it, and use Python 3.9+:

```sh
python3 run_example.py app-store-three-countries
```

This only previews the input. After setting your own `APIFY_TOKEN` in your environment:

```sh
python3 run_example.py app-store-three-countries --run --format csv --output reviews.csv
```

The runner starts one metered run, with a $0.15 event cap and 180-second timeout; platform resources are additional. It refuses to overwrite an existing output file and does not automatically retry a start request.

## Repeat without mixing storefronts

Keep `(appId, country, id)` as the downstream deduplication key. The Actor's within-run deduplication does not automatically deduplicate separate scheduled runs. For release monitoring, use explicit date filters such as `since`, retain overlapping exports, and deduplicate in your destination. Re-fetched delivered reviews may be billed again. Save and schedule a configuration only after checking one successful run and its cost.

175 archive/Mac storefront routes are configured, but app availability and review history vary. RSS has a 500-recent-review ceiling per app/storefront; archive mode is also bounded and does not promise complete history. Available app-version metadata can be missing.

[Use these Actors with an AI assistant](ai-assistant-setup.md) · [Full Actor reference](https://apify.com/peerless_columbine/apple-app-store-reviews-scraper-api)
