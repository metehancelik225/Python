import requests

siteler = ['https://www.google.com']

for x in siteler:
    r = requests.get(x)
    if r.status_code == 200: #200 döndürüyorsa böyle bir url var demektir.
        print('Url Bulundu : {}'.format(x))
    elif r.status_code == 404: #404 döndürüyorsa böyle bir url yok demektir.
        print('Url Hatalı')

print("Hangi Site'ye Gitmek İstersiniz?\n")
import requests
siteler = ['https://www.google.com',
'https://www.youtube.com/']
for x in siteler:
  r = requests.get(x)
  if r.status_code == 200:
    print('Url Bulundu : {}'
    .format(x))
  elif r.status_code == 404:
    print('Url Hatalı')
