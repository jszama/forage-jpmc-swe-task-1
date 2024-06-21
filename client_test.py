import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      assert getDataPoint(quote) == (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      assert getDataPoint(quote) == (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  """ ------------ Add more unit tests ------------ """

def test_getRatio_normal(self):
  price_a = 117.2
  price_b = 121.68
  assert getRatio(price_a, price_b) == 0.9611567255735853

def test_getRatio_priceBZero(self):
  price_a = 100
  price_b = 0
  assert getRatio(price_a, price_b) == 0  
  
def test_getRatio_priceAZero(self):
  price_a = 0
  price_b = 50
  assert getRatio(price_a, price_b) == 0
  
def test_getRatio_priceAEqualPriceB(self):
  price_a = 50
  price_b = 50
  assert getRatio(price_a, price_b) == 1

if __name__ == '__main__':
    unittest.main()
