import json
import os
import sys
import tempfile
import traceback
import re
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from models import UsersModel

@csrf_exempt
def login(request):
    temp = json.loads(request.body)
    if request.method == 'POST':
		userInput = temp['user']
		passwordInput = temp['password']
		response_data = {}
		response_data['errCode'] = UsersModel.login(userInput, passwordInput)
		
    if response_data['errCode'] >= 1:
                response_data['count'] = response_data['errCode']
                response_data['errCode'] = 1
                		
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt	
def add(request):
    temp = json.loads(request.body)
    if request.method == 'POST':
		userInput = temp['user']
		passwordInput = temp['password']
		response_data = {}
		response_data['errCode'] = UsersModel.add(userInput, passwordInput)
		
		if response_data['errCode'] >= 1:
			response_data['count'] = response_data['errCode']
			
		return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt	
def resetFixture(request):
	UsersModel.TESTAPI_resetFixture()
	response_data = {'errCode': 1}
	return HttpResponse(json.dumps(response_data), content_type = "application/json")

@csrf_exempt	
def unitTests(request):
	try:
		errMsg = ""
		output = ""
		totalTests = 0
		nrFailed   = 0
		while True:
			#cmd = "python \"C:\\Users\\Oscar\\Documents\\School\\Spring 2013\\CS 169\\warmup\\backend\\unitTest.py \" >temp 2>&1"
                        cmd = "make -C /app >temp 2>&1"
                        code = os.system(cmd)
			if code != 0:
				errMsg = "Error running command (code="+str(code)+"): "+cmd+"\n"
				
			try:
				ofileFile = open("temp", "r")
				output = ofileFile.read()
				ofileFile.close ()
			except:
				errMsg += "Error reading the output "+traceback.format_exc()
				break
			
			m = re.search(r'Ran (\d+) tests', output)
			if not m:
				errMsg += "Cannot extract the number of tests\n"
				break
			totalTests = int(m.group(1))
			m = re.search(r'FAILED. *\(failures=(\d+)\)', output)
			if m:
				nrFailures = int(m.group(1))
			break

		response_data = { 'output' : errMsg + output,
				 'totalTests' : totalTests,
				 'nrFailed' : nrFailed }
					
	finally:
		return HttpResponse(json.dumps(response_data), content_type = "application/json")