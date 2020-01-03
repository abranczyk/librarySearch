# A script that automates searching for a title at 
# the three main libraries in Waterloo, ON:
# 1) Waterloo Public Library
# 2) Kitchener Public Library
# 3) University of Waterloo library

from selenium import webdriver

searchTerm = input("What do you want to search for? ")

### WPL ###
driver1 = webdriver.Chrome()
driver1.get('https://www.wpl.ca/search')
searchField = driver1.find_element_by_xpath('//*[@id="encoreSearchInput"]')
searchField.send_keys(searchTerm)
searchButton = driver1.find_element_by_xpath('//*[@id="search-encore-submit"]')
searchButton.click()

### KPL ###
driver2 = webdriver.Chrome()
driver2.get('http://books.kpl.org/search~S1/')
searchField = driver2.find_element_by_xpath('//*[@id="encoreSearchInput"]')
searchField.send_keys(searchTerm)
searchButton = driver2.find_element_by_xpath('//*[@id="searchImageSumbitComponent"]')
searchButton.click()

### UW ###
driver3 = webdriver.Chrome()
driver3.get('https://primo.tug-libraries.on.ca/primo_library/libweb/action/search.do?vid=WATERLOO&fromLogin=true&reset_config=true')
searchField = driver3.find_element_by_xpath('//*[@id="search_field"]')
searchField.send_keys(searchTerm)
searchButton = driver3.find_element_by_xpath('//*[@id="goButton"]')
searchButton.click()