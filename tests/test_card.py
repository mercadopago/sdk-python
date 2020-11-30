import sys
sys.path.append('../')

from mercadopago import SDK
import unittest

class TestCard(unittest.TestCase):
    sdk = SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_all(self):
        self.assertEqual(self.sdk.card().find_all("67243")["status"], 404)

if __name__ == '__main__':
    unittest.main()


#print(sdk.card().find_all("67243"))

#print(sdk.card().find_by_id("67243", "456"))

#print(sdk.card().create("67243", {}))

#print(sdk.card().update("67243", "456", {}))

#print(sdk.card().delete("67243", "456"))
