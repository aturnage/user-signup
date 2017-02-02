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
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Signup
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

# a form for asking for username
username_form = """
<form name="username" method="post">
    <label>
        Username: 
        <input type="text" name="username"/>
    </label>
"""
#Form asking for password
password_form = """
<form name="password" method="post">
    <label>
        Password: 
        <input type="text" name="password"/>
    </label>
"""
#Form verifying password
verify_form = """
<form name="verify" method="post">
    <label>
        Verify: 
        <input type="text" name="verify"/>
    </label>
"""
#Form asking for email
email_form = """
<form name="email" method="post">
    <label>
        Email (Optional): 
        <input type="text" name="email"/>
    </label>
"""
#submit button for all forms
submit = """
<form>
    <input type="submit" value="submit">
</form>
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
    def get(self):
        content = (page_header + username_form + "<br>" + password_form + "<br>" + verify_form +
        "<br>" + email_form + "<br>" + submit + page_footer)

        self.response.write(content)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

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
            err_content = (page_header + username_form + err_username + "<br>" + password_form + err_password + "<br>" +
            verify_form + err_verify + "<br>" + email_form + err_email + "<br>" + submit + page_footer)

            self.response.write(err_content)
        else:
            self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def post(self):
       self.response.write("<h1>Welcome</h1>" + username)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
