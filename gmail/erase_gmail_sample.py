try:
    import imaplib
    import argparse
    import email
    import webbrowser
except Exception as e:
    print e

def Connect_And_Login(uname, passwd, bedate):

    if uname.endswith('@gmail.com'):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        inbox = "INBOX"
        url = 'https://www.google.com/settings/security/lesssecureapps'

    elif uname.endswith('@yahoo.com'):
        mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
        inbox = "Inbox"
        url = 'https://login.yahoo.com/account/security#less-secure-apps'

    else:
        print 'Enter The Email Address Carefully'
        exit(0)

    try:
        mail.login(uname, passwd)

    except Exception as e:
        print "\n\nFailed to login Allow less secure apps from your email settings and try again\n\n"
        webbrowser.open(url)
        exit(0)

    Mark_emails_as_Deleted(mail, bedate, inbox)
    #print mail.list()
    return

def Mark_emails_as_Deleted(mail, bedate, inbox):
    mail.select(inbox)
    result, data = mail.search(None, '(BEFORE "'+str(bedate)+'")')

    if result == 'OK':
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')

            res, msg_data = mail.fetch(str(num), '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    print '\nDleting.....\n'
                    for header in [ 'subject', 'to', 'from' ]:
                        print '%-8s: %s' % (header.upper(), msg[header])

        expunge_Them(mail)

    return

def expunge_Them(mail):

    mail.expunge()
    mail.close()
    mail.logout()
    return

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("uname", help="Your email username like shantanu@gmail.com")
    parser.add_argument("path", help="Enter your email password")
    parser.add_argument("bedate", help="Enter Date, Before this date all emails will be cleaned WRITE LIKE 01-Jan-2016")
    args = parser.parse_args()
    #print '(BEFORE "'+str(bedate)+'")'

    Connect_And_Login(args.uname, args.path, args.bedate)

if __name__ == "__main__":
    main()