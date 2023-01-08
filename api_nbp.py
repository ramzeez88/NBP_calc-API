
import requests
from os import system

url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
table = requests.get(url)
response = table.json()


def header():
    system('clear')
    print('*' *26)
    print('***  kalkulator walut  ***')
    print('*' *26, '\n')

header()
print(' Sprawdź symbol waluty której kurs chcesz przeliczyć \n')

COUNTER = 1
NEXT_10 = 10
currency_codes_list = []

for rate in response[0]['rates']:
    currency = rate['currency']
    code  = rate['code']
    print(f'{COUNTER}. {currency} => {code}')
    currency_codes_list.append(code)
    if COUNTER == NEXT_10:    
        press_key = input('\nNaciśnij enter aby wyświetlić następne')
        NEXT_10 += 10
        header()
        print('\n')
    COUNTER += 1

while True:
    currency_code = input(' \npodaj symbol: ')
    if currency_code in currency_codes_list:
        break
    print('musisz podać właściwy symbol waluty')
    
date = response[0]['effectiveDate']

for rate in response[0]['rates']:
    if currency_code == rate['code']:
        code = rate['code']
        price_mid = float(rate['mid'])
        print(f'{code}, {price_mid} PLN z dnia: {date}')
        
print(f' \n jak chcesz przeliczyć? \n 1. PLN => {currency_code}') 
print(f' 2. {currency_code} => PLN ')  

while True:
    try:
        choice = int(input('Twój wybór: '))
    except:
        print('Musisz wybrać opcje <1> lub <2>')
    else:
        break

while True:
    if choice == 1:
        quote = float(input(f'Podaj kwote (PLN) do przeliczenia na ({currency_code}): '))
        result = quote / price_mid
        print(f'Po przeliczeniu: {result:.2f} {currency_code}')
        break
    if choice == 2:
        quote = float(input(f'Podaj kwote ({currency_code} do przeliczenia na (PLN) ): '))
        result = quote * price_mid
        print(f'Po przeliczeniu: {result:.2f} PLN')
        break


    

