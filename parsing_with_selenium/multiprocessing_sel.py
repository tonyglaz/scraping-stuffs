from selenium import webdriver
import time
from fake_useragent import UserAgent
from multiprocessing import Pool

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(f'user-agent={useragent.opera}')  # ie,opera


urls_list = ['https://vk.com',
             'https://www.youtube.com', 'https://stackoverflow.com']


def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path=r'D:/Py_projects/scraping/parsing_with_selenium/chromedriver.exe',
            options=options)
        driver.get(url=url)
        time.sleep(3)
        print('before screen')
        driver.save_screenshot(f"media/{url.split('//')[1]}.png")
        print('after screen')

    except Exception as ex:
        print('there is ex', ex)
    finally:
        print('before close')
        driver.close()
        print('before quit')
        driver.quit()
        print('after quit')


def main():
    print(len(urls_list))
    p = Pool(processes=len(urls_list))
    p.map(get_data, urls_list)


if __name__ == '__main__':
    main()
