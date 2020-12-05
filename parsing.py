import requests
from bs4 import BeautifulSoup

def parse():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    d = {"sell_dollar":0, "buy_dollar":0, "sell_euro":0, "buy_euro":0}

    def parse_block(item):
        value = item.select('div.table-flex__rate.font-size-large.color-pumpkin-orange')
        if value != []:
            name = item.find_all("a", {"class":"font-bold" })[0].text
            name1 = item.find_all("div", {"class": "font-size-small"})[0].text
            for i in value:
                usd_eur = i.get('data-currencies-code')
                val = i.get('data-currencies-rate-buy')
                if val != None:
                    if usd_eur == 'USD':
                        d['sell_dollar'] = [val, name,name1.replace("\t", "").replace("\n", "")]
                    else :
                        d["sell_euro"] = [val, name,name1.replace("\t", "").replace("\n", "")]
            for i in value:
                usd_eur = i.get('data-currencies-code')
                val = i.get('data-currencies-rate-sell')
                if val != None:
                    if usd_eur == 'USD':
                        d['buy_dollar'] = [val, name,name1.replace("\t", "").replace("\n", "")]
                    else :
                        d["buy_euro"] = [val, name,name1.replace("\t", "").replace("\n", "")]

    Exchange = 'https://www.banki.ru/products/currency/cash/sankt-peterburg/'

    full_page = requests.get(Exchange, headers=headers )
    soup = BeautifulSoup(full_page.content, 'html.parser')
    container = soup.select('div.table-flex__row.item.calculator-hover-icon__container')
    for item in container:
        block = parse_block(item)

    return d

# print('Better to buy dollar in "' + d['buy_dollar'][1] + '"; exchange rate: ' + d['buy_dollar'][0] )
# print('Better to sell dollar in "' + d['sell_dollar'][1] + '"; exchange rate: ' + d['sell_dollar'][0] )
# print()
# print('Better to buy euro in "' + d['buy_euro'][1] + '"; exchange rate: ' + d['buy_euro'][0] )
# print('Better to sell euro in "' + d['sell_euro'][1] + '"; exchange rate: ' + d['sell_euro'][0] )

