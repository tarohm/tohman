import requests
from bs4 import BeautifulSoup as bs

url = 'https://factomos.com'
email = 'myemail'
password = 'mypassword'
#url_login = 'https://factomos.com/connexion'
url_login = 'https://app.factomos.com/controllers/app-pro/login-ajax.php'
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
})

data_login = {
    'appAction': 'login',
    'email': email,
    'password': password
}

with requests.Session() as s:
    dash = s.post(url_login, headers=headers, data=data_login)
    print("Tara")
    print(dash.status_code)


# MechanicalSoup
import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
resp = browser.open("https://app.factomos.com/connexion")
##resp = browser.open("https://app.factomos.com/controllers/app-pro/login-ajax.php")
browser.select_form('form[id="login-form"]')
browser["email"] = 'myemail'
browser["password"] = 'mypassword'
response = browser.submit_selected()
print("submite: ", response.status_code)
print(browser.get_current_page())


####

r = requests.get('https://reqbin.com/echo/get/json',
                 headers={'Accept': 'application/json'})

print(f"Response: {r.json()}")
