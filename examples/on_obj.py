from insta_profile import Profile
from pprint        import pprint

profile = Profile("francistaylor.py").on_obj()

print("Name:", profile.name)
print("Username:", profile.username)
print("Website:", profile.website)
print("Bio:", profile.bio)
print("Posts:", profile.posts)
print("Followers:", profile.followers)
print("Following:", profile.following)
print("Picture:", profile.picture)

"""
Name: Francis Taylor
Username: @francistaylor.py
Website: https://t.me/SrTaylor
Bio: a python programmer, musician and artist 😜♨️🎶
Posts: 340 posts
Followers: 431 followed by
Following: 558 following
Picture: https://bibliogram.pussthecat.org/imageproxy?userID=7695255712&url=https%3A%2F%2Fscontent-frx5-1.cdninstagram.com%2Fv%2Ft51.2885-19%2Fs150x150%2F118779313_800640644085014_1604849649686799309_n.jpg%3F_nc_ht%3Dscontent-frx5-1.cdninstagram.com%26_nc_ohc%3DZmyJ4Dl_iW4AX9EWzHA%26oh%3D16ebb0fb414eb5ea3e4c47e8ccbf5c39%26oe%3D5FBFCBAB
"""