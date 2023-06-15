import requests
import os
import subprocess
import logging
from collections import defaultdict
from urllib.parse import urlparse
from pprint import pprint
#import pandas as pd

# def json_to_csv(json_file, output_csv):
#     pdObj = pd.read_json(json_file, orient='index')
#     pdObj.to_csv(output_csv, index=False)

def dict_to_csv(dict, output_csv):
    with open(output_csv, 'w') as f:
        for key in dict.keys():
            f.write("%s, %s\n" % (key, dict[key]))


def get_domains_from_list(urls):
    return [get_domain(url) for url in urls]

def get_domain(url):
    if url[0:5].lower() == 'error':
        return "Error"

    dom = urlparse(url).netloc
    dom = '.'.join(dom.split('.',-2)[-2:])
    return dom

def clean_urls(urls:list):
    resp = urls

    if isinstance(urls, list):
        resp = [clean_doubleclick(u) for u in urls]

    return resp

def clean_doubleclick(url):
    if url.startswith('https://ad.doubleclick.net/'):
        url = url.split('?', 1)[1]
    return url

def get_html(html_file, url):
    temp_folder = 'tmp'
    if not os.path.isdir(temp_folder):
        os.makedirs(temp_folder)


    if not os.path.exists(f'{temp_folder}/{html_file}'):
        print(f' - Descargando {url}')
            
        page = requests.get(
            url,
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'},
            timeout=10
        )
        
        with open(f'{temp_folder}/{html_file}', 'w', encoding='utf-8') as f:
            f.write(page.text)
    
    with open(f'{temp_folder}/{html_file}', 'r', encoding='utf-8') as f:
        texto_pagina = f.read()
    
    return texto_pagina

def exec_cmd(cmd):
    logging.debug('Running: %r' % cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.wait()
    out, err = p.communicate()
    logging.debug('out: %r\nerr:%r', out, err)
    return p, out, err


def solve_redirect(url):
    p, out, err = exec_cmd(f'curl -v {url}')
#     print(err)
    for l in err.decode('utf8').splitlines():
#         print(l)
        if l.startswith('< Location: '):
            return l[len('< Location: '):]


def load_ats_domains():
    with open('ats_domains.txt') as fp:
        domains = [d.strip().split(':')[0] for d in fp.readlines()
                if d.strip() 
                and not d.strip().startswith('#')]
    assert all(len(d.split('.')) == 2 for d in domains)
    return domains

