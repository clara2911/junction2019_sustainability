import http.client, urllib.request, urllib.parse, urllib.error, base64
import pandas as pd
import json

data_path = ""

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

    df = pd.read_json(data)
    results = df.results.to_json()
    test = pd.read_json(results).T

    print(test.head())
    print(len(test))

    test.to_csv(data_path + "recipes.csv", index=False)
    print("Done")

except Exception as e:
    print("ahhhh")