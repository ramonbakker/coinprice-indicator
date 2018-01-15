# -*- coding: utf-8 -*-

# Nocks
# https://docs.nocks.com/#trade-market-get
# 
'''
Response example
{"data":{"code":"NLG-EUR","last":{"amount":"0.3478","currency":"EUR"},"volume":{"amount":"440039.8744","currency":"EUR"},"low":{"amount":"0.3230","currency":"EUR"},"high":{"amount":"0.3670","currency":"EUR"},"buy":{"amount":"0.3440","currency":"EUR"},"sell":{"amount":"0.3478","currency":"EUR"},"is_active":true,"resource":"trade-market"},"status":200}
'''

__author__ = "ramon.b@live.nl"

from exchange import Exchange, CURRENCY

class Nocks(Exchange):
  CONFIG = {
    'name': 'Nocks',
    'ticker': 'https://api.nocks.com/api/v2/trade-market',
    'asset_pairs': [
      {
        'isocode': 'XNLGZEUR',
        'pair': 'NLG-EUR',
        'name': 'NLG to EUR',
        'currency': CURRENCY['eur']
      }
    ]
  }

  def get_ticker(self):
    return self.config['ticker'] + '/' + self.pair

  def _parse_result(self, asset):
    asset = asset.get('data')

    label = asset.get('last').get('amount')
    bid = asset.get('buy').get('amount')
    high = asset.get('high').get('amount')
    low = asset.get('low').get('amount')
    ask = asset.get('sell').get('amount')
    vol = asset.get('volume').get('amount')

    return {
      'label': label,
      'bid': bid,
      'high': high,
      'low': low,
      'ask': ask,
      'vol': vol
    }