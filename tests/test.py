headers = {'Authorization': 'Bearer ' + "self.__access_token",
                'x-product-id': "self.__config.productId"}

__corporation_id = None 
__integrator_id = 2
__platform_id = 3

headers["corporation_id"] = __corporation_id
headers["integrator_id"] = __integrator_id
headers["platform_id"] = __platform_id

print(headers)