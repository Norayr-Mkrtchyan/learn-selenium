from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Declaring some variables to help us work with the driver
# url - the site url which we are going to visit
# chromedriver_path - chromedriver path in the local folder
url = "https://www.amazon.com/"
chromedriver_path = 'chromedriver.exe'

# Giving an option to automatically start browser in maximized mode  by adding an argument "start-maximized"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Assigning service and options to the driver
driver = webdriver.Chrome(
    service=Service(chromedriver_path),
    options=options
)

try:
    # Opening the given url
    driver.get(url=url)
    driver.implicitly_wait(10)

    # Finding the search box by ID, clearing it, and writing in it the string "Jabra"
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("Jabra")
    driver.implicitly_wait(10)

    # Finding the search button by ID and clicking on it
    driver.find_element(By.ID, "nav-search-submit-button").click()
    driver.implicitly_wait(10)

    # Finding the "Sort by" dropdown container by Class name and clicking on it
    driver.find_element(By.CLASS_NAME, "a-dropdown-container").click()
    driver.implicitly_wait(10)

    # From dropdown menu, finding the element "Price: Low to High" by ID and clicking on it
    driver.find_element(By.ID, "s-result-sort-select_1").click()
    driver.implicitly_wait(10)

    # Getting the name of the first search result and printing  it’s name
    value = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["
                                          "2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").text
    print("The item's name, which has the lowest price is:", value)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
