# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages

import requests
import simplejson

def home(request): 
  
  payload = {'lat': '13.060422', 'lon': '80.249583','city_id':'7','radius':'2000','random':'true','apikey':'a495e149451f47b8a08d70282ac1ad78'}
  r = requests.get("https://api.zomato.com/v1/search.json/near",params=payload)

  dd=simplejson.loads(r.text)
  cuisines = dd['cuisines'].encode()
  cuisines = cuisines.split(',')
  
  variables=RequestContext(request,{'dd':dd,'r':r,'cuisines':cuisines})
  return render_to_response('main.html',variables)

def bangalore(request): 
  
  payload = {'lat': '12.9715987', 'lon': '77.5945627','city_id':'4','radius':'2000','random':'true','apikey':'a495e149451f47b8a08d70282ac1ad78'}
  r = requests.get("https://api.zomato.com/v1/search.json/near",params=payload)

  dd=simplejson.loads(r.text)
  cuisines = dd['cuisines'].encode()
  cuisines = cuisines.split(',')
  
  variables=RequestContext(request,{'dd':dd,'r':r,'cuisines':cuisines})
  return render_to_response('main.html',variables)

def mumbai(request): 
  
  payload = {'lat': '19.0759837', 'lon': '72.8776559','city_id':'3','radius':'2000','random':'true','apikey':'a495e149451f47b8a08d70282ac1ad78'}
  r = requests.get("https://api.zomato.com/v1/search.json/near",params=payload)

  dd=simplejson.loads(r.text)
  cuisines = dd['cuisines'].encode()
  cuisines = cuisines.split(',')
  
  variables=RequestContext(request,{'dd':dd,'r':r,'cuisines':cuisines})
  return render_to_response('main.html',variables)

def delhi(request): 
  
  payload = {'lat': '28.635308', 'lon': '77.22496','city_id':'1','radius':'2000','random':'true','apikey':'a495e149451f47b8a08d70282ac1ad78'}
  r = requests.get("https://api.zomato.com/v1/search.json/near",params=payload)

  dd=simplejson.loads(r.text)
  cuisines = dd['cuisines'].encode()
  cuisines = cuisines.split(',')
  
  variables=RequestContext(request,{'dd':dd,'r':r,'cuisines':cuisines})
  return render_to_response('main.html',variables)
