from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Program Files/chromedriver.exe"

service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open the browser window maximized
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://internshala.com/internships/")

popup_element_xpath = "//*[@id='no_thanks']"
wait = WebDriverWait(driver, 10)
popup_element = wait.until(EC.element_to_be_clickable((By.XPATH, popup_element_xpath)))
popup_element.click()

location_search = "city_sidebar_chosen"
dropdown = wait.until(EC.element_to_be_clickable((By.ID, location_search)))
dropdown.click()

desired_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Bangalore')]")))
desired_option.click()

time.sleep(3)

try:
    # Wait for the search_results_container to be visible
    search_results_container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "internship_list_container_1")))
    
    # Find the individual results within the container
    search_results = search_results_container.find_elements(By.CLASS_NAME, "container-fluid.individual_internship.visibilityTrackerItem")

    for result in search_results:
        try:
            view_details_button = result.find_element(By.XPATH, ".//div[@class='cta_container']/a")
            link = view_details_button.get_attribute("href")
            print("Link:", link)
            print()
        except Exception as e:
            print("Error occurred:", e)

finally:
    driver.quit()
