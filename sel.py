from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options



#opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
"""
browser = Firefox()
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_name('q')
search_form.send_keys('real python')
search_form.submit()

results = browser.find_element_by_css_selector('.result__a')
print(results.text)


#opts = Options()
#opts.set_headless()
#browser = Firefox(options=opts)

browser = Firefox()
#browser.get('https://bandcamp.com')

#play the track
#tracks = browser.find_element_by_class_name('playbutton')
#tracks.click()

#extract the data

artist_name = browser.find_elements_by_css_selector(".detail-artist")
titles = browser.find_elements_by_css_selector(".item-title")
#artist = artist_name.text
for e in titles:
	print(e.text)
"""

browser = Firefox()
browser.get('http://www.bio-medicine.org/')
next = browser.find_element_by_tag_name('a')
next.click()



