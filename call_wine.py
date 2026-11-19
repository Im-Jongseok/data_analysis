import requests

URL = "http://127.0.0.1:5002/api/wine/predict"
wine = {"alcohol": 13.74, "malic_acid": 1.67, "ash": 2.25, "alcalinity_of_ash": 16.4,
        "magnesium": 118.0, "total_phenols": 2.6, "flavanoids": 2.9,
        "nonflavanoid_phenols": 0.21, "proanthocyanins": 1.62, "color_intensity": 5.85,
        "hue": 0.92, "od280/od315_of_diluted_wines": 3.2, "proline": 1060.0}
r = requests.post(URL, json=wine)
print(r.status_code, r.json())

wine["flavanoids"] = 0.5
r = requests.post(URL, json=wine)
print(r.status_code, r.json())

r = requests.post(URL, json={"alcohol": 13.0})
print(r.status_code, r.json()["message"])
