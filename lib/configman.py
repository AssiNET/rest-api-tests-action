# -*- coding: utf-8 -*- 

########################
### BUILD-IN IMPORTS ###
import os
import platform
import logging
import sys

##########################
######   SETTINGS   ######
sys.dont_write_bytecode = True # Disable .pyc file generation
logging.basicConfig(format='%(message)s',level=logging.INFO)

class ConfigMan(object):
    DEFAULT_RESPONSE_TIME = 3
    # SET Paths
    ROOT_DIR = os.getcwd() 
    TOOLS_DIR = os.path.join(ROOT_DIR, 'tools')
    CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
    CONTENT_DIR = os.path.join(ROOT_DIR, 'content')
    RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
    LATEST_DIR = os.path.join(RESULTS_DIR, 'latest')
    REPORT_HTML_FILE = os.path.join(ROOT_DIR, "index.html")
    REPORT_XML_FILE = os.path.join(ROOT_DIR, "report.xml")
    LATEST_RESULTS_DIR = "DIR NOT SET"
    TEST_SUITE_NAME = ""
    CURRENT_TESTS_DIR = ""
    BACKEND_URL = ''
