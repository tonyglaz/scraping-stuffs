from selenium import webdriver
import time
import random
import pickle
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys

auth_data={
    'login':'urlog',
    'pass':'urpass'
}

def main():
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
    options = webdriver.ChromeOptions()
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.opera}')  # ie,opera

    # options.add_argument(f'user-agent={random.choice(user_agents)}')
    driver = webdriver.Chrome(
        executable_path=r'D:\Py_projects\scraping\parsing_with_selenium\chromedriver.exe',
        options=options
    )
    try:
        # driver.get(url='https://vk.com/')
        # time.sleep(3)
        # email_input = driver.find_element('id', 'index_email')
        # email_input.clear()
        # email_input.send_keys(auth_data['login'])
        # time.sleep(3)
        # # enter = driver.find_element('span', 'FlatButton__content').click()
        # # time.sleep(3)
        # pass_input = driver.find_element('id', 'index_pass')
        # pass_input.clear()
        # pass_input.send_keys(auth_data['pass'])
        # time.sleep(3)
        # #enter = driver.find_element('id', 'index_login_button').click()
        # pass_input.send_keys(Keys.ENTER)
        # time.sleep(3)
        # news = driver.find_element('id', 'l_nwsf').click()
        # time.sleep(3)
        # #cookies
        # pickle.dump(driver.get_cookies(),open(f'{auth_data["login"][-3:]}cookies','wb'))
        driver.get(url='https://vk.com/')
        time.sleep(3)

        for cookie in pickle.load(open(f'{auth_data["login"][-3:]}cookies','rb')):
            driver.add_cookie(cookie)
        time.sleep(3)
        driver.refresh()
        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
