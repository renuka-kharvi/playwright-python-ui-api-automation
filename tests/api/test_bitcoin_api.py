from api.bitcoin_api import BitcoinAPI
from playwright.sync_api import APIRequestContext
import pytest
from utils.data_reader import read_json_data
from utils.logger import get_logger

logger=get_logger(__name__)


@pytest.mark.api
class TestBitcoinAPI:
    def test_get_bitcoin(self,request_context):
        """ 
        1.	Send the GET request
        2.	Verify the response contains  
        3.	The price in USD, GBP, and EUR

        """

        logger.info("Start get bitcoin api test")
        bitcoin_api=BitcoinAPI(request_context)

        #send get request

        response=bitcoin_api.get_bitcoin("/api/v3/coins/bitcoin")
        logger.info(f'{response.status}')
        response_body=response.json()
    
        # get actual value for validate 
        
        current_price=response_body["market_data"]["current_price"]
        market_cap=response_body["market_data"]["market_cap"]
        total_volume=response_body["market_data"]["total_volume"]
        price_change_percentage_24h=response_body["market_data"]["price_change_percentage_24h"]
        homepage=response_body["links"]["homepage"]
        logger.info(f'{current_price}')
        logger.info(f'{market_cap}')
        logger.info(f'{total_volume}')
        logger.info(f'{homepage}')

        print(price_change_percentage_24h)

        # read data from json file
        data=read_json_data("testdata/api_data/bitcoin.json")
        print(data)
        currency_data=data["bitcoin"]["currencies"]
        
        assert response.status==data["bitcoin"]["expected_status_code"],\
              f"Expected status {data['bitcoin']['expected_status_code']}, " \
              f"but received {response.status}"
        for currency in currency_data:
            assert( currency in current_price 
                   and current_price[currency] is not None  
                    and  current_price[currency]>0
                    and isinstance(current_price[currency], (int, float))), (
                    f"Invalid current price for {currency}: "f"{current_price.get(currency)}")
            
            assert (currency in market_cap 
                    and market_cap[currency] is not None  
                    and  market_cap[currency]>0 
                    and isinstance(market_cap[currency], (int, float))),(
                    f"Invalid market cap for {currency}: "f"{market_cap.get(currency)}")
            
            assert( currency in total_volume
                   and total_volume[currency] is not None  
                   and  total_volume[currency]>0 
                   and isinstance(total_volume[currency], (int, float))), (
                   f'{total_volume[currency]} is not present in total_volume or total_volume price  may be 0')

        assert (price_change_percentage_24h is not None
               and isinstance(price_change_percentage_24h, (int, float))
               and -100 <= price_change_percentage_24h <= 100),\
               f"Invalid 24h price change: {price_change_percentage_24h}"    
            
        assert (homepage and homepage[0].strip() != ""), (
        f"Homepage is blank: {homepage}")
        
        logger.info("end get bitcoin api test")
        
        






