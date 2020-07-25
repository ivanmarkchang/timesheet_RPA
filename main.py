from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from credentials import *

# point to chromedriver
chromedriver_location = "/Users/ivan.chang/code/ultipro_autofill/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

# go to webpage
driver.get('https://nw13.ultipro.com/default.aspx')

# go to username field and fill it out
username = driver.find_element_by_id("ctl00_Content_Login1_UserName")
username.send_keys(myUsername)

# go to password field and fill it out
password = driver.find_element_by_id("ctl00_Content_Login1_Password")
password.send_keys(myPassword)

# go to Login and click submit
driver.find_element_by_id("ctl00_Content_Login1_LoginButton").click()

# navigate to Time
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_name("menuButton")
action.move_to_element(firstLevelMenu).perform()
firstLevelMenu.click()
secondLevelMenu = driver.find_element_by_xpath("//div[@class='menuTopHeaderContainer']")
action.move_to_element(secondLevelMenu).perform()
thirdLevelMenu = driver.find_element_by_xpath("//div[@aria-label='Myself']")
action.move_to_element(thirdLevelMenu).perform()
fourthLevelMenu = driver.find_element_by_xpath("//*[@id='newMegaMenuContainer']/div[2]/div[3]/div[2]/div[2]/ul/li")
action.move_to_element(fourthLevelMenu).perform()
fourthLevelMenu.click()

"""
TODO:
# Now that we've navigated to the timesheet, we need to enter in our times
# Navigate to the first Entry
mon1_timeCode = driver.find_element_by_xpath("/html/body/app/div/div/div/div/div/timesheet/div/div[2]/timesheet-view/div/timesheet-entry/div/form/div[1]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/timesheet-entry-detail/div/table/tbody/tr[1]/td[1]/labor-metric-input/div").click()
"""