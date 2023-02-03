# -*- coding: utf-8 -*- 

########################
### BUILD-IN IMPORTS ###
import os
import shutil
import time
import datetime
import logging
import sys
import requests

##########################
######   SETTINGS   ######
logging.basicConfig(format='%(message)s',level=logging.INFO)
sys.dont_write_bytecode = True # Disable .pyc file generation

class File(object):
    @classmethod
    def get_file_content(cls, file_path, mode='r'):
        file_content = ""
        f = open(file_path, mode)
        file_content = f.read()
        f.close()
        return file_content

class Reporting(object):
    @classmethod
    def test_log(cls, message):
        '''Print info in the Report.html, Console output'''
        label_timestamp = "[" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S] TEST_LOG: ')
        #non_ascii_message = String.remove_non_ascii_char(message)

        # print in console
        message_console = str(label_timestamp) + str(message)
        logging.info(message_console)
        
        # print in Report.html
        message_report_html = str(label_timestamp) + str(message) # May need to use RemoveNonASCIIchar function
        print(message_report_html)

class Network(object):
    @classmethod
    def download_file(cls, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            r = requests.get(download_url, allow_redirects=True)
            with open(destination, 'wb') as dl_file:
                dl_file.write(r.content)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))

class String(object):
    @classmethod
    def remove_non_ascii_char(cls, text):
        '''Removes chars>128'''
        if isinstance(text, (int, int)):
            text = str(text)

        return ''.join([i if ord(i) < 128 else '*' for i in text])

    @classmethod
    def get_string_in_between(self, str_source, str_left, str_right):
        '''Easy way to extract value from string by giving left and right strings to the one you are searching'''
        start = str_source.find(str_left) + len(str_left)
        end = str_source.find(str_right)
        substring = str_source[start:end]
        return substring

    @classmethod
    def get_line_by_str(self, source_str, find_str):
        for row in source_str.split("\n"):
            if find_str in row:
                return row

    @classmethod
    def get_next_line_by_str(self, source_str, find_str):
        '''
        Split all string by new line
        Find desird line from find_str and return the next line
        '''
        source_str_no_empty_lines = String.remove_blank_lines(source_str)
        is_found = False
        for row in source_str_no_empty_lines.split("\n"):
            if is_found:
                return row
            if find_str in row:
                is_found = True

    @classmethod
    def get_custom_next_line_by_str(cls, source_str, find_str, custom_next_line_number):
        counter = 999999

        for row in source_str.split("\n"):
            if find_str in row:
                counter = 0

            if counter == custom_next_line_number:
                return row

            counter += 1

    @classmethod
    def get_previous_line_by_str(self, source_str, find_str):
        '''
        Split all string by new line
        Find desird line from find_str and return the previous line
        '''
        source_str_no_empty_lines = String.remove_blank_lines(source_str)

        previous_row = "emty prevous row"
        for row in source_str_no_empty_lines.split("\n"):
            if find_str in row:
                print("Previous row: " + str(previous_row))
                return previous_row
            previous_row = row

    @classmethod
    def remove_blank_lines(cls, source_str):
        text = source_str.replace("\n\n", "\n")
        return text


