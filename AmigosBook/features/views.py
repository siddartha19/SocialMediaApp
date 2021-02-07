from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os, sys, json
import pyrebase
import re

from AmigosBook.firebasesetup import connection
firebase = pyrebase.initialize_app(connection.firebaseconfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

@csrf_exempt
def registerUser(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Email not found"}), status=400)
     if 'password' not in data:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Password not found"}), status=400)
     if 'confirmpassword' not in data:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Password not found"}), status=400)

     if data['password'] != data['confirmpassword']:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Passwords didn't match"}), status=400)

     email = data['email']
     password = data['password']
     try:
          auth.create_user_with_email_and_password(email,password)
          response = {
               'status': "Success!!",
               'status_desc': "User Account Created"
               }
          return HttpResponse(json.dumps(response), status=200)
     except:
          return HttpResponse(json.dumps({"status": "error", "Desc": "User already exists!"}), status=400)

@csrf_exempt
def userAuth(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Email not found"}), status=400)
     if 'password' not in data:
          return HttpResponse(json.dumps({"status": "error", "Desc": "Password not found"}), status=400)

     email = data['email']
     password = data['password']
     try:
          auth.sign_in_with_email_and_password(email,password)
          response = {
               'status': "Success!!",
               'status_desc': "Logged In"
               }
          return HttpResponse(json.dumps(response), status=200)
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Email or Password"}), status=400)

@csrf_exempt
def createPost(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Email not found"}), status=400)
     if 'posttext' not in data and 'postimage' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Post data not found"}), status=400)
     if 'postimage' in data and (data['postimage'].split('.')[1]).lower() != 'jpg':
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Image Foramt is not jpg"}), status=400)

     
     emailname = data['email'].split('@')[0]
     count = db.child('postscount').child('count').get()
     if count.val() == None:
          db.child('postscount').child('count').set(0)
          count = db.child('postscount').child('count').get()

     pcount = count.val()+1
     db.child('postscount').update({'count': pcount})
     post_id = emailname + "_" + str(pcount)

     imageurl = ""
     if 'postimage' in data:
          filename = data['postimage']
          cloudfilename = post_id + ".jpg"
          storage.child(cloudfilename).put(filename)
          imageurl = storage.child(cloudfilename).get_url(None)
          print(imageurl)

     postdata = {
          'posttext': data['posttext'],
          'imageurl': imageurl
     }
     db.child('posts').child(post_id).set(postdata)
     response = postdata
     return HttpResponse(json.dumps(response), status=200)

@csrf_exempt
def likePost(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Email not found"}), status=400)
     if 'post_id' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Post data not found"}), status=400)
     
     email = data['email']
     post_id = data['post_id']
     post = dict(db.child('posts').child(post_id).get().val())
     if 'likescount' not in post.keys():
          db.child('posts').child(post_id).child('likescount').set(1)
          db.child('posts').child(post_id).child('likes').child(0).set(email)
     else:
          if 'likes' not in post.keys() or email not in post['likes']:
               likescount=post['likescount']
               db.child('posts').child(post_id).child('likescount').set(likescount+1)
               db.child('posts').child(post_id).child('likes').child(likescount).set(email)
          else:
               likescount=post['likescount']
               db.child('posts').child(post_id).child('likescount').set(likescount-1)
               db.child('posts').child(post_id).child('likes').child(likescount-1).remove()
     
     response = dict(db.child('posts').child(post_id).get().val())
     return HttpResponse(json.dumps(response), status=200)

@csrf_exempt
def commentPost(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Email not found"}), status=400)
     if 'post_id' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Post data not found"}), status=400)
     if 'comment' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Comment Data not found"}), status=400)
     
     email = data['email'].split('@')[0]
     post_id = data['post_id']
     comment = data['comment']

     db.child('posts').child(post_id).child('comments').child(email).set(comment)
     
     response = dict(db.child('posts').child(post_id).get().val())
     return HttpResponse(json.dumps(response), status=200)


@csrf_exempt
def listPosts(request):
     if request.method != "GET":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     response = dict(db.child('posts').get().val())
     return HttpResponse(json.dumps(response), status=200)

@csrf_exempt
def sortPosts(request):
     if request.method != "GET":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     data = dict(db.child('posts').get().val())
     response = sorted(data.items(), key = lambda x: x[1]['likes'], reverse=True)
     return HttpResponse(json.dumps(response), status=200)

@csrf_exempt
def filterPosts(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Email not found"}), status=400)
     
     email = data['email'].split('@')[0]
     data = dict(db.child('posts').get().val())
     response = {}
     for post in data:
          if email == post.split('_')[0]:
               response[post] = data[post]

     if response == {}:
          response['status'] = "No related posts found!!"
     return HttpResponse(json.dumps(response), status=200)

@csrf_exempt
def searchPosts(request):
     if request.method != "POST":
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Request"}), status=403)

     try:
          data = json.loads(request.body) if len(request.body)>0 else None
     except:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Invalid Data"}), status=400)

     if 'email' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Email not found"}), status=400)
     if 'searchkey' not in data:
          return HttpResponse(json.dumps({"status": "Error", "Desc": "Search Key not found"}), status=400)
     
     searchkey = data['searchkey'].lower()
     data = dict(db.child('posts').get().val())
     response = {}
     for post in data.keys():
          if re.search(searchkey,data[post]['posttext'].lower()):
               print(re.search(searchkey,data[post]['posttext']), data[post]['posttext'])
               response[post] = data[post]
     if response == {}:
          response['status'] = "No related posts found!!"
     return HttpResponse(json.dumps(response), status=200)
     