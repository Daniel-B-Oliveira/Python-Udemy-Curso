#type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO__WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Espere pelo input
    # APjFqb

    search_input = WebDriverWait(browser, TIME_TO__WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    search_input.send_keys('Hello word!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # Dorme por 10 segundos
    sleep(TIME_TO__WAIT)

    # import time

    # from pathlib import Path

    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service 

    # print('Hello word!')

    # ROOT_FOLDER = Path(__file__).parent
    # CHROMEDRIVER_EXECUTAVEL = ROOT_FOLDER / 'drivers' / 'chromedriver.exe' 

    # print(CHROMEDRIVER_EXECUTAVEL)

    # chrome_options = webdriver.ChromeOptions()
    # chrome_servide = Service(executable_path=str(CHROMEDRIVER_EXECUTAVEL))
    # chrome_browser = webdriver.Chrome(
    #     service=chrome_servide,
    #     options=chrome_options,
    # )

    # chrome_browser.get('https://www.google.com.br/')
    # time.sleep(30)


