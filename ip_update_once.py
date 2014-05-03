import urllib
import threading

def work (): 
  try:
    ip = urllib.urlopen('http://ip.42.pl/raw').read()
    urllib.urlopen('http://tsotnet.scripts.mit.edu/change_ip.py?ip='+ip)
  except IOError:
    pass

work ();
