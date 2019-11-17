import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import pandas as pd
import os

data_path = "YOUR_PATH"
data = pd.read_csv(os.path.join(data_path+ "Junction_data_sample.csv"), sep=";")

# because of a (suspected) API bug, the info of all products is not fetchable.
# Querying for specific values seems to check for the urlSlug,
# because of this we fetch info on any product which has its ean in the urlSlug as a hack-around the 100 limit.
# This leads to a drastic reduction in data we can obtain, but is good enough for now.

unique_ena = data.EAN.unique()

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'YOUR_KEY',
}

params = urllib.parse.urlencode({

})
all_eans = []
for ean in unique_ena:

    body = {"query": "%s"%ean}

    # body = {"filters": {
    #         "ean": unique_ena
    #     }}
    json_data = json.dumps(body)

    try:
        conn = http.client.HTTPSConnection('kesko.azure-api.net')
        conn.request("POST", "/v1/search/products?%s" % params, "%s" % json_data, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()

        df = pd.read_json(data)
        results = df.results.to_json()
        test = pd.read_json(results).T

        print(test.head())
        print(len(test))
        all_eans.append(test)

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

big_df = pd.concat(all_eans)
big_df.to_csv(data_path+"product_info.csv", index=False)
print(len(big_df))

print("Done")
