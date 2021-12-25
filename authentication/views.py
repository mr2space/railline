from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login #,auth,User
from django.contrib.auth.models import auth , User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from random import randint


#################### index#######################################
def index(request):
	return render(request, 'user/index.html', {'title': 'index'})

########### register here #####################################

class userRegistration():
	code = {"code":randint(100,99999)}
	def register(request,self=code):
		if request.method != 'POST':
			return render(request, 'user/registration.html')
		#first_name = request.POST['first_name']
		# last_name = request.POST['last_name']
		self['userName'] = request.POST['userName']
		self['password'] = request.POST.get('password')
		self['confirmPassword'] = request.POST.get('confirmPassword')
		self['email'] = request.POST['email']
		if self['password'] != self['confirmPassword']:
			return redirect("user/registration.html")
		htmly = get_template('user/Email.html')
		d = { 'userName': self['userName'], 'code':self['code']}
		subject, from_email, to = 'welcome', 'mrspace.pro@gmail.com', self['email']
		html_content = htmly.render(d)
		msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
		msg.attach_alternative(html_content,"text/html")
		msg.send()
		return render(request,"accounts/emailconfig.html")

	def verifyEmail(request, self=code):
		if request.method != 'POST':
			return render(request, 'user/emailconfig.html')
		user_code = request.POST.get('user_code')
		if user_code != self['code']:
			return render(request,'user/emailconfig.html')
		self.user.save()
		return redirect('registration')