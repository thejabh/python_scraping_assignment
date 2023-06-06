import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"


driver = webdriver.Firefox()
driver.get(url)

element= driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[6]/div/div/div/div[3]/div/table/tbody/tr[1]/td[4]/div/a")
print(element.text)
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

xpaths={"est_val":"/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]",
        "closing_date":"/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]",
        "description":"/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]"
}
next_button_path='//*[@id="id_prevnext_next"]'
def next_data():
    driver.find_element(By.XPATH,next_button_path).click()

fields=["est_val","closing_date","description"]
data_csv =open("D:/Data Science/data_csv.csv","w")

writer=csv.DictWriter(data_csv,fieldnames=fields)
writer.writeheader()
data_list=[]
data_dict={}
for i in range(5):    
    time.sleep(1)
    for path in xpaths.keys():
        data=driver.find_element(By.XPATH,xpaths[path])
        data_dict[path]=data.text
    writer.writerow(data_dict)
    
    print(f"completed {i+1}/5")
    next_data()
    time.sleep(1)
    
# print(data_list)
# writer.writerows(data_list)
data_csv.close()

driver.close()