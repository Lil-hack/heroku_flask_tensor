from flask import Flask
from datetime import datetime
from selenium import webdriver
app = Flask(__name__)
import os
import random
from threading import Thread, Lock
from flask import send_file
import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# path = os.getcwd()
# list_cockie=[]
# with os.scandir(path+"/cockiestwitch") as listOfEntries:
#     for entry in listOfEntries:
#         # печать всех записей, являющихся файлами
#         if entry.is_file():
#            list_cockie.append(entry.name)
        
def new(url):
    print(url)
    url=f'https://www.twitch.tv/{url}'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("http://check.torproject.org")
    driver.save_screenshot(f'ip.png')
    driver.get(url)
    for i in range(0, 100):
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div[7]/div/div[3]/button').click()
        except Exception as e:
            pass
        driver.save_screenshot(f'photo.png')
        print('lox2')
        time.sleep(500)
        driver.get(url)
        
def new_youtube(url):
    print(url)
    url=f'https://www.youtube.com/watch?v={url}'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("http://check.torproject.org")
    driver.save_screenshot(f'ip.png')
    driver.get(url)
    file1 = open('cockiestwitch/' + list_cockie[random.randint(1,len(list_cockie))], 'r')
    driver.delete_all_cookies()
    for item in file1:
        data = item.split('	')
        if url.find(data[0]) != -1:
            print(file1)
            value = data[6].replace(' ', '').replace('\r', '').replace('\n', '')
            cookie_dict = {
                'name': data[5],
                'value': value,
                "domain": data[0],  # google chrome
                "expires": data[4],
                'path': data[2],
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            driver.add_cookie(cookie_dict)
    driver.get(url)
    time.sleep(5)
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) #hits space
    time.sleep(1)
    video.click()   
    for i in range(0, 100):
        driver.save_screenshot(f'photo.png')
        print('lox2')
        time.sleep(500)
          
        
@app.route('/get_image')
def get_image():
    filename = 'ip.png'
    return send_file(filename, mimetype='image/png')

@app.route('/get_image2')
def get_image2():
    filename = 'photo.png'
    return send_file(filename, mimetype='image/png')

@app.route('/youtube/<url>')
def homepage_youtube(url):
    print(url)
    Thread(target=new_youtube,args=([url])).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)
@app.route('/<url>')
def homepage(url):
    print(url)
    Thread(target=new,args=([url])).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

