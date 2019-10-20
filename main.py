from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/location/to/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
#webdriver.get('https://www.facebook.com/login')
webdriver.get('https://www.instagram.com/accounts/login/')

sleep(1)

username = webdriver.find_element_by_name('username')
username.send_keys('Your_username')
password = webdriver.find_element_by_name('password')
password.send_keys('Your_password')

"""
username = webdriver.find_element_by_name('email')
username.send_keys('your_email')
password = webdriver.find_element_by_name('pass')
password.send_keys('your_password')
"""
#button_login = webdriver.find_element_by_css_selector('#loginbutton')
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

sleep(40)

hashtag_list = ['drawings', 'travelblogger', 'traveler']
tag=0
likes=0
comments=0
for hashtag in hashtag_list:
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    tag += 1
    sleep(1)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first_thumbnail.click()
    sleep(randint(5, 10))
    try:
        for x in range(1, 10):
            button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
            likes+=1
            sleep(randint(10, 15))
            # Comments and tracker
            comm_prob = randint(1, 10)
            print('{}_{}: {}'.format(hashtag, x, comm_prob))
            if comm_prob > 7:
                comments += 1
                webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                comment_box = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                if (comm_prob < 7):
                    comment_box.send_keys('Really cool!')
                    sleep(1)
                elif comm_prob == 8:
                    comment_box.send_keys('Awesome work :)')
                    sleep(1)
                elif comm_prob == 9:
                    comment_box.send_keys('Nice gallery!!')
                    sleep(1)
                elif comm_prob == 10:
                    comment_box.send_keys('Nice work, Checkout my profile also :)')
                    sleep(1)
                # Enter to post comment
                comment_box.send_keys(Keys.ENTER)
                sleep(randint(5, 10))
                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(4, 10))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(5, 10))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
