# WebScraperCS11

## Project implementation steps

## Stages  1 - 3

1. Provide url of the product's opinions page
2. Send Request to provided  url
3. Fetch product name
4. Fetchall opinion from the webpage
5. Parse opinions to extract required data
6. Check if theere is next page with opinions
7. Repeat steps4-6 for all pages with opinions about product
8. Save acquired opnions

## Product Inputs

### Product Codes
-187595793
-133523566
-158068054
-90558992
### Opinion structure


| component | name | selector |
|-----------|------|----------|
| opinion ID | opinion_id |[data-entry-id]|
| opinion's author | author |span.user-post__author-name |
| author's recommendation | recommendation | span.user-post__author-recomend > em|
| score expressed in number of stars | score | span.user-post__score-count |
| opinion's content | content | div.user-post__text |
| list of product advantages | pros | div.review-feature__item--positive |
| list of product disadvantages | cons | div.review-feature__item--negative |
| how many users think that opinion was helpful | helpful | button.vote-yes > span |
| how many users think that opinion was unhelpful | unhelpful | button.vote-no > span |
| publishing date | publish_date | span.user-post__published > time:nth-child(1)[datetime] |
| purchase date | purchase_date | span.user-post__published > time:nth-child(2)[datetime] |