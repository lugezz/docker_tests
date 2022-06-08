import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from utils import get_domain, get_html, load_ats_domains
import re
import hashlib


def scrap_urls(urls, idx):
    ats_companies = set(load_ats_domains())
    try:
        texto_pagina = get_html(f'pagina-{idx}-{len(urls)}.html', urls[-1])
    except Exception as e:
        results = ["Error: "+str(e)]
        return results
    soup = BeautifulSoup(texto_pagina, 'html.parser')
    links = soup.find_all('a', href=True)
    results = []
    for a in links:
        if (a['href'].startswith('http')
            and a['href'] not in results
            and get_domain(a['href']) in ats_companies):
                results.append(a['href'])
    return results


def normalize_str(name):
    return re.sub(f'[^a-zA-Z_]+', '', name.replace(' ','_')).strip('_')


def main():
    results = {}
    parsed_step2 = (json.load(open('step2.json')))
    
    idx = 0
    for comp, comp_dict in parsed_step2.items():
        #f'pagina-{normalize_str(comp)}-{idx}-{count}.html'
        #f'{hash_company(comp)}-{normalize_str(comp)}.html'
        #f'{hash_company(comp)}.html'
        idx += 1
        results[comp]=comp_dict
        results[comp]['match_url'] = scrap_urls(results[comp]['urls'], idx)

        print (idx)
        if idx > 10:
            break

    with open('step3.json', 'w') as f:
        f.write(json.dumps(results, indent=1))

def hash_company(company):
    return hashlib.sha256(company.encode('utf8')).hexdigest()

if __name__ == '__main__':
#     print(hashlib.sha256('Blas asdaslk asdl %3$%$#'.encode('utf8')).hexdigest())
#     print(normalize_str())
    main()
