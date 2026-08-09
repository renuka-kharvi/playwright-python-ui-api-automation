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
        homepage=response_body["links"]["homepage"]
        logger.info(f'{current_price}')
        logger.info(f'{market_cap}')
        logger.info(f'{total_volume}')
        logger.info(f'{homepage}')

        # read data from json file
        data=read_json_data("testdata/api_data/bitcoin.json")
        print(data)
        currency_data=data["bitcoin"]["currencies"]
        
        assert response.status==data["bitcoin"]["expected_status_code"]
        for currency in currency_data:
            assert current_price[currency] is not None  and  current_price[currency]>0 and isinstance(current_price[currency], (int, float)), f'{current_price[currency]} is not present in current_price or price may be 0'
            assert market_cap[currency] is not None  and  market_cap[currency]>0 and isinstance(market_cap[currency], (int, float)), f'{market_cap[currency]} is not present in market_cap or market_cap price  may be 0'
            assert total_volume[currency] is not None  and  total_volume[currency]>0 and isinstance(total_volume[currency], (int, float)), f'{total_volume[currency]} is not present in total_volume or total_volume price  may be 0'


        assert homepage is not [] and homepage[0]!="", f'homepage: {homepage} is blank'
        logger.info("end get bitcoin api test")
        
        






