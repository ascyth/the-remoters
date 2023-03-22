# https://open-platform.theguardian.com/documentation/search

# endpoint: https://content.guardianapis.com/search

import requests
import json
import pandas as pd
import re
from unidecode import unidecode
import datetime

# Set the API endpoint and parameters
endpoint = 'https://content.guardianapis.com/search'
params = {
    'q': 'remote work',  # search query
    'page-size': 100,  # number of results per page
    'api-key': '7067aedc-f50c-430e-8971-acba247ab46a',  # replace with your API key
    'show-fields': 'body'
}

# Initialize the list to store the results
results = []

# Loop through 10 pages (total of 1000 results)
for page in range(1, 11):
    # Add the current page parameter to the API request
    params['page'] = page

    # Call the API and get the response data
    response = requests.get(endpoint, params=params)
    data = json.loads(response.text)

    # Extract the relevant fields from each article and append them to the results list
    for article in data['response']['results']:
        results.append({
            'ID': article['id'],
            'URL': article['webUrl'],
            'DATE': article['webPublicationDate'],
            'PLAIN_TEXT': article['fields']['body'],
            'SOURCE': "The Guardian"
        })

# Save the results to a JSON file
with open('guardian_articles.json', 'w') as outfile:
    json.dump(results, outfile)

df = pd.read_json('guardian_articles.json')

df.info()
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(lambda x: re.sub('\n', '', x))
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(lambda x: re.sub('<.*?>', '', x))
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(lambda x: unidecode(str(x)))
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(lambda x: re.sub(" +", " ", x))
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].str.replace('/', '', regex = False)
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(lambda x: x.replace('\'', ''))

def replace_unicode_escapes(text):
    return re.sub(r'\\u[0-9a-fA-F]{4}', lambda m: chr(int(m.group(0)[2:], 16)), text)

def remove_quotes_and_backslashes(text):
    return text.replace('\\', '').replace('"', '').replace("'", '')

df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(replace_unicode_escapes)
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].apply(remove_quotes_and_backslashes)
df['PLAIN_TEXT'] = df['PLAIN_TEXT'].str.replace('\\', '', regex = False)

df['DATE'] = pd.to_datetime(df['DATE'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')

df.to_json('guardian_articles.json', orient='records')
