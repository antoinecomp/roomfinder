from selenium import webdriver


api_location = 'http://iphoneapp.spareroom.co.uk'
api_search_endpoint = 'flatshares'
api_details_endpoint = 'flatshares'

location = 'http://www.spareroom.co.uk'
details_endpoint = 'flatshare/flatshare_detail.pl?flatshare_id='

def contact_room(room_id):
    url = '{location}/{endpoint}/{id}?format=json'.format(location=api_location, endpoint=api_details_endpoint, id=room_id)

    driver_path = 'C:\Program Files\chromedriver'
    driver = webdriver.Chrome(executable_path = driver_path	)  # Optional argument, if not specified will search path.
    # Go to your page url
    driver.get(url)
    # Get button you are going to click by its id ( also you could use find_element_by_css_selector to get element by css selector)
    button_element = driver.find_element_by_id('button id')
    button_element.click()

contact_room(13829371)