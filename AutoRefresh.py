from selenium import webdriver
import time

def open_and_refresh_page(url, refresh_interval_seconds, chromedriver_path):
    chrome_options = webdriver.ChromeOptions()
    #maximize window -- optional
    chrome_options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    try:
        driver.get(url)

        #refresh
        while True:
            time.sleep(refresh_interval_seconds)
            driver.refresh()
            print("Page refreshed at", time.strftime("%Y-%m-%d %H:%M:%S"))

    except KeyboardInterrupt:
        print("Script terminated")
    finally:
        driver.quit()

open_url = "https://" #replace with desired site
refresh_interval = 60  #num seconds
chromedriver_path = "filePath" #replace path

open_and_refresh_page(open_url, refresh_interval, chromedriver_path)

#########
##Notes##
#########

#my current version of Chrome (120.0.6099.129) is not currently working with ChromeDriver (https://googlechromelabs.github.io/chrome-for-testing/)



