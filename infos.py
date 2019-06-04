#!/usr/bin/env python3
import json, sys

class Infos:
    def missing_key(self, key):
        print("key {} is missing in configuration file".format(key))
        sys.exit(-1)

    def __init__(self, file):
        with open(file) as json_configuration:
            data = json.load(json_configuration)
            if not 'name' in data:
                self.missing_key('name')
            self.name = data['name']
            if not 'email' in data:
                self.missing_key('email')
            self.email = data['email']
            if not 'poll_title' in data:
                self.missing_key('poll_title')
            self.poll_title = data['poll_title']
            if not 'description' in data:
                self.missing_key('description')
            self.description = data['description']
            if not 'people_can_only_modify_their_vote' in data:
                self.missing_key('people_can_only_modify_their_vote')
            self.people_can_only_modify_their_vote = data['people_can_only_modify_their_vote']
            if not 'receive_mail_for_each_vote' in data:
                self.missing_key('receive_mail_for_each_vote')
            self.receive_mail_for_each_vote = data['receive_mail_for_each_vote']
            if not 'receive_mail_for_each_comment' in data:
                self.missing_key('receive_mail_for_each_comment')
            self.receive_mail_for_each_comment = data['receive_mail_for_each_comment']
            if not 'use_image_instead_of_text' in data:
                self.missing_key('use_image_instead_of_text')
            self.use_image_instead_of_text = data['use_image_instead_of_text']
            if not 'language' in data:
                self.missing_key('language')
            self.language = data['language']
            if not 'item_file' in data:
                self.missing_key('item_file')
            self.item_file = data['item_file']

    