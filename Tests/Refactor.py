import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class Email:
    def __init__(self, login, passwd, subject, recipients, message, header=None):
        self.login = login
        self.passwd = passwd
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        server = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()
        server.login(self.login, self.passwd)
        server.sendmail(self.login, self.recipients, msg.as_string())
        server.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.passwd)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    my_login = 'login'
    my_passwd = 'password'
    my_subject = 'Subject'
    my_recipients = ['email_1', 'email_2']
    my_message = 'Message'

    my_male = Email(my_login, my_passwd, my_subject, my_recipients, my_message)
    my_male.send_message()
    print(my_male.receive_message())
