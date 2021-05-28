import requests
import sys

vermelho = '\033[31m'
verde = '\033[32m'

argv = sys.argv

lista = argv[2]

lt = open(lista, 'r')

'''
argv1 url, argv2 lista para o crawler
'''

a = str(argv[1])

for i in lt:
    url = a + '/' + i
    r = requests.get(url)

    if r.status_code == 404:
        print(vermelho + url, 'Not Found')

    elif r.status_code == 200:
        print(verde + url, 'Found')

    elif r.status_code == 403:
        print(vermelho + url, 'Forbidden' )

    elif r.status_code == 301:
        print(vermelho + url, 'Moved Permanently')