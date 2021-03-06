# -*- coding: utf-8 -*-

# Bx.in.th Api 
# https://bittrex.com/Home/Api
# Added by : Theppasith N. 
__author__ = "tutorgaming@gmail.com"

from exchange import Exchange, CURRENCY

class Bxinth(Exchange):
    """
    Bx.in.th Exchange class
    """
    CONFIG = {
        'name' : 'BX.in.th',
        'default_label': 'current',
        'ticker' : 'https://bx.in.th/api/',
        'asset_pairs': [
            {
                'isocode' : 'XXBTCZTHB',
                'pair' : 'XXBTCZTHB',
                'name' : 'BTC to THB',
                'volumelabel' : 'BTC',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 1,
                'primary_currency': 'THB',
                'secondary_currency': 'BTC'
            },
            {
                'isocode' : 'XXETHZTHB',
                'pair' : 'XXETHZTHB',
                'name' : 'ETH TO THB',
                'volumelabel' : 'ETH',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 21,
                'primary_currency': 'THB',
                'secondary_currency': 'ETH'
            },
            {
                'isocode' : 'XXDASZTHB',
                'pair' : 'XXDASZTHB',
                'name' : 'DASH TO THB',
                'volumelabel' : 'DAS',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 22,
                'primary_currency': 'THB',
                'secondary_currency': 'DAS'
            },
            {
                'isocode' : 'XXREPZTHB',
                'pair' : 'XXREPZTHB',
                'name' : 'REP TO THB',
                'volumelabel' : 'REP',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 23,
                'primary_currency': 'THB',
                'secondary_currency': 'REP'
            },
            {
                'isocode' : 'XXGNOZTHB',
                'pair' : 'XXGNOZTHB',
                'name' : 'GNO TO THB',
                'volumelabel' : 'GNO',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 24,
                'primary_currency': 'THB',
                'secondary_currency': 'GNO'
            },
            {
                'isocode' : 'XXRPZTHB',
                'pair' : 'XXRPZTHB',
                'name' : 'XRP TO THB',
                'volumelabel' : 'XRP',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 25,
                'primary_currency': 'THB',
                'secondary_currency': 'XRP'
            },
            {
                'isocode' : 'XXOMGZTHB',
                'pair' : 'XXOMGZTHB',
                'name' : 'OMG TO THB',
                'volumelabel' : 'OMG',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 26,
                'primary_currency': 'THB',
                'secondary_currency': 'OMG'
            },
            {
                'isocode' : 'XXBCHZTHB',
                'pair' : 'XXBCHZTHB',
                'name' : 'BCH TO THB',
                'volumelabel' : 'BCH',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 27,
                'primary_currency': 'THB',
                'secondary_currency': 'BCH'
            },
            {
                'isocode' : 'XXEVXZTHB',
                'pair' : 'XXEVXZTHB',
                'name' : 'EVX TO THB',
                'volumelabel' : 'EVX',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 28,
                'primary_currency': 'THB',
                'secondary_currency': 'EVX'
            },
            {
                'isocode' : 'XXXZCZTHB',
                'pair' : 'XXXZCZTHB',
                'name' : 'XZC TO THB',
                'volumelabel' : 'XZC',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 29,
                'primary_currency': 'THB',
                'secondary_currency': 'XZC'
            },
            {
                'isocode' : 'XXLTCZTHB',
                'pair' : 'XXLTCZTHB',
                'name' : 'LTC TO THB',
                'volumelabel' : 'LTC',
                'currency' : CURRENCY['thb'],
                'pairing_id' : 30,
                'primary_currency': 'THB',
                'secondary_currency': 'LTC'
            }
        ]
    }

    def get_ticker(self):
        return self.config['ticker']

    def _parse_result(self, data):
        database = []
        # convert key value to array 

        for key,value in data.items():
            database.append(value)

        selected_isocode = self.asset_pair


        # Select result by its isocode
        selected_asset = [item for item in self.config['asset_pairs'] if item['isocode'] == selected_isocode][0]

        query_result = [item for item in database 
                        if item['primary_currency'] == selected_asset['primary_currency'] and
                           item['secondary_currency'] == selected_asset['secondary_currency'] ][0]

        
        current = float(query_result['last_price'])

        bids_highbid = float(query_result['orderbook']['bids']['highbid']) #Buy price 
        bids_volume = float(query_result['orderbook']['bids']['volume'])
        
        asks_volume = float(query_result['orderbook']['asks']['volume'])
        asks_highbid = float(query_result['orderbook']['asks']['highbid']) #Sell price
        
        volume = float(query_result['volume_24hours'])
        
        return {
          'cur': current,
          'bid': bids_highbid,
          'high': None,
          'low': None,
          'ask': asks_highbid,
          'vol': volume
        }