#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyquery import PyQuery


def get_exchange_rate():
    html = PyQuery('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    currency_names = html('div.hidden-phone').text().split()
    bid_filter = 'td.rate-content-cash[data-table="本行現金買入"]'
    offer_filer = 'td.rate-content-cash[data-table="本行現金賣出"]'
    currency_bids = html(bid_filter).text().split()
    currency_offers = html(offer_filer).text().split()
    currency = {}

    price_idx = 0
    for idx, name in enumerate(currency_names):

        if idx % 2 == 0:

            # EX: "美金": { "bids": "30.00", "offers": "30.50" }
            currency[name] = {
                "bids": currency_bids[price_idx],
                "offers": currency_offers[price_idx]
            }
           
            price_idx += 1
    # {"美元":{"bids": 30,"offers": 30},""}
    return currency
