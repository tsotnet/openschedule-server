import mechanize
import sys
import threading
import json
  
class User:
  def __init__(self, username, password):
    self.br = mechanize.Browser()
    self.br.set_handle_robots(False)
    self.username = username
    self.password = password
  
  def authenticate(self, response = None):
    url = None if response == None else response.geturl()
    if url == None:
      resp = self.br.open("https://student.mit.edu/cgi-docs/shrwstop.html")
      return self.authenticate(resp)
    elif url == "https://idp.mit.edu:443/idp/Authn/MIT":
      forms = mechanize.ParseResponse(response, backwards_compat=False)
      form = forms[1]
      form["j_username"] = self.username
      form["j_password"] = self.password
      resp = self.br.open(form.click())
      return self.authenticate(resp)
    elif url == "https://idp.mit.edu:443/idp/profile/SAML2/Redirect/SSO":
      forms = mechanize.ParseResponse(response, backwards_compat=False)
      form = forms[0]
      resp = self.br.open(form.click())
      return self.authenticate(resp)
    elif url == "https://student.mit.edu/cgi-docs/shrwstop.html":
      # Authentication succeded!
      return True
    else:
      # Something went wrong, authentication failed :'(
      return False
      
  def getWebsite(self, url):
    resp = self.br.open(url)
    if resp.geturl() != "https://idp.mit.edu:446/idp/Authn/Certificate?login_certificate=Use+Certificate+-+Go":
      return resp.read()
    else:
      return

  def getSubjectListing(self):
    s = self.getWebsite("https://student.mit.edu/cgi-bin/shrwssor.sh")
    s = s[s.find("Current Registration"):]
    lst = []
    while True:
      i = s.find("<TR>")
      j = i+s[i:].find("</table>")
      if i == -1 or i > j:
        return lst
      s = s[i:]
      x, y = None, None
      s = s[s.find("<TD")+1:]
      for k in range(0,j-i):
        if x == None and s[k] == ">":
          x = k + 1
        elif y == None and s[k] == "<":
          y = k
      sbj = s[x:y].strip()
      if sbj != "":
        lst.append(sbj)
    return lst
