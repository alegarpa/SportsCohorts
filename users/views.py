from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import UserProfile, FriendRequest
import json


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.encode())
        username = data.get('username', 'NONE')
        password = data.get('password', 'NONE')
        user = UserProfile().auth(username=username, password=password)
        if user is not None:
            UserProfile().loginUser(request, user)
            response = {'errCode': UserProfile.SUCCESS}
        else:
            response = {'errCode': UserProfile.INVALID_CREDENTIALS}
        return HttpResponse(json.dumps(response), content_type='application/json', status=200)

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        UserProfile().logout(request)
        #Redirect to a success page
        return HttpResponse(json.dumps({'errCode': UserProfile.SUCCESS}), 
            content_type='application/json', status=200)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.encode())
        username = data.get('username', 'NONE')
        password = data.get('password', 'NONE')
        email = data.get('email', 'NONE')
        firstName = data.get('firstName', 'NONE')
        lastName = data.get('lastName', 'NONE')
        err_code = UserProfile().registerUser(username, password, email, firstName, lastName)
        response = {'errCode': err_code}
        return HttpResponse(json.dumps(response), content_type='application/json', status=200)

@csrf_exempt
def requestFriend(request):
    if request.method == 'POST':
        data = json.loads(request.body.encode())
        username = data.get('username', 'NONE')
        friend = data.get('friend', 'NONE')
        err_code = FriendRequest().requestFriend(username, friend)
        response = {'errCode': err_code}
        return HttpResponse(json.dumps(response), content_type='application/json', status=200)


@csrf_exempt
def reset(request):
    UserProfile().TESTAPI_reset()
    return HttpResponse(json.dumps({'errCode': UserProfile.SUCCESS}), content_type='application/json', status=200)     

