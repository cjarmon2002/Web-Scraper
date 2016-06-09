#! python 3
# mapIt.py - launches a map in the browser using an address from the command
# or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)