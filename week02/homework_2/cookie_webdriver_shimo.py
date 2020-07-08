from logging import exception
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from contextlib import contextmanager
import time

# Because we always need to wait for an operation to complete and set a timeout period.
# Blow part is the functions to make these actions reusable.
#


def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(
        condition_function.__name__))

# def page_has_loaded(old_page: WebElement) -> bool:
#     new_page = browser.find_element_by_tag_name('html')
#     return new_page.id != old_page.id


@contextmanager
def wait_for_page_load(browser: WebDriver):
    old_page = browser.find_element_by_tag_name('html')

    yield

    def page_has_loaded():
        new_page = browser.find_element_by_tag_name('html')
        return new_page.id != old_page.id

    wait_for(page_has_loaded)


try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://shimo.im/welcome')
    # Wait for the browser to meet the conditions.
    # The condition is document.readyState == 'complete'
    WebDriverWait(browser, 10).until(lambda d: d.execute_script(
        'return document.readyState') == 'complete')
    # With customized functions:
    # log-in button xpath: //*[@id="homepage-header"]/nav/div[3]/a[2]/button
    # old_page = browser.find_element_by_tag_name('html')
    # login_button = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    # login_button.click()
    # wait_for(page_has_loaded(old_page))

    # With contextmanager decorator:
    with wait_for_page_load(browser):
        browser.find_element_by_xpath(
            '//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('<PHONE_NUM>')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('<PASSWORD>')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    

except Exception as e:
    print(e)
finally:
    print('You should close the browser manually...')
