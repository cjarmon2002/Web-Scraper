#! python 3
# downloadXKCD.py - Downloads every single xkcd comic.

import requests, os, bs4
from pathlib import Path
from sys import exit

url = 'http://xkcd.com'		#starting url
os.makedirs('xkcd', exist_ok=True) 	#stores comics in ./xkcd
while not url.endswith('#'):
	# download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "html.parser")

	# find the URL of the comic image
	CElem = soup.select('#comic img')
	if CElem == []:
		print('Couldn\'t find comic image')
	else:
		try:
			cURL = 'http:' + CElem[0].get('src')
			# Download the image
			print('Downloading image %s...' % (cURL))
			res = requests.get(cURL)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# skip this comic
			pLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + pLink.get('href')
			continue
		# check to see if the comic has been downloaded and quit program
		if Path(os.path.join('xkcd', os.path.basename(cURL))).exists() == True:
			print('You have downloaded all new comics.')
			exit(0)
		# save to ./xkcd
		iFile = open(os.path.join('xkcd', os.path.basename(cURL)), 'wb')
		for chunk in res.iter_content(100000):
			iFile.write(chunk)
		iFile.close()

	# get prev button's URL
	pLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + pLink.get('href')

print('Done.')