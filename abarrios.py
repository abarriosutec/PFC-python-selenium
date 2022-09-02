import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:80") 

elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/span[2]/input')
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/span/input').click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="CreateTicketInQueue"]/input').click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="TitleBox--_Ticket_Create_html--messagedetails----Q3JlYXIgdW4gbnVldm8gdGlja2V0IGVuIEdlbmVyYWw_---0"]/table/tbody/tr[6]/td[2]/input').send_keys("Asunto de prueba")

driver.find_element(By.XPATH, '//*[@id="SubmitTicket"]/div[2]/input').click()

driver.close()
