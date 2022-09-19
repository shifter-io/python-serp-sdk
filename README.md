# Shifter’s SERP Python SDK

Shifter [SERP](https://shifter.io/services/serp-scraping) is an API that allows scraping various search engines such as Google, Bing, Yandex, etc. while using rotating proxies to prevent bans. This SDK for Python makes the usage of the API easier to implement in any project you have.
## Installation

Run the following command in the main folder of your project:

```
pip install serp
```

## API Key

To use the API and the SDK you will need an API Key. You can get one by registering at [Shifter.io](https://shifter.io)

## Classes
This SDK provides a class for each search engine from shifter.io. Here is the list:

| Class                           | Usage                            |
|---------------------------------|----------------------------------|
| SerpGoogleSearch          | google searches                  |
| SerpBingSearch            | bing searches                    |
| SerpYandexSearch          | yandex searches                  |
| SerpGoogleAutocomplete    | google autocomplete searches     |
| SerpGoogleEvents          | google events searches           |
| SerpGoogleJobs            | google jobs searches             |
| SerpGoogleJobsListing     | google jobs listing searches     |
| SerpGoogleMaps            | google maps searches             |
| SerpGoogleMapsReviews     | google maps reviews searches     |
| SerpGoogleProduct         | google product searches          |
| SerpGoogleReverseImage    | google reverse image searches    |
| SerpGoogleScholar         | google scholar searches          |
| SerpGoogleScholarAuthor   | google scholar author searches   |
| SerpGoogleScholarCite     | google scholar cite searches     |
| SerpGoogleScholarProfiles | google scholar profiles searches |
| SerpLocations             | locations api                    |

## Usage

Using the SDK it's quite easy. An example of a GET call to the API is the following:

```
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
```

Alternatively, you can use the function executeRaw, which will allow you to send the parameters in an associative array:

```
from serp import SerpLocations, SerpGoogleSearch

serpGoogleSearch = SerpGoogleSearch('YOUR_API_KEY')
locationsAPI = SerpLocations()

response = locationsAPI.execute("Austin", 1)
locations = response.json()
location = locationsAPI.process_location(locations[0])
response = serpGoogleSearch.executeRaw({
    'q': 'test',
    'device': 'mobile',
    'lr': 'lang_en|lang_ar',
    'location': location
})

# print(response.status_code)
# print(response.headers);
print(response.json());
```

For a better understanding of the parameters, please check out [our documentation](https://developers.shifter.io/).
