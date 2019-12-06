import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    conn.request("POST", "/files/store_services?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))