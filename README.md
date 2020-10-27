# InstaProfile
Get instagram profile information.


## Install
* * *

* Clone the repository ```git clone https://github.com/francis-taylor/InstaProfile``` or download.

* enter the folder: ```cd InstaProfile```

* Install the dependencies: ```pip install -r requirements.txt```

## Basic usage

```python
from insta_profile import profile

profile = Profile("Username")
```
 
## profile.on_dict() - (On Dictionary)

* Simple:

```python
from insta_profile import profile
from pprint        import pprint

profile = Profile("FrancisTaylor.py").on_dict()
pprint(profile)

>>>
{'followers': '431',
 'following': '558',
 'name': 'Francis Taylor',
 'picture': 'https://instagram.fssz7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/118779313_800640644085014_1604849649686799309_n.jpg?_nc_ht=instagram.fssz7-1.fna.fbcdn.net&_nc_ohc=ZmyJ4Dl_iW4AX9DMvXy&oh=bdc735ba9d906d52fcf0a4094565ef5b&oe=5FBFCBAB',
 'username': '@francistaylor.py'}
```

* Dumps Support:

```python
from insta_profile import profile
from pprint        import pprint

profile = Profile("FrancisTaylor.py").on_dict(dumps=True, indent=4) #indent by pattern 4, not required
pprint(profile)

>>>
('{\n'
 '    "name": "Francis Taylor",\n'
 '    "username": "@francistaylor.py",\n'
 '    "followers": "431",\n'
 '    "following": "558",\n'
 '    "picture": '
 '"https://instagram.fssz7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/118779313_800640644085014_1604849649686799309_n.jpg?_nc_ht=instagram.fssz7-1.fna.fbcdn.net&_nc_ohc=ZmyJ4Dl_iW4AX9DMvXy&oh=bdc735ba9d906d52fcf0a4094565ef5b&oe=5FBFCBAB"\n'
 '}')
```

## profile.on_obj() - (On Object)

```python
from insta_profile import profile
from pprint        import pprint

profile = Profile("FrancisTaylor.py").on_obj()

pprint(profile.name)
pprint(profile.username)
pprint(profile.followers)
pprint(profile.following)
pprint(profile.picture)

>>>
'Francis Taylor'
'@francistaylor.py'
'431'
'558'
'https://instagram.fssz7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/118779313_800640644085014_1604849649686799309_n.jpg?_nc_ht=instagram.fssz7-1.fna.fbcdn.net&_nc_ohc=ZmyJ4Dl_iW4AX9DMvXy&oh=bdc735ba9d906d52fcf0a4094565ef5b&oe=5FBFCBAB'
```
