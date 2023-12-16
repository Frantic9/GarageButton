import smtplib
import sys

def get_email_cred(email_cred_file):
    file = open(email_cred_file, 'r')
    email = file.readline()
    password = file.readline()
    file.close()
    return (email, password)

def get_message(message_file):
    file = open(message_file, 'r')
    message = file.read()
    file.close()
    return message

def get_recipients(recipients_file):
    file = open(recipients_file, 'r')
    file_lines = file.readlines()
    numbers = [line.strip() for line in file_lines]
    file.close()
    return numbers

def send_message(message_file, recipients_file, email_file):
    message = get_message(message_file)
    recipients = get_recipients(recipients_file)
    email_auth = get_email_cred(email_file)

    print(email_auth[0].strip() + ' ' + email_auth[1].strip())
    print(recipients)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_auth[0], email_auth[1])

    for number in recipients:
        server.sendmail(email_auth[0], number, message)
        
if __name__ == '__main__':
    message_file = sys.argv[1]
    recipients_file = sys.argv[2]
    email_file = sys.argv[3]

    send_message(message_file, recipients_file, email_file)


