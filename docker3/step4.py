import json

def main():
    results = {}
    
    parsed_step3 = (json.load(open('step3.json')))
    
    for k, v in parsed_step3.items():
        if v["match_url"]: 
            results[k] = v['match_url']

    #print(results)
    with open('step4.json', 'w') as f:
        f.write(json.dumps(results, indent=1))

if __name__ == '__main__':
    main()