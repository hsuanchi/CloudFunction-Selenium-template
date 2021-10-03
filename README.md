# CloudFunction-Selenium-template

## How to Start?
### 1. Clone this project
```
$ git clone git@github.com:hsuanchi/CloudFunction-Selenium-template.git
```

### 2. Deploy to your Cloud Function
1. Upload ZIP the chromedriver.zip & headless-chromium.zip

2. install [gcloud sdk](https://www.maxlist.xyz/2021/08/28/en-quickstart-python-cloudfunction-deploy-with-gcloud-sdk/)
3. run deploy
```
$ sh deploy.sh
```


## How to change the Chrome webdriver version?
Now we using ChromeDriver 67.0.3396.99. You also can download new version form [here](https://chromedriver.chromium.org/home).

* how to check the Chrome Version & Chrome Driver Version?
```
chrome_driver_version = driver.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]
chrome_version = driver.capabilities["version"]
```
