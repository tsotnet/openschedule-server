import urllib
import threading

last_ip = None


def work (): 
  global last_ip
  threading.Timer(1, work).start (); 
  try:
    ip = urllib.urlopen('http://ip.42.pl/raw').read()
    if ip != last_ip:
      urllib.urlopen('http://tsotnet.scripts.mit.edu/change_ip.py?ip='+ip)
      last_ip = ip
      print ip, last_ip, ip!=last_ip
  except IOError:
    pass

work ();
