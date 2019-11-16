import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import pandas as pd

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({

})

body = {"query": "*"
        }

json_data = json.dumps(body)

try:
    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    conn.request("POST", "/v1/search/products?%s" % params, "%s" % json_data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

    df = pd.read_json(data)
    print(len(df))
    results_df = df.results

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
