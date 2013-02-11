from django.db import models

class UsersModel(models.Model):
	user = models.CharField(max_length=128)
	password = models.CharField(max_length=128)
	count = models.IntegerField()
	user.primary_key=True
	
	@classmethod
	def login(cls, userInput, passwordInput):
		try:
			result = cls.objects.get(user=userInput, password=passwordInput)
		except cls.DoesNotExist:
			return -1
		else:
			result.count += 1
			result.save()
			return result.count
			
	@classmethod
	def add(cls, user_input, password_input):
		if (len(user_input) == 0) or (len(user_input) > 128):
			return -3 #Invalid username
		elif (len(password_input) > 128):
			return -4 #Bad password
		else:
			try:
				result = cls.objects.get(user=user_input)
			except cls.DoesNotExist:
				new = cls(user=user_input, password=password_input, count=1)
				new.save()
				return new.count
			else:
				return -2 #User exists
				
	@classmethod
	def TESTAPI_resetFixture(cls):
		cls.objects.all().delete()   #All users data are deleted
		return 1