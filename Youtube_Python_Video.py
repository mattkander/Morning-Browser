#What we want the program to do
#What variables we need
#how are we going to do it

#Open up a series of web pages

#We need a list of urls that we will open

#Open a web page
#open up a series of tabs

import webbrowser
import time
socialMediaUrls = ["www.google.com", "www.twitter.com"]
techUrls = ["www.pcper.com", "https://www.youtube.com/user/jerzybakes420"]

def open_tabs(url_list):
	for element in url_list:
		webbrowser.open_new_tab(element)

def main():
	webbrowser.open("www.youtube.com", new=0, autoraise=False)
	time.sleep(1)
	open_tabs(socialMediaUrls)
	open_tabs(techUrls)

main()