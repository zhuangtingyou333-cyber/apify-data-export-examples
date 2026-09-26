# Search Bilibili Videos by Chinese Keyword

Search Bilibili (哔哩哔哩) videos for Chinese-language topic research and brand monitoring. Export titles, publication dates, video links and available engagement counts; use the other modes for creator profiles, comments and timed danmaku.

Maintained by the publisher of this paid Actor, with AI assistance. Runs use your own Apify credits.

## Inspect, then run

**[Try the prefilled example](https://apify.com/peerless_columbine/bilibili-all-in-one-scraper-api/examples/search-bilibili-videos-by-keyword?utm_source=actor_readme&utm_medium=example&utm_campaign=portfolio_20260927)** · **[Inspect sample JSON before signing in](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/bilibili-keyword-search-preview-20260927.json)** · **[Download sample CSV](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/bilibili-keyword-search-preview-20260927.csv)**

The dated preview contains selected fields from a September 27, 2026 owner check: 3 non-error records. It is not live data. Full descriptions, review bodies and personal reviewer identifiers are omitted; excerpts and counts are preview-only summaries.

1. Open the prefilled example and inspect the target, limits and Pricing tab.
2. Start one run, then inspect its dataset and `OUTPUT` diagnostics. A successful status alone is not proof of exhaustive coverage.
3. Export CSV, Excel or JSON. Nested fields are easiest to preserve in JSON.

Change `searchQuery`, then choose `sortOrder` and a small `maxResults`. Search uses Bilibili relevance; returned titles need not contain the exact phrase.

```json
{
  "mode": "search",
  "searchQuery": "人工智能教程",
  "sortOrder": "pubdate",
  "maxResults": 3
}
```

## Python integration

[Download the starter ZIP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/raw/refs/heads/main/apify-portfolio-starter-20260927.zip). Python 3.9+ and standard library only. Preview without a cloud run:

```sh
python3 run_example.py bilibili-keyword-search
```

Set your own `APIFY_TOKEN` in your shell environment, then explicitly start a metered run:

```sh
python3 run_example.py bilibili-keyword-search --run --format csv --output results-bilibili-keyword-search.csv
```

The Python starter applies a $0.15 event limit and 180-second timeout; the Console preset uses the options below. The script inherits the Actor's default memory, including 1 GB for Trustpilot. Never publish tokens. It does not retry run-start requests or overwrite existing exports. CSV formula-like source strings are escaped; nested data is serialized as JSON.

## Price and scope

| Free plan | Starter / Bronze | Scale / Silver | Business / Gold+ |
|---:|---:|---:|---:|
| $3 | $2.5 | $2 | $1.5 |

Rates per **1,000 video discovery results**. These rates apply to discovery results. Video details, creator/relation/live records and danmaku/profile bundles use separate event types in Pricing.

At the Free-plan result rate, this 3-record sample adds $0.00900 in event fees. The owner check recorded $0.000208 in resources, giving an illustrative **$0.00921 combined** at that result rate and resource usage. Actual costs vary with retries, proxy traffic, storage and exports.

The Console example has a $0.03 Actor-event cap, 256 MB memory and a 240-second timeout. The event cap does not cap separate platform resources.

Full subtitle text is not included. Creator and live endpoints may be restricted or partial. Search counts are source-provided and are not a complete engagement audit.

## Use with an AI assistant

[Connect the named tool with MCP](https://github.com/zhuangtingyou333-cyber/apify-data-export-examples/blob/main/ai-assistant-setup.md). Ask it to use this exact Actor and the bounded input above, inspect the price, start one run and read the dataset plus coverage diagnostics. Do not create schedules or silently retry a run start. MCP Actor inputs do not expose the starter's dollar cap; use Console/Python when you need that explicit event limit.

[Actor and full reference](https://apify.com/peerless_columbine/bilibili-all-in-one-scraper-api) · [All ten workflows](actor-workflows.md)
