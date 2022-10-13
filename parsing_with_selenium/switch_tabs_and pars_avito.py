from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

auth_data = {
    'login': '',
    'pass': 'urpass'
}


def main():
    options = webdriver.ChromeOptions()
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.opera}')  # ie,opera
    driver = webdriver.Chrome(
        executable_path=r'D:\Py_projects\scraping\parsing_with_selenium\chromedriver.exe',
        options=options
    )

    # options.add_argument(f'user-agent={random.choice(user_agents)}')
    driver = webdriver.Chrome(
        executable_path=r'D:\Py_projects\scraping\parsing_with_selenium\chromedriver.exe',
        options=options
    )
    try:
        driver.get('https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty')
        print(driver.current_url)
        item=driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
        time.sleep(3)
        item[0].click()
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_url)
        time.sleep(5)
        adress=driver.find_element(By.CLASS_NAME,'style-item-address__string-wt61A')
        print(adress.text)

        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        print(driver.current_url)
        item[1].click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        adress = driver.find_element(By.CLASS_NAME, 'style-item-address__string-wt61A')
        print(adress.text)
        time.sleep(2)



    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
