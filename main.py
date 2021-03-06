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
import caesar
import cgi

def buildpage(text_area_content):
    styles = '''<style>
        * {
            font-family: "Trebuchet", Gadget, sans-serif;
            color: #111;
        }
        img {
            height: 95vh;
        }
        #eyes {
            z-index: -1;
            position: absolute;
            transform: translate3d(-1px, 0px, 0px);
            transition: transform 1s ease-in-out;
            width: 68%;
        }
        #bust:hover + #eyes{
            transform: translate3d(18px, 0px, 0px);
        }
        #bust {
            z-index: +1;
            position: absolute;
            float:left;
            width: 68%;
        }
        .right {
            float: right;
            clear: right;
        }
        input {
            z-index: +10;
            padding: 10px;
            margin: 20px;
        }
        #rot {
            width: 70px;
        }
        #message {
            width: 205px;
            height: 120px;
        }

    </style>'''
    img_divs = '<div id="bust"><img src = "/images/caesar_bust.png"/></div><div id="eyes"><img src = "/images/caesar_eyes.png"/></div>'
    header = '<title>Caesar Cipher</title><h2 class="right">Caesar Cipher</h2><br>'
    rot_label = '<div class="right"><label>Rotate by: </label>'
    rotation = '<input id="rot" type = "number" name = "rot" ></div>'
    text_label = '<div class="right"><label>Message to encode: </label>'
    textarea = '<textarea id="message" name = "message">' + text_area_content + '</textarea></div>'
    button = '<input class = "right" type="submit" />'
    form = '<div class="right">' + styles + '<form method="post">' + rot_label + rotation + '<br>' + text_label + textarea + '<br>' + button + '</form></div>'
    return header + form + img_divs

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildpage("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        num = self.request.get("rot")
        encrypted_message = caesar.encrypt(message, int(num))
        escaped_message = cgi.escape(encrypted_message)
        content = buildpage(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
