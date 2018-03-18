# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.core.validators import RegexValidator
import hashlib
from django.core.validators import  *
from django.core.exceptions import ValidationError
import datetime
from .models import *
# Create your models here.

class Passenger(models.Model):
    # username = models.CharField(primary_key=True,max_length =50)
	email = models.EmailField(primary_key = True)
	password = models.CharField(max_length=100)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") #############look into regex
	phonenumber = models.CharField(validators=[phone_regex],max_length=15,blank = True)
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		assert password
		hashed = hashlib.md5(password).hexdigest()
		return self.password == hashed
	def set_password(self, password):
		self.password = password

class Airline(models.Model):
    # username = models.CharField(primary_key=True,max_length =50)
	email = models.EmailField(primary_key = True)
	password = models.CharField(max_length=100)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") #############look into regex
	phonenumber = models.CharField(validators=[phone_regex],max_length=15,blank = True)
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		assert password
		hashed = hashlib.md5(password).hexdigest()
		return self.password == hashed
	def set_password(self, password):
		self.password = password

class Airport(models.Model):
	airport_regex = RegexValidator(regex=r'^[1-9]\d{4,4}$', message="Flight id must be entered in the format: '100000'. A 5 digit number not starting with 0.")
	airport_id = models.CharField(validators=[airport_regex],primary_key = True,max_length=5)
	airport_name = models.CharField(max_length=20)
	airport_country = models.CharField(max_length=20)
	airport_city = models.CharField(max_length=20)
	airport_news  = models.CharField(max_length=1000)

class Flight(models.Model):
	flight_regex = RegexValidator(regex=r'^[1-9]\d{9,9}$', message="Flight id must be entered in the format: '1000000000'. A 10 digit number not starting with 0.")
	price_regex = RegexValidator(regex=r'^\d+(\.\d{1,2})?$', message="Valid Price must be entered in the format: '5000.05 or 5000'.")
	count_regex = RegexValidator(regex=r'^\d+$', message="Enter valid number of seats")
	time_regex = RegexValidator(regex=r'^[0-2][0-3]:[0-5][0-9]$', message="Enter valid time of format HH:MM 24hour")
	count1_regex = RegexValidator(regex=r'^\d$', message="Enter valid offset")
	flight_id = models.CharField(validators=[flight_regex],primary_key = True,max_length=10)
	business_classfare = models.CharField(validators=[price_regex],max_length=15)
	economy_classfare = models.CharField(validators=[price_regex],max_length=15)
	total_seats = models.CharField(validators=[count_regex],max_length=4)
	airline_email = models.ForeignKey(Airline,on_delete=models.CASCADE)
	daysoffset = models.CharField(validators=[count1_regex],max_length=1)
	sourceid = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="sourceid")
	departureid = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="destinationid")
	departure_time = models.CharField(validators=[time_regex],max_length=5)
	arrival_time = models.CharField(validators=[time_regex],max_length=5)

class Flight_instance(models.Model):
	count_regex = RegexValidator(regex=r'^\d+$', message="Enter valid number of seats")
	date_regex = RegexValidator(regex=r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$', message="Enter valid date")
	flight_id = models.ForeignKey(Airport,primary_key = True,on_delete=models.CASCADE)
	date_of_departure = models.CharField(validators=[date_regex],max_length=10)
	available_seats = models.CharField(validators=[count_regex],max_length=4)

class Offers(models.Model):
	offer_regex = RegexValidator(regex=r'^\d+$', message="Enter valid number of seats")
	date_regex = RegexValidator(regex=r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$', message="Enter valid date")
	offer_id = models.ForeignKey(Airport,primary_key = True,on_delete=models.CASCADE)
	startdate = models.CharField(validators=[date_regex],max_length=10)
	end_date = models.CharField(validators=[date_regex],max_length=10)
	description = models.CharField(max_length=1000)
