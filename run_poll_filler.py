#!/usr/bin/env python3

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import infos, poll_items

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
        
def fill_first_poll_page(browser):
    # opts = Options()
    # opts.set_headless()
    # assert opts.headless  # Operating in headless mode
    #browser = Firefox(options=opts)
    fill_infos(browser)
    set_poll_settings(browser)
    submit_button_infos_page = browser.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/form/p/button')
    submit_button_infos_page.click()    

def fill_second_poll_page(browser):
    items_list = []
    items_list = poll_items.create_item_list("Poll Filler/items.txt")
    for elt in items_list:
        print(f"out item name {elt.name} & item link {elt.image_link}")
    # TODO: check list size if it is superior to 5
    more_items = len(items_list) - 5
    if more_items > 0:
        # TODO: if superior click on + button on the page
        add_choice_button = browser.find_element_by_xpath('//*[@id="add-a-choice"]')
        remaining_items = more_items
        while remaining_items > 0:
            add_choice_button.click()
            remaining_items = remaining_items - 1
    for x in range(0,len(items_list)):
        id_string = "choice" + str(x)
        choice_form = browser.find_element_by_id(id_string)
        choice_form.send_keys(items_list[x].name)
        # TODO: fill the form with items names

    browser.find_element_by_xpath('/html/body/div[1]/main/form/div[1]/div/div[8]/button').click()
    browser.find_element_by_xpath('/html/body/div[3]/main/form/div/div/p/button[2]').click()
        
if __name__ == "__main__":
    browser = Firefox()
    browser.get('https://framadate.org/create_poll.php?type=autre')
    fill_first_poll_page(browser)
    fill_second_poll_page(browser)
