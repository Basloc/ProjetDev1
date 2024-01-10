import smtplib 
from email.mime.text import MIMEText

try :
    message = MIMEText('ceci est un meesage')
    message['From'] = 'bastienlocat@gmail.com'
    message['To'] = 'bastienlocat@gmail.com'
    message['Subject'] = ' a test email '
    
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login('bastienlocat@gmail.com', 'bhbl iddn plyk cfyr') # utiliser la cle generer en tant que mdp 
    mail_server.send_message(message)
    mail_server.quit()
    
    print("email send")
    
except Exception as e :
    print("email not send")
    print(e)