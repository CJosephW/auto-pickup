# auto-pickup
 auto pickup and notify for hotschedules.com

# Clone Repo:
`git clone https://github.com/CJosephW/auto-pickup`

# dependencies:
-Selenium

# Using Selenium:
- Choose desired webdriver and add to PATH(In this case I use Mozilla's geckodriver.)
- [geckodriver](https://github.com/mozilla/geckodriver/releases)

# How to send SMS messages to yourself
```python
import smtplib

carriers = {
    'att': '@mms.att.net',
}

def send(text):
    my_number = '0000000000@mms.att.net'
    auth = ('email', 'pass')

    server = smtplib.SMTP( "smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], my_number, text)
```
In this example I use at&t's mobile gateway address
[Here](https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses) is a link for other carrier's gateway addresses
