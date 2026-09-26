# Google News API: export brand mentions to CSV or JSON

Collect a bounded news feed for a company or topic with headlines, publication dates, publishers and links. This walkthrough searches NVIDIA in the US English edition over the last seven days.

Maintained by the publisher of this paid Actor; created with AI assistance. The example is a keyword collection, not an exhaustive brand-monitoring service or an independent recommendation.

## Preview five actual results

[View JSON](google-news-brand-preview-20260927.json) · [Download CSV](google-news-brand-preview-20260927.csv)

These are selected fields from an owner-run check on September 27, 2026 (UTC+8), not current results. The preview omits article bodies. Results can include the company's own publications as well as third-party coverage; keyword search does not establish sentiment or relevance by itself.

## Try it without code

[Open the prefilled brand-news example](https://apify.com/peerless_columbine/google-news-scraper-api/examples/export-google-news-keyword-alerts?utm_source=github&utm_medium=tutorial&utm_campaign=brand_news_20260927), sign in to your own account, inspect the limits, then start.

```json
{
  "queries": [
    "NVIDIA"
  ],
  "region_language": "US:en",
  "dateRange": "7d",
  "maxArticles": 5,
  "maxItems": 5,
  "resolvePublisherUrls": true,
  "extractFullText": false,
  "extractImages": false,
  "maxFeedRequestsPerQuery": 2
}
```

Change `queries` to your company or topic. `region_language` selects the edition, not article translation. `dateRange` is a rolling window. The small `maxArticles` and `maxItems` caps limit delivered rows. This preset requests publisher links but does not fetch full article text or images.

The exact owner test returned five non-error articles with titles, publishers, publication dates and resolved links. Publisher decoding and optional enrichment remain source-dependent. Open `SOURCE_DIAGNOSTICS` and inspect `coverage` and `warnings` when results are incomplete. Five results are a sample of the source feed, not every mention in seven days.

## Know the cost

The current Free/Bronze/Silver/Gold+ result prices are $0.75/$0.60/$0.45/$0.30 per 1,000 articles, plus platform resources. Five results cost $0.00375 in result fees on the Free plan. The owner test used about $0.000324 in resources, giving an illustrative total of $0.00407 at the Free rate for the same usage. Retries, optional rendering/proxies and later storage/exports can add cost. Both the public example and Python runner use a $0.15 event cap and 180-second timeout; this event cap excludes platform resources. Check the [Pricing tab](https://apify.com/peerless_columbine/google-news-scraper-api/pricing).

## Call the API with Python

Download [the workflow starter](apify-workflow-starter-20260927.zip), unzip it, and preview the input:

```sh
python3 run_example.py google-news-brand-monitoring
```

After setting your own `APIFY_TOKEN` in your environment, explicitly run once:

```sh
python3 run_example.py google-news-brand-monitoring --run --format csv --output news.csv
```

The runner prints the Console run link, waits for completion, and exports the dataset. An existing output file is preserved. If the connection fails after starting, check that link before starting another metered run.

## Build a recurring news feed

Keep source links, publication dates and retrieval timestamps. Deduplicate overlapping exports downstream using `googleNewsUrl` when present, falling back to a resolved publisher URL; neither is a perfect identifier for every syndicated or updated story. Every scheduled run can deliver and bill overlapping articles again. A rolling seven-day search is useful for a first check; use a narrower window after inspecting real output. Set up scheduling in your own account only when ready.

For larger bounded keyword collections, see [the seven-day industry-news example](https://apify.com/peerless_columbine/google-news-scraper-api/examples/collect-a-week-of-industry-news). Date splitting can collect beyond one RSS page but does not guarantee complete archives. Topics/sections have different source limits. Optional article text cannot bypass unavailable or restricted publishers.

[Use these Actors with an AI assistant](ai-assistant-setup.md) · [Full Actor reference](https://apify.com/peerless_columbine/google-news-scraper-api)
