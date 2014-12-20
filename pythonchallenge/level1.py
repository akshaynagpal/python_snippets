# http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans
data = "http://www.pythonchallenge.com/pc/def/map.html"
incoming = "abcdefghijklmnopqrstuvwxyz"
outgoing = "cdefghijklmnopqrstuvwxyzab"
trans = maketrans(incoming,outgoing)
print data.translate(trans)

"""
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url
"""
