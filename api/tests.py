from django.test import TestCase
import requests

# Create your tests here.
url = 'http://127.0.0.1:8000/api/food/'
data = {'image':1}

h = requests.post(url,json=data)
print(h.text)