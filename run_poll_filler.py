#!/usr/bin/env python3

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from infos import Infos
import poll_items
import getopt
import sys


def fill_infos(browser, configuration):
    name_form = browser.find_element_by_id("yourname")
    name_form.send_keys(configuration.name)

    email_form = browser.find_element_by_id("email")
    email_form.send_keys(configuration.email)

    poll_title_form = browser.find_element_by_id("poll_title")
    poll_title_form.send_keys(configuration.poll_title)

    description_form = browser.find_element_by_id("poll_comments")
    description_form.send_keys(configuration.description)


def set_poll_settings(browser, configuration):
    facultative_settings_button = browser.find_element_by_xpath(
        "/html/body/div[3]/main/div[1]/div/form/div[7]/a"
    )
    facultative_settings_button.click()
    if configuration.people_can_only_modify_their_vote == True:
        browser.find_element_by_xpath(
            "/html/body/div[3]/main/div[1]/div/form/div[9]/div[4]/div/div/label[2]"
        ).click()
    if configuration.receive_mail_for_each_vote == True:
        browser.find_element_by_id("receiveNewVotes").click()
    if configuration.receive_mail_for_each_comment == True:
        browser.find_element_by_id("receiveNewComments").click()


def fill_first_poll_page(browser, configuration):
    # opts = Options()
    # opts.set_headless()
    # assert opts.headless  # Operating in headless mode
    # browser = Firefox(options=opts)
    fill_infos(browser, configuration)
    set_poll_settings(browser, configuration)
    submit_button_infos_page = browser.find_element_by_xpath(
        "/html/body/div[3]/main/div[1]/div/form/p/button"
    )
    submit_button_infos_page.click()


def fill_second_poll_page(browser, configuration):

    items_list = []
    items_list = poll_items.create_item_list(configuration.item_file)
    for elt in items_list:
        print(f"out item name {elt.name} & item link {elt.image_link}")
    more_items = len(items_list) - 5
    if more_items > 0:
        add_choice_button = browser.find_element_by_xpath('//*[@id="add-a-choice"]')
        remaining_items = more_items
        while remaining_items > 0:
            add_choice_button.click()
            remaining_items = remaining_items - 1
    for x in range(0, len(items_list)):
        id_string = "choice" + str(x)
        choice_form = browser.find_element_by_id(id_string)
        choice_form.send_keys(items_list[x].name)

    NEXT_BUTTON_XPATH = "//button[@name='fin_sondage_autre']"
    browser.find_element_by_xpath(NEXT_BUTTON_XPATH).click()
    # browser.find_element_by_xpath('/html/body/div[3]/main/form/div/div/p/button[2]').click()


def complete_poll_creation(browser):
    CREATE_POLL_BUTTON_XPATH = "//button[contains(text(),'Create the poll')]"
    browser.find_element_by_xpath(CREATE_POLL_BUTTON_XPATH).click()

def usage():
    print("No config file has been specified.\nRun the script this way :\npython run_poll_filler.py [--config=config_file.json]")

if __name__ == "__main__":
    # Use config.json as default config file
    config_file = 'config.json'
    # Get arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "config="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    # Parse arguments from configuration file
    for o, a in opts:
        if o in ('-c', '--config'):
            config_file=a
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
    configuration = Infos(config_file)
    browser = Firefox()
    browser.get("https://framadate.org/create_poll.php?type=autre")
    fill_first_poll_page(browser, configuration)
    fill_second_poll_page(browser, configuration)
    CREATE_POLL_BUTTON_XPATH = "//button[@name='confirmation']"
    browser.find_element_by_xpath(CREATE_POLL_BUTTON_XPATH).click()
