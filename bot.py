from requests import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random,time,os,re,json
from time import sleep
import undetected_chromedriver as uc
cwd = os.getcwd()
opts = Options()
opts.headless = True

def xpath_type(el,mount):
    return wait(browser,15).until(EC.element_to_be_clickable((By.XPATH, el))).send_keys(mount)
def xpath_fast(el):
    return wait(browser,1).until(EC.element_to_be_clickable((By.XPATH, el))).click()
def xpath_el(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    
    element_all.click()
 
def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return str(date)

def bot():
    global browser
    browser = uc.Chrome(options=opts,driver_executable_path=f"{cwd}//chromedriver.exe")
    #browser = webdriver.Chrome(,options=opts, desired_capabilities=dc)
    browser.get("https://www.tiktok.com/")
    with open(f"{cwd}//cookies.json", 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://www.tiktok.com/")
    print(f'{date()} Process to like video')
    browser.get(url_vid)
    xpath_el('//span[@data-e2e="like-icon"]/parent::button')
    print(f'{date()} Success like video')
    print(f'{date()} Process rewatch video..')
    xpath_el('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]')
    durs = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]'))).text
    video_duration = durs.split("/")[1].split(":")[1]
    print(f'{date()} Get Duration video {video_duration}s')
    for i in range(duration):
        browser.get(url_vid)
        sleep(int(video_duration)+2)
        print(f'{date()} Process rewatch video {i+1}x')
    print(f'{date()} Success rewatch video..')
    print(f'{date()} Process to share video..')
    xpath_el('//span[@data-e2e="share-icon"]/parent::button')
    css_selct = '.css-1mkqzm9 > .css-1mkqzm9-content > .css-1mkqzm9-inner > .tiktok-63dd6w-DivShareWrapper > .tiktok-1881jny-AShareLink:nth-child(2)'
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selct)))
    element_all.click()
    xpath_el('(//div[contains(@class,"DivUserItemContainer")])[1]')
    xpath_el('//button[contains(@class,"Button-StyledSendButton")]')
    print(f'{date()} Success share video..')
    sleep(1)
    print(f'{date()} Process to comment video..')
    element =  wait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]')))
    browser.execute_script("arguments[0].scrollIntoView();", element)
 
    xpath_type('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div',word)
    sleep(1)
    xpath_el('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/div/div/div[2]')
    print(f'{date()} Success comment video..')
    sleep(5)
if __name__ == '__main__':
    global url_vid, duration,word
    print(f"{date()} Automation Tiktok")
    url_vid = input(f'{date()} Input Link Video: ')
    word = input(f'{date()} Input Comment: ')
    duration = int(input(f'{date()} How much rewatch Video: '))
    bot()
 