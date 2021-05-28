import requests
import sys

argv = sys.argv

lista = argv[2]

lt = open(lista, 'r')

'''
argv1 url, argv2 lista para o crawler
'''
print('Testando...')

a = str(argv[1])

for i in lt:
    url = a + '/' + i
    r = requests.get(url)

    if r.status_code == 200:
        print(url)