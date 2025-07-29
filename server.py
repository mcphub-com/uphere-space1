import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/uphere.space/api/uphere-space1'

mcp = FastMCP('uphere-space1')

@mcp.tool()
def orbit(period: Annotated[Union[int, float], Field(description='Orbital period (minutes) Default: 90')]) -> dict: 
    '''Orbital track for specified period'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/25544/orbit'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'period': period,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def launch_sites() -> dict: 
    '''Launch sites around the world'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/list/launch-sites'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location(units: Annotated[Literal['imperial', 'metric', None], Field(description='Units for height and speed values. Options are: imperial metric')] = None,
             lng: Annotated[Union[int, float, None], Field(description='Longitude to get satellite visibility Default: 122.374199')] = None,
             lat: Annotated[Union[int, float, None], Field(description='Latitude to get satellite visibility Default: 47.6484346')] = None) -> dict: 
    '''Current location by NORAD TLE number'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/20580/location'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'units': units,
        'lng': lng,
        'lat': lat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def popular_satellites(days: Annotated[Union[int, float], Field(description='Days to go back Default: 1')]) -> dict: 
    '''Most popular satellites going back x days'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/top'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'days': days,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def visible_satellites(lat: Annotated[str, Field(description='')],
                       lng: Annotated[str, Field(description='')]) -> dict: 
    '''Satellites visible from a specific latitude and longitude'''
    url = 'https://uphere-space1.p.rapidapi.com/user/visible'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lng': lng,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def details(number: Annotated[Union[int, float], Field(description='Norad TLE number Default: 43226')]) -> dict: 
    '''Details by Norad TLE number'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/43226/details'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def categories() -> dict: 
    '''Categories used to filter satellites'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/list/categories'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries() -> dict: 
    '''Countries who have launched satellites which have been or are in orbit.'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/list/countries'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def satellite_list(page: Annotated[Union[int, float], Field(description='Page of results (60 per page) Default: 1')],
                   text: Annotated[Union[str, None], Field(description='Search by text')] = None,
                   country: Annotated[Union[str, None], Field(description='Search by country')] = None) -> dict: 
    '''List of satellites in orbit'''
    url = 'https://uphere-space1.p.rapidapi.com/satellite/list'
    headers = {'x-rapidapi-host': 'uphere-space1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
        'text': text,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
