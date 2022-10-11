from selenium import webdriver
#from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent


def main():
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
    options = webdriver.ChromeOptions()
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.random}')  # ie,opera
    options.add_argument('--proxy-server=23.227.38.51:8000')
    # proxy_options = {
    #     'proxy': {
    #         'https': f'http://{login}:{password}@23.227.38.51:8000'
    #     }
    # }
    # options.add_argument(f'user-agent={random.choice(user_agents)}')
    driver = webdriver.Chrome(
        executable_path=r'D:\Py_projects\scraping\parsing_with_selenium\chromedriver.exe',
        options=options
    )
    try:
        # driver.get(url=url)
        # time.sleep(3)
        # driver.get_screenshot_as_file('db.png')
        driver.get(url='https://instagram.com/')
        # driver.get_screenshot_as_file('stack.png')
        time.sleep(3)
        # driver.refresh()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
