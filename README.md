# Apify data export examples: jobs, app reviews, trends and news

Small Python examples for running ten hosted Apify Actors and exporting JSON or CSV. Python 3.9+; no npm or third-party Python packages required.

**Publisher disclosure:** These examples are maintained for the paid Actors published by `peerless_columbine`. The examples were developed with AI assistance. The hosted Actors charge for delivered results; most Actors add platform resource costs. Google Play Reviews and Workday include Actor-run resources; Workday also has its listed start event. Check each Actor's live Pricing tab. These are integration examples, not independent product recommendations.

## Two focused workflows to start with

| Goal | Walkthrough | Inspect data before running |
|---|---|---|
| Export App Store reviews separately for US, UK and Germany | [Country-review guide](app-store-reviews-by-country.md) | [JSON preview](app-store-countries-preview-20260927.json) / [CSV](app-store-countries-preview-20260927.csv) |
| Export a company's recent Google News mentions | [Brand-news guide](google-news-brand-monitoring.md) | [JSON preview](google-news-brand-preview-20260927.json) / [CSV](google-news-brand-preview-20260927.csv) |

[Download the workflow starter](apify-workflow-starter-20260927.zip) · [Connect both Actors to an AI assistant](ai-assistant-setup.md)

The September 27 owner checks returned 15 reviews (five per country) and five news articles. Samples are dated, with selected fields; these are not live feeds or proof of customer adoption. The guides explain exact inputs, source limits and illustrative costs. The original ten examples remain available below.

## Inspect sample data before creating an account

Download [the Python starter ZIP](apify-export-examples-20260927.zip), or inspect these small historical exports without an Apify login or a cloud run:

| Sample | JSON | CSV |
|---|---|---|
| Five Google News headlines and publisher links | [JSON](google-news-selected-fields-20260918.json) | [CSV](google-news-selected-fields-20260918.csv) |
| Five Stripe jobs from Greenhouse | [JSON](ats-jobs-selected-fields-20260918.json) | [CSV](ats-jobs-selected-fields-20260918.csv) |

These are selected fields from owner-run checks on September 18, 2026 (UTC+8), not live feeds or customer data. Article bodies and job descriptions are omitted from these previews; the Actors' full output schemas are documented on their product pages. Live results can differ.

## Try without API code

Open a preconfigured example below, inspect its inputs and cost, then start it in Apify Console. Start with a small result limit before scheduling larger jobs.

| Example | Preconfigured input |
|---|---|
| `google-trends` | [Export Google Trends Keyword Interest](https://apify.com/peerless_columbine/google-trends-scraper-api/examples/compare-google-trends-keyword-interest?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `google-news` | [Export Google News by Keyword](https://apify.com/peerless_columbine/google-news-scraper-api/examples/export-google-news-keyword-alerts?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `clutch` | [Export a Clutch Agency Profile](https://apify.com/peerless_columbine/clutch-companies-reviews-scraper/examples/export-clutch-agency-profile?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `ats-aggregation` | [Export Greenhouse Jobs with Descriptions](https://apify.com/peerless_columbine/multi-ats-jobs-scraper/examples/export-greenhouse-jobs-with-descriptions?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `trustpilot` | [Export Trustpilot Reviews and Replies](https://apify.com/peerless_columbine/trustpilot-reviews-data-scraper/examples/export-trustpilot-reviews-and-replies?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `workday` | [Export Workday Jobs with Details](https://apify.com/peerless_columbine/workday-public-jobs-data/examples/export-workday-jobs-with-details?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `wellfound` | [Export a Wellfound Job Search Sample](https://apify.com/peerless_columbine/wellfound-jobs-scraper-api/examples/export-wellfound-job-search-sample?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `app-store-reviews` | [Export App Store reviews by country](https://apify.com/peerless_columbine/apple-app-store-reviews-scraper-api/examples/export-app-store-reviews-by-country?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `google-play-low-star-reviews` | [Export low-star Google Play reviews](https://apify.com/peerless_columbine/google-play-reviews-scraper-api/examples/export-low-star-google-play-reviews?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |
| `bilibili-keyword-search` | [Search Bilibili by keyword](https://apify.com/peerless_columbine/bilibili-all-in-one-scraper-api/examples/search-bilibili-videos-by-keyword?utm_source=github&utm_medium=example&utm_campaign=first_users_202609) |

## Python quick start

1. Download this repository and use Python 3.9 or newer.
2. Inspect the input without starting or paying for a run:

```sh
python3 run_example.py ats-aggregation
```

3. Set your own Apify API token in your shell environment as `APIFY_TOKEN`. Keep it out of code, screenshots, commits and public issues.
4. Explicitly start one cloud run and create a CSV:

```sh
python3 run_example.py ats-aggregation --run --format csv --output results-jobs.csv
```

The example starts one run with a **$0.15 Actor-event limit and 180-second timeout**. For Actors that add platform resource fees, $0.15 is only an event cap. For Google Play Reviews and Workday, Actor-run resources are included in event pricing. Downstream services can charge separately. Existing output files are not overwritten. Run-start requests are not automatically retried, so a connection error cannot silently create a second job. Check the printed Console link before starting another run.

## Adapt the examples

Edit the `input` object in one of the `examples/*.json` files:

- Jobs: change the ATS/provider and company slug, or the Workday career-site URL. Published salary fields can be absent.
- App reviews: keep country and language explicit. Low-star selection is useful for triage but is not representative of all customers.
- Google Trends: interest is normalized, not absolute search volume. One result record contains a report, not one time point.
- Google News: the basic example returns article metadata and publisher links; it does not promise access to paywalled full text.
- Trustpilot and Clutch: result limits are ceilings, not guarantees of complete history. Clutch's starter uses residential proxy, which adds platform cost.
- Wellfound: free-text matching is applied to the visible public feed. It is not an exhaustive site-wide search.

The JSON output retains nested fields. CSV serializes nested values as JSON strings and prefixes source strings that could be interpreted as spreadsheet formulas.

## Verification

On September 18, 2026 (UTC+8), bounded owner-run cloud checks returned real records for the seven newly linked examples. App Store, Google Play and Bilibili examples have bounded cloud checks dated September 11. These checks establish sample execution, not customer adoption, complete historical coverage, or guaranteed future availability. Source websites and records change.

Run the integration-runner tests without making network requests or starting paid jobs:

```sh
python3 -m unittest discover -s tests
```

For a failed run, inspect its log and OUTPUT record before increasing limits. Report reproducible issues through the relevant Actor's Issues tab using non-sensitive inputs and a description of expected versus observed results. Never publish API tokens.

Pricing and discovery update, September 27, 2026 (UTC+8): Google Play review event rates remain $0.08 / $0.07 / $0.06 / $0.05 per 1,000 according to plan, now including Actor-run resources and with no separate start fee. The latest owner-run check delivered 1,000 reviews. This is functional evidence, not evidence of external customers or exhaustive coverage. Collection stops after 15 minutes with an explicit limited-coverage report when needed.
