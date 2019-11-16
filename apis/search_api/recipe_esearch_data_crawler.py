import http.client, urllib.request, urllib.parse, urllib.error, base64
import pandas as pd
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({
})

body = {
    "query": "*"
}

json_data = json.dumps(body)

try:
    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    conn.request("POST", "/v1/search/recipes?%s" % params, "%s" %json_data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

    df = pd.json(data, orient='index')
    print(df.head())
except Exception as e:
    print("ahhhh")