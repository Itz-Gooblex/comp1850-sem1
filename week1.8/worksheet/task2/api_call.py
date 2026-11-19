
import httpx

base_url = "https://dummyjson.com/"

content = "product/"

query = "search?q=Apple"

url = base_url + content + query  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(len(content))
