import requests
payload = {'q': 'hot girls'}
r = requests.get('https://www.google.com.vn/search?q=', params=payload)
str1 = r.text
str2 = "https://www.youtube.com/"
print (len(r.text))
