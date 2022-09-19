from unittest import mock

import pytest

from serp import SerpLocations, SerpGoogleSearch

@pytest.fixture(scope='module')
def googleSearch():
    return SerpGoogleSearch(api_key='API_KEY')


@pytest.fixture(scope='module')
def locations():
    return SerpLocations()


@mock.patch('serp.SerpLocations.request')
def test_locations(mock_request, locations):
    '''It should make a GET request with the locations api url and API key'''
    locations.execute("test", 10)

    mock_request.assert_called_with({'q': 'test', 'limit': 10})
    

@mock.patch('serp.SerpGoogleSearch.request')
def test_get(mock_request, googleSearch):
    '''It should make a GET request with the url and API key'''
    googleSearch.execute()

    mock_request.assert_called_with({})


@mock.patch('serp.SerpGoogleSearch.request')
def test_get_with_params(mock_request, googleSearch):
    '''It should add parameters to the url'''
    googleSearch.set_q("test")
    googleSearch.execute()

    mock_request.assert_called_with({'q': 'test'})