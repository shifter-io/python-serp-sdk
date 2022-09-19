from serp import SerpLocations, SerpGoogleSearch

serpGoogleSearch = SerpGoogleSearch('YOUR_API_KEY')
locationsAPI = SerpLocations()

response = locationsAPI.execute("Austin", 1)
locations = response.json()
location = locationsAPI.process_location(locations[0])
serpGoogleSearch.set_q("Test")
serpGoogleSearch.set_location(location)
serpGoogleSearch.set_lr('lang_en|lang_ar')
response = serpGoogleSearch.execute()

# print(response.status_code)
# print(response.headers);
print(response.json());