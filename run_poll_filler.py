#!/usr/bin/env python3

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import infos

def fill_infos(browser):
    name_form = browser.find_element_by_id('yourname')
    name_form.send_keys(infos.name)
    
    email_form = browser.find_element_by_id('email')
    email_form.send_keys(infos.email)
    
    poll_title_form = browser.find_element_by_id('poll_title')
    poll_title_form.send_keys(infos.poll_title)
    
    description_form = browser.find_element_by_id('poll_comments')
    description_form.send_keys(infos.Description)
    

def set_poll_settings(browser):
    facultative_settings_button = browser.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/form/div[7]/a')
    facultative_settings_button.click()
    if(infos.people_can_only_modify_their_vote == True):
        browser.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/form/div[9]/div[4]/div/div/label[2]').click()
    if(infos.receive_mail_for_each_vote == True):
        browser.find_element_by_id('receiveNewVotes').click()
    if(infos.receive_mail_for_each_comment == True):
        browser.find_element_by_id('receiveNewComments').click()
        



def fill_first_poll_page():
    # opts = Options()
    # opts.set_headless()
    # assert opts.headless  # Operating in headless mode
    #browser = Firefox(options=opts)
    browser = Firefox()
    browser.get('https://framadate.org/create_poll.php?type=autre')
    fill_infos(browser)
    set_poll_settings(browser)
    submit_button_infos_page = browser.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/form/p/button')
    submit_button_infos_page.click()    



if __name__ == "__main__":
    fill_first_poll_page()
