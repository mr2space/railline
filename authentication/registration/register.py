from django.contrib.auth.forms import UsernameField
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
import random
import math
import hashlib



class registerFunctions():  
    def hashPassword(self, raw_password):
        passwd = str(raw_password)
        passwd = hashlib.sha256(passwd.encode())
        return passwd
    
    def otpGenerator(self):
        # variable to store digit use in Otp
        digits = '0123456789'
        otp = ''
        for i in range(5):
            otp += str(math.floor(random.random()*10))
        return otp
    
    def sendEmail(self):
        htmly = get_template('user/Email.html')
        d = { 'userName': self.userName, 'code':self.code}
        subject, from_email, to = 'welcome', 'mrspace.pro@gmail.com', self.email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content,"text/html")
        msg.send()
        return 1
    
    def resendOtp(self):
        self.code = self.otpGenerator()
        self.sendEmail()
        return 1

