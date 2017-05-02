from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import csv

chrome_options = Options()
chrome_options.add_argument("--incognito") #meant to avoid certain caching errors
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
wait = WebDriverWait(browser, 60)

browser.get('site login page goes here')

elem = browser.find_element_by_name('') #find the login name region
elem.send_keys('username') #this will autofill in 'username', make sure to change to your username. When the script executes, you should enter in your password and hit enter in the appropriate field

elem = browser.find_element_by_name('') #find the password field. just enter in password manually
i = 0

with open('csv file', 'rb') as csvfile: #make sure to change the path to the path for your CSV list on your local machine
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i == 200:
            sleep(60) #rest a minute so you aren't making too many requests
            i = 0
        wait.until(lambda browser: browser.find_element_by_id('element')) #wait until next page loads, allows user to enter password and login before continuing
        elem = browser.find_element_by_id('element you want to click on') #the directory you need to select

        ActionChains(browser).context_click(elem).perform()
        elem = browser.find_element_by_id('number goes here') #this clicks a specific context menu option
        elem.click()
        elem = browser.find_element_by_id('')
        elem.send_keys('path to pdfs' + row[0]) #make sure to change to the path of your pdf forms on your local machine
        browser.find_element_by_name('').click()
        colnum = 0
        for col in row:
            if col == row[0] or col == row[1] or col == row[2] or col ==row[3]:
                pass
            else:
                if col is not None:
                    elem = browser.find_element_by_id('')
                    elem.send_keys("" + col) #add a path to attachments
                    browser.find_element_by_name('').click()
        browser.find_element_by_name('').click()
        browser.execute_script('') #there was a button on the page that just executed a javascript command, so I did that directly
        wait.until(lambda browser: browser.find_element_by_name(''))
        elem = browser.find_element_by_name('')
        elem.send_keys(row[2]) #this is where an important index in the file should be
        elem.send_keys(Keys.TAB) #generate an autocomplete for the index
        wait.until(lambda browser: browser.find_element_by_name(''))
        select = Select(browser.find_element_by_name(''))
        select.select_by_value('') #select specific option from a dropdown menu
        browser.find_element_by_name('').click()
        try:
            WebDriverWait(browser, .5).until(EC.alert_is_present(),
                                            'Timed out waiting for popup to appear.')
            alert = browser.switch_to_alert()
            alert.accept()
            print('duplicate index') 
            alert = browser.switch_to_alert()
            alert.dismiss()
        except TimeoutException:
            print('new')

        print(row[0] + ", " + row[1] + " indexed") #used for logging

        browser.get('') #go to whatever address you were at right after login, start the process again

        i = i + 1
