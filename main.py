import os
from selenium import webdriver


def handler(request):
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280x1696")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--log-level=0")
    chrome_options.add_argument("--v=99")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(
        "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    )

    chrome_options.binary_location = os.getcwd() + "/headless-chromium"
    driver = webdriver.Chrome(
        os.getcwd() + "/chromedriver", chrome_options=chrome_options
    )
    driver.get("https://en.wikipedia.org/wiki/")
    line = driver.title
    print(line)
    driver.quit()
    return line
