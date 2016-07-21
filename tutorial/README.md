scrapy crawl dmoz -o dmoz.json
cat dmoz.json | python -m json.tool | less
