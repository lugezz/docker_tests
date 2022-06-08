import json

from utils import dict_to_csv, json_to_csv, get_domains_from_list

def main():
    parsed_json = (json.load(open('step3.json')))
    
    with open('final_results.csv', 'w') as f:
        for company, info in parsed_json.items():
            
            urls = set(get_domains_from_list(info['match_url']))

            f.write(f"{company.replace(',', '_')}, {' | '.join(urls)}\n")
            
if __name__ == '__main__':
    main()