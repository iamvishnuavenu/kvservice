import argparse
from time import sleep
import requests
import os


API_ENDPOINT= "http://127.0.0.1:5000/api/vi/resource/kv/"
JSON_HEADER={ 'Content-Type': 'application/json'}
PERMITTED_ACTIONS = ['set', 'get', 'watch']


parser = argparse.ArgumentParser()
parser.add_argument("action", nargs="+")
args = parser.parse_args()


def prepQueryParams(params):
    c = map(lambda x: "key="+x, params['key'])
    return '&'.join(c)        

def cmd_processor(args):
    if args[0] not in PERMITTED_ACTIONS:
        print("Error: Invalid action. Choose set or get")
    
    if args[0] == 'get':
        params = { 'key' : args[1:] }
        url = API_ENDPOINT+'?'+prepQueryParams(params)
        result = requests.get(url, headers=JSON_HEADER)
        print(result.text)
        return

    elif args[0] == 'set':
        print(args[1:])
        param = {}
        for keyval in args[1:]:
            if "=" not in keyval:
                print("Error: Invalid parameter. use params key1=val1 key2=val2")
                return 
            
            key, val = keyval.split("=")
            param[key] = val
            # print(param)
            result = requests.post(API_ENDPOINT, headers=JSON_HEADER, params=param)
            print(result.text)
            return

    elif args[0] == 'watch':
        while( True ):
            os.system("clear")
            print("Watching KV Store");
            result = requests.get(API_ENDPOINT, headers=JSON_HEADER)
            print(result.text)
            sleep(2)            



if __name__ == "__main__":
    cmd_processor(args.action)