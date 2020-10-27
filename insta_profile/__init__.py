import json
import requests
from bs4 import BeautifulSoup

class OnInstagram:
	def __init__(self, obj):
		self.name      = obj.name
		self.username  = obj.username
		self.followers = obj.followers
		self.following = obj.following
		self.picture   = obj.picture

class Profile:
	def __init__(self, username):
		self.url = f"https://www.instagram.com/{username}"
		self.propertys = dict(picture="og:image", description="og:description")
		
		html = requests.get(self.url)
		soup = BeautifulSoup(html.text, 'html.parser')
		
		meta_picture = soup.find_all('meta', attrs={'property':self.propertys['picture']})
		self.picture = meta_picture[0].get('content')
		
		meta = soup.find_all('meta', attrs={'property':self.propertys['description']})
		text = meta[0].get('content').split()

		self.name = f"{text[-3]} {text[-2]}"
		self.username = text[-1].replace('(','').replace(')','')
		self.followers = text[0]
		self.following = text[2]

	def on_dict(self, dumps=False, indent=4):
		dictionary = dict(name=self.name, username=self.username, followers=self.followers, following=self.following, picture=self.picture)
		if dumps:
			dictionary = json.dumps(dictionary, indent=indent)
		return dictionary

	def on_obj(self):
		return OnInstagram(self)