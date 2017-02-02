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
    <br>
"""
#Form asking for password
password_form = """
<form name="password" method="post">
    <label>
        Password: 
        <input type="text" name="password"/>
    </label>
    <br>
"""
#Form verifying password
verify_form = """
<form name="verify" method="post">
    <label>
        Verify: 
        <input type="text" name="verify"/>
    </label>
    <br>
"""
#Form asking for email
email_form = """
<form name="email" method="post">
    <label>
        Email (Optional): 
        <input type="text" name="email"/>
    </label>
    <br>
"""
#submit button for all forms
submit = """
<form>
    <input type="submit" value="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = page_header + username_form + password_form + verify_form + email_form + submit + page_footer

        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
