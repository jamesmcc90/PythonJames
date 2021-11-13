#DataFlame: Machine-Learning Oriented Dataframe Manipulation Interface for Pandas Dataframes
#Selenium: package used to automate web browser interaction from Python. https://www.selenium.dev/documentation/webdriver/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Keys -> for simulating pressing of arrow keys

driver = webdriver.Chrome(executable_path='C:\\Users\\James\\Desktop\\chromedriver.exe')
driver.get("https://selenium-python.readthedocs.io/index.html")
assert "Selenium" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

assert "No results found." not in driver.page_source
driver.save_screenshot('C:\\Users\\James\\Desktop\\Python.png')