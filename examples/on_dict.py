from insta_profile import Profile
from pprint        import pprint

# only dict
profile = Profile("francistaylor.py").on_dict()
pprint(profile)

"""
{'bio': 'a python programmer, musician and artist 😜♨️🎶',
 'followers': '431 followed by',
 'following': '558 following',
 'name': 'Francis Taylor',
 'picture': 'https://bibliogram.pussthecat.org/imageproxy?userID=7695255712&url=https%3A%2F%2Fscontent-frx5-1.cdninstagram.com%2Fv%2Ft51.2885-19%2Fs150x150%2F118779313_800640644085014_1604849649686799309_n.jpg%3F_nc_ht%3Dscontent-frx5-1.cdninstagram.com%26_nc_ohc%3DZmyJ4Dl_iW4AX9EWzHA%26oh%3D16ebb0fb414eb5ea3e4c47e8ccbf5c39%26oe%3D5FBFCBAB',
 'posts': '340 posts',
 'username': '@francistaylor.py',
 'website': 'https://t.me/SrTaylor'}
 """

# Use dumps
profile = Profile("francistaylor.py").on_dict(True)
pprint(profile)

"""
('{\n'
 '    "posts": "340 posts",\n'
 '    "bio": "a python programmer, musician and artist '
 '\\ud83d\\ude1c\\u2668\\ufe0f\\ud83c\\udfb6",\n'
 '    "website": "https://t.me/SrTaylor",\n'
 '    "name": "Francis Taylor",\n'
 '    "username": "@francistaylor.py",\n'
 '    "followers": "431 followed by",\n'
 '    "following": "558 following",\n'
 '    "picture": '
 '"https://bibliogram.pussthecat.org/imageproxy?userID=7695255712&url=https%3A%2F%2Fscontent-frx5-1.cdninstagram.com%2Fv%2Ft51.2885-19%2Fs150x150%2F118779313_800640644085014_1604849649686799309_n.jpg%3F_nc_ht%3Dscontent-frx5-1.cdninstagram.com%26_nc_ohc%3DZmyJ4Dl_iW4AX9EWzHA%26oh%3D16ebb0fb414eb5ea3e4c47e8ccbf5c39%26oe%3D5FBFCBAB"\n'
 '}')"""