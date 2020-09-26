#! python3
import bs4, requests, smtplib

# ------------------- E-mail list ------------------------
toAddress = ['ehomnici@gmail.com','mattcastillo2010@gmail.com']
# --------------------------------------------------------

#Download page
getPage = requests.get('https://sodastream.com/products/exchange-cylinder')
getPage.raise_for_status() #if error it will stop the program

#Parse text for foods
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
foods = menu.select('.btn-add')

the_one = 'out of stock' # This is the name of the food you are looking for
flength = len(the_one)
available = False

for food in foods:
    for i in range(len(food.text)):
        chunk = food.text[i:i+flength].lower()
        if chunk == the_one:
            available = False

if available == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('mattcastillo2010@gmail.com', 'xghumulesnhngkyf')
    conn.sendmail('mattcastillo2010@gmail.com', toAddress, 'Subject: SodaStream Alert!\n\nAttention!\n\nIN STOCK NOW.\n\n')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('SodaStream is not available.')