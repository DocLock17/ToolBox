#!/bin/bash/python3
## TestREST - A simple REST request interface for testing APIs.


# Try import and install inline if module import fails.
try:
  import requests
except ModuleNotFoundError:
  !pip install requests
except Exception as e:
  print(e)


# Set API endpoint and query and response fields
api_endpoint = 'http://35.188.177.166:5000'
query_field = 'input'
response_field = 'body'


# Set a count variable for bug tracking.
count = 1


# Send REST input based requests in an infinite loop print response and increment count variable for tracking.
while(True):
  query = {query_field:input("Enter input to query field: {0} \nFor request to: {1} \n".format(query_field, api_endpoint))}
  response = requests.put(api_endpoint, params=query)
  print('\n ',count,"  ", response.json()[response_field], '\n')
  count+=1
