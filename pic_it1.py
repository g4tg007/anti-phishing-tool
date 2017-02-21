from selenium import webdriver

class FirefoxPic():
#browser = webdriver.Firefox()
	def __init__(self, url):
		self.url = url

	def picpage(self):
		browser= webdriver.Firefox()
		browser.set_window_size(1200, 900)
		browser.get(self.url)
		fileName1=self.url.replace("/","_").replace('http:','')
		fileName =fileName1+".jpg"
		browser.save_screenshot(fileName)
		browser.quit()

		pass


if __name__ == "__main__":
	picurl=FirefoxPic('http://jd.com')
	picurl.picpage()
	print "done!"

