import requests

url = 'http://localhost:5000/predict'
r = requests.post(url, json={'area': 3000, 'bedroom': 2, 'age': 15,'bathrooms':2,
'basement':0,'stories':1,'parking':0,'areaperbedroom':1500,'guestroom':0,'bbratio':0.89})


print(r.json())
