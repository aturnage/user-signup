#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

# html boilerplate for the top of every page
page = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {color: red;}
    </style>
</head>
<body>
    <h1>Signup</h1>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username" value="%(username)s"/>
        <span class="error">%(err_username)s</span>
        <br>
        <label>Password:</label>
        <input type="text" name="password" value="%(password)s"/>
        <span class="error">%(err_password)s</span>
        <br>
        <label>Verify Password:</label>
        <input type="text" name="verify" value="%(verify)s"/>
        <span class="error">%(err_verify)s</span>
        <br>
        <label>Email (Optional):</label>
        <input type="text" name="email" value="%(email)s"/>
        <span class="error">%(err_email)s</span>
        <br>
        <input type="submit" value="submit">
</body>
</html>
"""

user_check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and user_check.match(username)

pass_check = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and pass_check.match(password)

email_check = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or email_check.match(email)

class MainHandler(webapp2.RequestHandler):
    def write_page(self, username="", password="", verify="", email="", err_username="", err_password="", err_verify="",err_email=""):
        self.response.write(page % {"username":username,"password":password, "verify":verify,"email":email,
                                    "err_username":err_username, "err_password":err_password, "err_verify": err_verify,
                                    "err_email":err_email})

    def get(self):
        self.write_page()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        have_error = False

        if not valid_username(username):
            err_username = "That's not a valid username."
            have_error = True
    
        if not valid_password(password):
            err_password = "That wasn't a valid password."
            have_error = True

        elif password != verify:
            err_verify = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            err_email = "That's not a valid email."
            have_error = True

        if have_error:
            self.write_page()
        else:
            self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def post(self):
       self.response.write("<h1>Welcome</h1>" + username)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
