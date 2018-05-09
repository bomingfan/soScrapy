# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpider(scrapy.Spider):
    name = "scrapso"
    start_urls = [
        'https://stackoverflow.com/jobs?sort=p&pg=1',
    ]

    def parse(self, response):
        for job in response.css("div.-job-summary"):
            yield {
                'name': job.css("h2.g-col10 > a::attr(title)").extract_first(),
                'tags': job.css("p > a.post-tag::text").extract()
            }

        next_page_url = response.css("div.pagination > a.test-pagination-next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
