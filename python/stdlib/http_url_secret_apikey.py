import http.client


host = "example.com"
conn = http.client.HTTPSConnection(host)
conn.request(
    "GET", "/path?apiKey=value&otherParam=123", headers={"Host": host}
)
response = conn.getresponse()
