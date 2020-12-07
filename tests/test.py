headers = {'Authorization': 'Bearer ' + "self.__access_token",
                'x-product-id': "self.__config.productId"}

__corporation_id = 1 #None

headers["corporation_id"] = __corporation_id

print(headers)