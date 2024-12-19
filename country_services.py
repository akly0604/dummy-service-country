import requests
import os

# World Bank API endpoint from environment variable
world_bank_api_url = os.getenv("WORLD_BANK_API_URL", "http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={year}&format=json")

# REST Countries API endpoint from environment variable
rest_countries_api_url = os.getenv("REST_COUNTRIES_API_URL", "https://restcountries.com/v3.1/name/{country_name}?fullText=true")

def get_world_bank_data(country_code, indicator, year):
    url = world_bank_api_url.format(country_code=country_code, indicator=indicator, year=year)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch World Bank data: {response.status_code}")

def get_rest_countries_data(country_name):
    url = rest_countries_api_url.format(country_name=country_name)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch REST Countries data: {response.status_code}")

# No main function here; Choreo manages inputs and execution flow.
