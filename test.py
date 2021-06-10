# "appPackage": "com.example.vrit",
# "appWaitActivity": "com.example.vrit.ui.login.LoginRegistrationActivity",
# "appWaitDuration": 20,
# "autoGrantPermissions": True

# "appPackage": "com.android.mms",
# "appActivity": "com.android.mms.ui.ConversationList"

# "appPackage": "com.example.vrit",
# "appActivity": "com.example.vrit.MainActivity"

import webbrowser

try:
    assert sum([11, 2, 3]) == 6
except AssertionError:
    print("Failed")

url = "file://D:/AppiumProject/vrit/report/report.html"
webbrowser.open(url)
