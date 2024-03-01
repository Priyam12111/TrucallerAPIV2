import asyncio
from truecallerpy import search_phonenumber
from truecallerpy import bulk_search

def NormalSearch(phone_number):
    country_code = "US"
    installation_id = "a1i03--lJA-YoFKkPpJkYKoe42mQpRdgh-w22OoFRX4KAAa22vubbc3zA7APDTwT"


    response = asyncio.run(search_phonenumber(phone_number, country_code, installation_id))
    name = (response['data']['data'][0]['name'])
    return name

def BulkSearch(phone_numbers):
    country_code = "US"
    installation_id = "a1i03--lJA-YoFKkPpJkYKoe42mQpRdgh-w22OoFRX4KAAa22vubbc3zA7APDTwT"

    response = asyncio.run(bulk_search(phone_numbers, country_code, installation_id))
    name = (response)
    return name

print(NormalSearch(9826076158))

# print(BulkSearch("9826076158,7566074639,9311866397"))