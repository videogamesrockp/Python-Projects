import requests
import json


if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    with open('test.json', 'w') as f:
        json.dump(response.json(), f, indent=4, separators=(", ", ": "), sort_keys=True, default=str)