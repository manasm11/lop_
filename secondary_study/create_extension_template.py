#!/usr/bin/python3

import os
import requests

# TAKING INPUTS
dirname = input("Extension directory name: " )
extension_name = input("Extension Name: " )
description = input("Description: " )
jquery_version = input("JQuery Version (3.5.1): " )
print("PERMISSIONS")
is_storage = input("\tStorage (y,N): " )
is_tabs = input("\tTabs (y,N): " )
is_notifications = input("\tNotifications (y,N): " )
is_context = input("\tContext Menu (y,N): " )

# CREATE FILES
os.makedirs(dirname)
os.chdir(dirname)
manifest_file = open('manifest.json', 'a')
popup_html_file = open('popup.html', 'a')
popup_js_file = open('popup.js', 'a')
options_html_file = open('options.html', 'a')
options_js_file = open('options.js', 'a')

# ICONS
# Resize any png image from https://onlinepngtools.com/resize-png
# *** LIST OF ICONS AT ***
# https://github.com/eladkarako/ionicons_png
icon_name="color-palette-outline"
# icon_name="bandage-outline"
main_url = "https://raw.githubusercontent.com/eladkarako/ionicons_png/master/"
print("Downloading PNG icons...")
for size in ['16', '48', '128']:
  url = f'{main_url}{size}x{size}/{icon_name}.png'
  res = requests.get(url)
  open(f'icon{size}.png', 'wb').write(res.content)
print("*** Downloaded PNG icons ***")

# MANIFEST
updatePermission = lambda response, permission : response.strip().lower() == 'y' and permissions.append(permission)
permissions = []
updatePermission(is_storage, 'storage')
updatePermission(is_tabs, 'tabs')
updatePermission(is_notifications, 'notifications')
updatePermission(is_context, 'contextMenus')
is_context_bool = is_context.strip().lower() == 'y'
manifest_string='''{
  "manifest_version": 2,
  "name": "'''+extension_name+'''",
  "description": "'''+description+'''",
  "version": "0.1.0",
  "icons":{
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "browser_action": {
    "default_icon": "icon16.png",
    "default_title": "'''+extension_name+'''",
    "default_popup": "popup.html"
  },
  "permissions": '''+str(permissions).replace("'", '"')+''',
  '''+(is_context_bool and '''"background": {
    "scripts": ["eventPage.js"],
    "persistence": false
  },''' or "")+'''
  "options_page": "options.html"
}'''

manifest_file.write(manifest_string)

# JQUERY
if not jquery_version:
  jquery_version = '3.5.1'
jquery_url="https://code.jquery.com/jquery-"+jquery_version+".min.js"
print('Downloading JQuery...')
open('jquery.min.js', 'wb').write(requests.get(jquery_url).content)
print("*** Downloaded JQuery ***")

# POPUP HTML
popup_html_string='''<!DOCTYPE html>
<html lang="en">
<head>
  <title>'''+extension_name+'''</title>
  <script src="jquery.min.js"></script>
  <script src="popup.js"></script>
</head>
<body>
  <h2>'''+extension_name+'''</h2>
</body>
</html>'''
popup_html_file.write(popup_html_string)

# POPUP JS
popup_js_string='''$(function(){
  
})'''
popup_js_file.write(popup_js_string)

# OPTIONS HTML
options_html_file.write(popup_html_string.replace('popup.js', 'options.js'))

# OPTIONS JS
options_js_file.write(popup_js_string)

# CONTEXTS JS
if is_context_bool:
  is_badge = input("Do you wish to add badge (y,N)? ").strip().lower() == 'y'
if is_context_bool:
  context_file = open('eventPage.js', 'a')
  context_string = '''var menuID = "contextID"
var contextMenuItem = {
    id: menuID,
    title: "Context Title",
    contexts: ["selection"] // For all context types, refer: https://developer.chrome.com/docs/extensions/reference/contextMenus/#type-ContextType
  };
chrome.contextMenus.create(contextMenuItem)
chrome.contextMenus.onClicked.addListener(function(clickedData){
  if (clickedData.menuItemId == menuID){
    alert("Selected:", clickedData.selectionText)
  }
})
'''
  if is_badge:
    context_string += '''
chrome.storage.onChanged.addListener(function(changes, storageName){
  chrome.browserAction.setBadgeText({text: "HELLO"})
  // Changed value can be accessed by: changes.[storage_variable].newValue
})'''
  context_file.write(context_string)
  context_file.close()

# CLOSING FILES
popup_html_file.close()
popup_js_file.close()
manifest_file.close()
options_html_file.close()
options_js_file.close()