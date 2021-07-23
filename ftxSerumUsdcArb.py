import numpy as np
import pandas as pd
import requests
import json
import xlsxwriter
import time
import hmac
from requests import Request
import urllib.parse
from requests import Request, Session, Response
from ciso8601 import parse_datetime
import ftx
from solana.account import Account
from solana.publickey import PublicKey
from solana.rpc.types import TxOpts
from pyserum.connection import conn
import pyserum
from pyserum.enums import OrderType, Side
from pyserum.market import Market
from pyserum.connection import get_live_markets, get_token_mints
from pyserum.open_orders_account import OpenOrdersAccount
from typing import Optional, Dict, Any, List
import requests
from Config import FTX_API, FTX_SECRET, solletKeyPair, ftxSubAccountName, usdcPubKey, solletPubKey

pp = 69
while pp == 69:
    try:
        client = ftx.FtxClient(api_key=FTX_API, api_secret=FTX_SECRET, subaccount_name=ftxSubAccountName)

        cc = conn("https://api.mainnet-beta.solana.com/")
        market_address_KinUsdc = "Bn6NPyr6UzrFAwC4WmvPvDr2Vm8XSUnFykM2aQroedgn"  # Address for KIN/USDC


        # Load the given market
        marketKinUsdc = Market.load(cc, market_address_KinUsdc)


        key_pair = solletKeyPair  # Supply the private key of the desired wallet and append it to a variable.
        account = Account(key_pair[:32])

        # Api Call
        """api_ftx_url_usd = "https://ftx.com/api/markets/KIN/USD/orderbook?depth=100"
        data_ftx_usd = requests.get(api_ftx_url_usd).json()"""

        api_ftx_url_perp = "https://ftx.com/api/markets/KIN-PERP/orderbook?depth=100"
        data_ftx_perp = requests.get(api_ftx_url_perp).json()


        def decimal_str(x: float, decimals: int = 10) -> str:
            return format(x, f".{decimals}f").lstrip().rstrip('0')


        # print(data['result']['bids'])


        def sort_ftx_perp_bid_prices():
            for i in data_ftx_perp['result']['bids']:
                perp_bid_prices_data = i[0]
                ftx_perp_bid_prices_raw.append(perp_bid_prices_data)


        ftx_perp_bid_prices_raw = []
        sort_ftx_perp_bid_prices()


        def sort_ftx_perp_ask_prices():
            for i in data_ftx_perp['result']['asks']:
                perp_ask_prices_data = i[0]
                ftx_perp_ask_prices_raw.append(perp_ask_prices_data)


        ftx_perp_ask_prices_raw = []
        sort_ftx_perp_ask_prices()


        def sort_ftx_perp_bid_sizes():
            for i in data_ftx_perp['result']['bids']:
                perp_bid_sizes_data = i[1]
                ftx_perp_bid_sizes.append(perp_bid_sizes_data)


        ftx_perp_bid_sizes = []
        sort_ftx_perp_bid_sizes()


        def sort_ftx_perp_ask_sizes():
            for i in data_ftx_perp['result']['asks']:
                ftx_perp_ask_sizes_data = i[1]
                ftx_perp_ask_sizes.append(ftx_perp_ask_sizes_data)


        ftx_perp_ask_sizes = []
        sort_ftx_perp_ask_sizes()



        def get_decimals_perp():
            for ftx_perp_bid in ftx_perp_bid_prices_raw:
                ftx_perp_bids = decimal_str(ftx_perp_bid)
                ftx_perp_bid_prices.append(ftx_perp_bids)

            for ftx_perp_ask in ftx_perp_ask_prices_raw:
                ftx_perp_asks = decimal_str(ftx_perp_ask)
                ftx_perp_ask_prices.append(ftx_perp_asks)


        ftx_perp_ask_prices = []
        ftx_perp_bid_prices = []
        get_decimals_perp()

        ftx_perp_highest_bid_price = float(ftx_perp_bid_prices[0])
        ftx_perp_lowest_ask_price = float(ftx_perp_ask_prices[0])
        ftx_perp_highest_bid_size = float(ftx_perp_bid_sizes[0])
        ftx_perp_lowest_ask_size = float(ftx_perp_ask_sizes[0])

        ftx_perp_second_highest_bid_price = float(ftx_perp_bid_prices[1])
        ftx_perp_third_highest_bid_price = float(ftx_perp_bid_prices[2])
        ftx_perp_fourth_highest_bid_price = float(ftx_perp_bid_prices[3])
        ftx_perp_fifth_highest_bid_price = float(ftx_perp_bid_prices[4])
        ftx_perp_sixth_highest_bid_price = float(ftx_perp_bid_prices[5])
        ftx_perp_seventh_highest_bid_price = float(ftx_perp_bid_prices[6])
        ftx_perp_eight_highest_bid_price = float(ftx_perp_bid_prices[7])
        ftx_perp_ninth_highest_bid_price = float(ftx_perp_bid_prices[8])
        ftx_perp_tenth_highest_bid_price = float(ftx_perp_bid_prices[9])
        ftx_perp_eleventh_highest_bid_price = float(ftx_perp_bid_prices[10])

        ftx_perp_second_highest_bid_size = float(ftx_perp_bid_sizes[1])
        ftx_perp_third_highest_bid_size = float(ftx_perp_bid_sizes[2])
        ftx_perp_fourth_highest_bid_size = float(ftx_perp_bid_sizes[3])
        ftx_perp_fifth_highest_bid_size = float(ftx_perp_bid_sizes[4])
        ftx_perp_sixth_highest_bid_size = float(ftx_perp_bid_sizes[5])
        ftx_perp_seventh_highest_bid_size = float(ftx_perp_bid_sizes[6])
        ftx_perp_eight_highest_bid_size = float(ftx_perp_bid_sizes[7])
        ftx_perp_ninth_highest_bid_size = float(ftx_perp_bid_sizes[8])
        ftx_perp_tenth_highest_bid_size = float(ftx_perp_bid_sizes[9])
        ftx_perp_eleventh_highest_bid_size = float(ftx_perp_bid_sizes[10])

        three_bid_sizes_summed = ftx_perp_highest_bid_size + ftx_perp_second_highest_bid_size + ftx_perp_third_highest_bid_size
        six_bid_sizes_summed = ftx_perp_highest_bid_size + ftx_perp_second_highest_bid_size + ftx_perp_third_highest_bid_size + ftx_perp_fourth_highest_bid_size + ftx_perp_fifth_highest_bid_size + ftx_perp_sixth_highest_bid_size
        eleven_bid_sizes_summed = ftx_perp_highest_bid_size + ftx_perp_second_highest_bid_size + ftx_perp_third_highest_bid_size + ftx_perp_fourth_highest_bid_size + ftx_perp_fifth_highest_bid_size + ftx_perp_sixth_highest_bid_size + ftx_perp_seventh_highest_bid_size + ftx_perp_eight_highest_bid_size + ftx_perp_ninth_highest_bid_size + ftx_perp_tenth_highest_bid_size + ftx_perp_eleventh_highest_bid_size




        # print(data)
        # print(data['data']['bids'])

        # Arrange the data
        def decimal_str(x: float, decimals: int = 10) -> str:
            return format(x, f".{decimals}f").lstrip().rstrip('0')




        serum_usdc_api_url = "https://serum-api.bonfida.com/orderbooks/KINUSDC"
        serum_data_usdc = requests.get(serum_usdc_api_url).json()


        # print(data)
        # print(data['data']['bids'])

        # Arrange the data

        def decimal_str(x: float, decimals: int = 10) -> str:
            return format(x, f".{decimals}f").lstrip().rstrip('0')


        serum_usdc_bid_prices_raw = [i['price'] for i in serum_data_usdc['data']['bids']]
        serum_usdc_ask_prices_raw = [i['price'] for i in serum_data_usdc['data']['asks']]
        serum_usdc_bid_sizes = [i['size'] for i in serum_data_usdc['data']['bids']]
        serum_usdc_ask_sizes = [i['size'] for i in serum_data_usdc['data']['asks']]


        def usdc_prices_get_decimals():
            for usdc_bid in serum_usdc_bid_prices_raw:
                usdc_bids = decimal_str(usdc_bid)
                serum_usdc_bid_prices.append(usdc_bids)

            for usdc_ask in serum_usdc_ask_prices_raw:
                usdc_asks = decimal_str(usdc_ask)
                serum_usdc_ask_prices.append(usdc_asks)


        serum_usdc_ask_prices = []
        serum_usdc_bid_prices = []
        usdc_prices_get_decimals()

        serum_usdc_lowest_ask_price = float(serum_usdc_ask_prices[0])
        serum_usdc_highest_bid_price = float(serum_usdc_bid_prices[0])
        serum_usdc_highest_bid_size = float(serum_usdc_bid_sizes[0])
        serum_usdc_lowest_ask_size = float(serum_usdc_ask_sizes[0])
        serum_usdc_second_highest_bid = float(serum_usdc_bid_prices[1])
        serum_usdc_third_highest_bid = float(serum_usdc_bid_prices[2])
        serum_usdc_fourth_highest_bid = float(serum_usdc_bid_prices[3])
        serum_usdc_fifth_highest_bid = float(serum_usdc_bid_prices[4])

        myOrders_KinUsdc = marketKinUsdc.load_orders_for_owner(
            owner_address=PublicKey(solletPubKey)
        )



        # print(myOrders_KinUsdc)

        def serum_openOrderPrices_KinUsdc():
            for orders in myOrders_KinUsdc:
                ooc_data = orders[5][0]
                open_order_prices_KinUsdc.append(ooc_data)


        open_order_prices_KinUsdc = []
        serum_openOrderPrices_KinUsdc()
        # print(open_order_prices)
        # print(myOrders)

        if open_order_prices_KinUsdc == []:
            KinUsdc_my_order_price = 0
        else:
            KinUsdc_my_order_price = open_order_prices_KinUsdc[0]



        # kin_short_size = 100000000 - open_order_sizes[0]
        # print(kin_short_size)

        # All prices variable checks the equality of open order prices, if all the open orders have the same price, all_prices will return True boolean, otherwise False.
        all_prices_KinUsdc = all(element == open_order_prices_KinUsdc[0] for element in open_order_prices_KinUsdc)
        # all_prices_KinUsdt = all(element == open_order_prices_KinUsdt[0] for element in open_order_prices_KinUsdt)



        def serum_openOrderSizes_KinUsdc():
            for sizes in myOrders_KinUsdc:
                osc_data = sizes[5][1]
                serum_open_order_sizes_KinUsdc.append(osc_data)


        serum_open_order_sizes_KinUsdc = []
        serum_openOrderSizes_KinUsdc()

        if serum_open_order_sizes_KinUsdc == []:
            KinUsdc_my_order_size = 0
        else:
            KinUsdc_my_order_size = serum_open_order_sizes_KinUsdc[0]



        ftx_open_orders = client.get_open_orders('KIN-PERP')
        try:
            ftx_open_order_price = ftx_open_orders[0]['price']
            ftx_open_order_size = ftx_open_orders[0]['size']
        except Exception:
            pass

        order_history_data = client.get_order_history('KIN-PERP')
        fill_size = order_history_data[0]['filledSize']
        avg_fill_price = order_history_data[0]['avgFillPrice']
        remaining_size = order_history_data[0]['remainingSize']
        # print(remaining_size)
        # print(fill_size)
        # print(avg_fill_price)
        order_size = 8000000
        kin_short_size_forUsdc = order_size - KinUsdc_my_order_size
        # kin_short_size_forUsdt = order_size - KinUsdt_my_order_size

        usd_value_KinUsdc = kin_short_size_forUsdc * serum_usdc_lowest_ask_price
        max_usd_value_KinUsdc = order_size * serum_usdc_lowest_ask_price

        # usd_value_KinUsdt = kin_short_size_forUsdt * serum_usdt_lowest_ask_price
        # max_usd_value_KinUsdt = order_size * serum_usdt_lowest_ask_price

        # kin_short_size * 1.05 >= fill_size >= kin_short_size * 0.95

        ts = int(time.time() * 1000)
        s = Session()
        request = Request('GET', 'https://ftx.com/api/wallet/balances')
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'
        if prepared.body:
            signature_payload += prepared.body
        signature_payload = signature_payload.encode()
        signature = hmac.new(FTX_SECRET.encode(), signature_payload, 'sha256').hexdigest()

        prepared.headers['FTX-KEY'] = FTX_API
        prepared.headers['FTX-SIGN'] = signature
        prepared.headers['FTX-TS'] = str(ts)
        prepared.headers['FTX-SUBACCOUNT'] = urllib.parse.quote('AA')

        response = s.send(prepared)
        ftx_wallet_data = response.json()


        # print(data)
        # print(data['result'][5]['coin'])

        def wallet_free_usd_holdings():
            for i in ftx_wallet_data['result']:
                if i['coin'] == str('USD'):
                    free_usd_data = i['free']
                    freeUsdHoldings.append(free_usd_data)


        freeUsdHoldings = []
        wallet_free_usd_holdings()

        free_usd_balance = freeUsdHoldings[0]
        # print(free_usd_balance)

        ts = int(time.time() * 1000)
        s = Session()
        request = Request('GET', 'https://ftx.com/api/positions')
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'
        if prepared.body:
            signature_payload += prepared.body
        signature_payload = signature_payload.encode()
        signature = hmac.new(FTX_SECRET.encode(), signature_payload, 'sha256').hexdigest()

        prepared.headers['FTX-KEY'] = FTX_API
        prepared.headers['FTX-SIGN'] = signature
        prepared.headers['FTX-TS'] = str(ts)
        prepared.headers['FTX-SUBACCOUNT'] = urllib.parse.quote('AA')

        response = s.send(prepared)
        ftx_positions_data = response.json()


        # print(ftx_positions_data)

        def ftx_kin_position_size():
            for i in ftx_positions_data['result']:
                if i['future'] == str('KIN-PERP'):
                    kin_position_size_data = i['size']
                    kinPositionSize.append(kin_position_size_data)


        kinPositionSize = []
        ftx_kin_position_size()
        kin_position_size_ftx = kinPositionSize[0]

        # print(kin_position_size)
        # print(remaining_size)

        kin_position_allowance = 1000000

        # or kin_position_size_ftx >= kin_short_size * 1.1
        # 1
        if ((myOrders_KinUsdc == []) and (ftx_open_orders != []) and (three_bid_sizes_summed >= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_third_highest_bid_price, remaining_size)
                print('#1')
            except Exception:
                print('Exception passed #1')
                pass
        else:
            pass

        # 2
        if ((myOrders_KinUsdc != []) and (ftx_open_orders != []) and (three_bid_sizes_summed >= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_third_highest_bid_price, remaining_size)
                print('#2')
            except Exception:
                print('Exception passed #2')
                pass
        else:
            pass

        # 3
        if ((myOrders_KinUsdc == []) and (ftx_open_orders != []) and (six_bid_sizes_summed >= remaining_size) and (
                three_bid_sizes_summed <= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_sixth_highest_bid_price, remaining_size)
                print('#3')
            except Exception:
                print('Exception passed #3')
                pass
        else:
            pass

        # 4
        if ((myOrders_KinUsdc != []) and (ftx_open_orders != []) and (six_bid_sizes_summed >= remaining_size) and (
                three_bid_sizes_summed <= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_sixth_highest_bid_price, remaining_size)
                print('#4')
            except Exception:
                print('Exception passed #4')
                pass
        else:
            pass

        # 5
        if ((myOrders_KinUsdc == []) and (ftx_open_orders != []) and (eleven_bid_sizes_summed >= remaining_size) and (
                six_bid_sizes_summed <= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_eleventh_highest_bid_price, remaining_size)
                print('#5')
            except Exception:
                print('Exception passed #5')
                pass
        else:
            pass

        # 6
        if ((myOrders_KinUsdc != []) and (ftx_open_orders != []) and (eleven_bid_sizes_summed >= remaining_size) and (
                six_bid_sizes_summed <= remaining_size) and (
                kin_short_size_forUsdc * 0.9 >= kin_position_size_ftx or remaining_size >= kin_short_size_forUsdc * 0.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                time.sleep(2)
                client.place_order('KIN-PERP', 'sell', ftx_perp_eleventh_highest_bid_price, remaining_size)
                print('#6')
            except Exception:
                print('Exception passed #6')
                pass
        else:
            pass

        # 7
        if ((myOrders_KinUsdc != []) and (ftx_open_orders != []) and (
                kin_short_size_forUsdc * 0.1 >= remaining_size) and (
                kin_short_size_forUsdc * 0.9 <= kin_position_size_ftx <= kin_short_size_forUsdc * 1.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                for order in myOrders_KinUsdc:
                    marketKinUsdc.cancel_order(
                        owner=account,
                        order=order,
                        opts=TxOpts()
                    )
                    print('Closed Orders #7')
                print('#7')
                time.sleep(100)

            except Exception:
                print('Exception passed #7')
                pass
        else:
            pass
        # 8
        if ((myOrders_KinUsdc == []) and (ftx_open_orders != []) and (
                kin_short_size_forUsdc * 0.1 >= remaining_size) and (
                kin_short_size_forUsdc * 0.9 <= kin_position_size_ftx <= kin_short_size_forUsdc * 1.1) and (
                kin_position_size_ftx >= kin_position_allowance)):
            try:
                client.cancel_orders('KIN-PERP')
                print('#8')
                time.sleep(2)

            except Exception:
                print('Exception passed #8')
                pass
        else:
            pass

        # 9
        if ((myOrders_KinUsdc != []) and (ftx_open_orders == []) and (
                kin_short_size_forUsdc * 0.9 <= kin_position_size_ftx <= kin_short_size_forUsdc * 1.1 or ftx_perp_highest_bid_price <= KinUsdc_my_order_price * 1.01)):
            try:
                for order in myOrders_KinUsdc:
                    marketKinUsdc.cancel_order(
                        owner=account,
                        order=order,
                        opts=TxOpts()
                    )
                    print('Closed Orders #9')
                print('#9')
                time.sleep(100)

            except Exception:
                print('Exception passed #9')
                pass
        else:
            pass

        # 10
        if ftx_perp_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and serum_usdc_lowest_ask_size >= order_size and eleven_bid_sizes_summed >= order_size and ftx_perp_eleventh_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and six_bid_sizes_summed <= order_size and myOrders_KinUsdc == [] and ftx_open_orders == [] and free_usd_balance >= usd_value_KinUsdc and free_usd_balance >= max_usd_value_KinUsdc:
            for order in myOrders_KinUsdc:
                if ((order[5][0] >= ftx_perp_highest_bid_price * 0.98 and myOrders_KinUsdc != []) or (
                        order[5][0] != serum_usdc_lowest_ask_price) or (all_prices_KinUsdc == False)):
                    try:
                        marketKinUsdc.cancel_order(
                            owner=account,
                            order=order,
                            opts=TxOpts()
                        )
                        print('Closed Orders #10')
                        time.sleep(100)
                    except Exception:
                        pass
                        print('Error Passed #10')
                        time.sleep(100)
                else:
                    pass
            if serum_usdc_lowest_ask_price != KinUsdc_my_order_price:
                try:
                    order = marketKinUsdc.place_order(
                        payer=PublicKey(usdcPubKey),
                        owner=account,
                        side=Side.BUY,
                        order_type=OrderType.LIMIT,
                        limit_price=serum_usdc_lowest_ask_price,
                        max_quantity=order_size,
                        opts=TxOpts()
                    )
                    print('Bought the cheapest coins #10')
                    time.sleep(100)

                    myOrders_KinUsdc = marketKinUsdc.load_orders_for_owner(
                        owner_address=PublicKey(solletPubKey)
                    )


                    def serum_openOrderSizes_KinUsdc():
                        for sizes in myOrders_KinUsdc:
                            osc_data = sizes[5][1]
                            serum_open_order_sizes_KinUsdc.append(osc_data)


                    serum_open_order_sizes_KinUsdc = []
                    serum_openOrderSizes_KinUsdc()

                    if serum_open_order_sizes_KinUsdc == []:
                        KinUsdc_my_order_size = 0
                    else:
                        KinUsdc_my_order_size = serum_open_order_sizes_KinUsdc[0]

                    kin_short_size_forUsdc = order_size - KinUsdc_my_order_size
                    client.place_order('KIN-PERP', 'sell', ftx_perp_eleventh_highest_bid_price, kin_short_size_forUsdc)
                    print('Shorted the best we can on ftx #10')


                except Exception:
                    pass
                    print('Exception passed #10')
                    time.sleep(2)
        else:
            pass
        # 11
        if ftx_perp_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and serum_usdc_lowest_ask_size >= order_size and six_bid_sizes_summed >= order_size and ftx_perp_sixth_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and three_bid_sizes_summed <= order_size and myOrders_KinUsdc == [] and ftx_open_orders == [] and free_usd_balance >= usd_value_KinUsdc and free_usd_balance >= max_usd_value_KinUsdc:
            for order in myOrders_KinUsdc:
                if ((order[5][0] >= ftx_perp_highest_bid_price * 0.98 and myOrders_KinUsdc != []) or (
                        order[5][0] != serum_usdc_lowest_ask_price) or (all_prices_KinUsdc == False)):
                    try:
                        marketKinUsdc.cancel_order(
                            owner=account,
                            order=order,
                            opts=TxOpts()
                        )
                        print('Closed Orders #11')
                        time.sleep(100)
                    except Exception:
                        pass
                        print('Error Passed #11')
                        time.sleep(100)
                else:
                    pass

            if serum_usdc_lowest_ask_price != KinUsdc_my_order_price:
                try:
                    order = marketKinUsdc.place_order(
                        payer=PublicKey(usdcPubKey),
                        owner=account,
                        side=Side.BUY,
                        order_type=OrderType.LIMIT,
                        limit_price=serum_usdc_lowest_ask_price,
                        max_quantity=order_size,
                        opts=TxOpts()
                    )
                    print('Bought the cheapest coins #11')
                    time.sleep(100)

                    myOrders_KinUsdc = marketKinUsdc.load_orders_for_owner(
                        owner_address=PublicKey(solletPubKey)
                    )


                    def serum_openOrderSizes_KinUsdc():
                        for sizes in myOrders_KinUsdc:
                            osc_data = sizes[5][1]
                            serum_open_order_sizes_KinUsdc.append(osc_data)


                    serum_open_order_sizes_KinUsdc = []
                    serum_openOrderSizes_KinUsdc()

                    if serum_open_order_sizes_KinUsdc == []:
                        KinUsdc_my_order_size = 0
                    else:
                        KinUsdc_my_order_size = serum_open_order_sizes_KinUsdc[0]

                    kin_short_size_forUsdc = order_size - KinUsdc_my_order_size
                    client.place_order('KIN-PERP', 'sell', ftx_perp_sixth_highest_bid_price, kin_short_size_forUsdc)
                    print('Shorted the best we can on ftx #11')


                except Exception:
                    pass
                    print('Exception passed #11')
                    time.sleep(2)

        else:
            pass
        # 12
        if ftx_perp_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and serum_usdc_lowest_ask_size >= order_size and three_bid_sizes_summed >= order_size and ftx_perp_third_highest_bid_price >= serum_usdc_lowest_ask_price * 1.02 and myOrders_KinUsdc == [] and ftx_open_orders == [] and free_usd_balance >= usd_value_KinUsdc and free_usd_balance >= max_usd_value_KinUsdc:
            for order in myOrders_KinUsdc:
                if ((order[5][0] >= ftx_perp_highest_bid_price * 0.98 and myOrders_KinUsdc != []) or (
                        order[5][0] != serum_usdc_lowest_ask_price) or (all_prices_KinUsdc == False)):
                    try:
                        marketKinUsdc.cancel_order(
                            owner=account,
                            order=order,
                            opts=TxOpts()
                        )
                        print('Closed Orders #12')
                        time.sleep(100)
                    except Exception:
                        pass
                        print('Error Passed #12')
                        time.sleep(100)
                else:
                    pass

            if serum_usdc_lowest_ask_price != KinUsdc_my_order_price:
                try:
                    order = marketKinUsdc.place_order(
                        payer=PublicKey(usdcPubKey),
                        owner=account,
                        side=Side.BUY,
                        order_type=OrderType.LIMIT,
                        limit_price=serum_usdc_lowest_ask_price,
                        max_quantity=order_size,
                        opts=TxOpts()
                    )
                    print('Bought the cheapest coins and routed third highest bid #12')
                    time.sleep(100)

                    myOrders_KinUsdc = marketKinUsdc.load_orders_for_owner(
                        owner_address=PublicKey(solletPubKey)
                    )


                    def serum_openOrderSizes_KinUsdc():
                        for sizes in myOrders_KinUsdc:
                            osc_data = sizes[5][1]
                            serum_open_order_sizes_KinUsdc.append(osc_data)


                    serum_open_order_sizes_KinUsdc = []
                    serum_openOrderSizes_KinUsdc()

                    if serum_open_order_sizes_KinUsdc == []:
                        KinUsdc_my_order_size = 0
                    else:
                        KinUsdc_my_order_size = serum_open_order_sizes_KinUsdc[0]

                    kin_short_size_forUsdc = order_size - KinUsdc_my_order_size

                    client.place_order('KIN-PERP', 'sell', ftx_perp_third_highest_bid_price, kin_short_size_forUsdc)
                    print('Shorted the best we can on ftx #12')
                    time.sleep(2)



                except Exception:
                    pass
                    print('Exception passed #12')
                    time.sleep(2)


        else:
            print('NONONO')
            pass




    except Exception:
        print('Error passed')
        time.sleep(5)
        pass