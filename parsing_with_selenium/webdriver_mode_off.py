from selenium import webdriver
import time
from fake_useragent import UserAgent

auth_data={
    'login':'urlog',
    'pass':'urpass'
}

def main():
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
    options = webdriver.ChromeOptions()
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.opera}')  # ie,opera
    # disable webdriver mode
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument(f'user-agent={random.choice(user_agents)}')
    driver = webdriver.Chrome(
        executable_path=r'D:\Py_projects\scraping\parsing_with_selenium\chromedriver.exe',
        options=options
    )
    try:
        driver.get(url='https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
        time.sleep(5)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
