from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


# url - the site url which we are going to visit
url = "https://www.amazon.com/"

# Giving an option to start browser in headless mode
options = webdriver.FirefoxOptions()
options.headless = True

# Assigning service and options to the driver
driver = webdriver.Firefox(
    service=Service('geckodriver.exe'),
    options=options
)

try:
    # Opening the given url
    driver.get(url=url)
    driver.implicitly_wait(10)
    print("Opening the browser...")

    # Finding the search box by ID, clearing it, and writing in it the string "Jabra"
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("Jabra")
    driver.implicitly_wait(10)
    print("Searching for string 'Jabra'...")

    # Finding the search button by ID, pressing "ENTER" button and waiting for 3 seconds
    driver.find_element(By.ID, "nav-search-submit-button").send_keys(Keys.ENTER)
    time.sleep(3)
    print("Pressing the 'ENTER' key...")

    # Finding the "Sort by" dropdown container by Class name and double-clicking on it
    option = driver.find_element(By.CLASS_NAME, "a-button-inner")
    actionChains = ActionChains(driver)
    actionChains.double_click(option).perform()
    driver.implicitly_wait(10)
    print("Changing the sorting method...")

    # From dropdown menu, finding the element "Price: Low to High" by ID and clicking on it
    driver.find_element(By.ID, "s-result-sort-select_1").click()
    driver.implicitly_wait(10)
    print("Sorting method is changed, finding the item name...")

    # Getting the name of the first search result and printing  it’s name
    value = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["
                                          "2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").text
    print("The item's name, which has the lowest price is:", value)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
