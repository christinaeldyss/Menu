Menu Project

Description: This code, menu.py, is designed to process a Menu of items, summing the items contained in each menu, as long as those items contain a "Label". In order to process, the Menu needs to be in a json file. The output will be an array of the item-sums for each menu.

Technical Summary: Menu.py is written in Python, using Python 3.6.3. It was developed in a Windows system and assumes the end user will be operating in a Windows environment as well. It is also assumed the end user has Python installed on their machine, as well as PowerShell and pytest. 

Operating Instructions:
 1) Please download the menu.py file and place it in a directory such that Python is able to call it. If using the test menu json file, download the "menu.json" file as well from the Testing folder and place in the same folder as menu.py.
 2) In the command line, using Python, type "import menu" and press enter
 3) Type "menu.menu_project('menu.json')" and press enter
 
 This should output an array containing the item sums. In the menu.json example given, this should output "[46,0,248]"
 
 Testing Instructions:
 1) Download the Testing folder contained in this repository
 2) Open PowerShell and navigate to this directory
 3) Type "python -m pytest" and press enter
 4) This will run each test contained in this directory, using test files contained as well in that directory. The output should contain a "." next to each test run if it passed (which they all hopefully should!).
 
