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