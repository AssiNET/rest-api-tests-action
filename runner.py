# -*- coding: utf-8 -*- 

########################
### BUILD-IN IMPORTS ###
import sys
import os
import time
import datetime
import shutil
import argparse
import logging
import xml.etree.ElementTree as ET
from distutils.dir_util import copy_tree

#########################
### FRAMEWORK IMPORTS ###
from lib.common_lib import Reporting
from lib.configman import ConfigMan

##########################
######   SETTINGS   ######
sys.dont_write_bytecode = True # Disable .pyc file generation
logging.basicConfig(format='%(message)s',level=logging.INFO)

class Runner(object):
    @classmethod
    def run_test_set(cls, test_set):
            test_set_path = os.path.join("tests", test_set + ".py")
            logging.info("")
            logging.info("Module Path: " + str(test_set_path))
            logging.info("")

            command = "pytest " + test_set_path + " --html=index.html --self-contained-html --capture=tee-sys --junitxml=report.xml -v --color=yes"
 
            logging.info("###########################")
            logging.info("######### COMMAND #########")
            logging.info(command)
            logging.info("########### END ###########")
            os.system(command)

    @classmethod
    def clean_latest_folder(cls, destination):
        # Delete latest dir and last reports
        if os.path.exists(destination):
            shutil.rmtree(destination)
            os.mkdir(destination)
        else:
            os.mkdir(destination)

    @classmethod
    def create_result_dir(cls, test_suite_name):
        if not DEBUG:
            if not os.path.exists(ConfigMan.RESULTS_DIR):
                os.mkdir(ConfigMan.RESULTS_DIR)

            timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_"))
            latest_results_dir_name = timestamp + test_suite_name
            latest_results_dir_path = os.path.join(ConfigMan.ROOT_DIR, ConfigMan.RESULTS_DIR, latest_results_dir_name)
            os.mkdir(latest_results_dir_path)
            return latest_results_dir_path

    @classmethod
    def copy_results(cls, destination):
        print("Copy Results to: " + destination)

        # Delete latest dir and last reports
        if os.path.exists(destination):
            shutil.rmtree(destination)
            os.mkdir(destination)
        else:
            os.mkdir(destination)

        # HTML
        if os.path.exists(ConfigMan.REPORT_HTML_FILE):
            shutil.move(ConfigMan.REPORT_HTML_FILE, destination)

        # XML
        if os.path.exists(ConfigMan.REPORT_XML_FILE):
            shutil.move(ConfigMan.REPORT_XML_FILE, destination)

    @classmethod
    def get_exit_code(cls, result_file_path):
        tree = ET.parse(result_file_path)  # Parse XML Report
        root = tree.getroot()  # Get root of XML Report
        test_suite = root[0] # Get Test Suite

        if test_suite.attrib['failures'] > '0' or test_suite.attrib['errors'] > '0': 
            return 1
        else:
            return 0

    @classmethod
    def set_exit_code(cls, exit_code):
        if (exit_code == 0):
            logging.info(" Set Exit Code: No errors or failures - exit(0) ")
            exit(0)
        else:
            logging.info(" Set Exit Code: Found errors or failures - exit(1) ")
            exit(1)

if __name__ == '__main__':
    #####################
    ####  ARGUMENTS  ####
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", help="Add Test Set Name")
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args()

    ConfigMan.TEST_SUITE_NAME = args.set
    DEBUG = args.debug # default is False
    ######################
    ConfigMan.CURRENT_TESTS_DIR = os.path.join(ConfigMan.ROOT_DIR, 'tests', ConfigMan.TEST_SUITE_NAME)
    ConfigMan.LATEST_RESULTS_DIR = Runner.create_result_dir(ConfigMan.TEST_SUITE_NAME)

    #####################
    ### PRECONDITIONS ###
    Runner.clean_latest_folder(ConfigMan.LATEST_DIR)

    ###########################################################
    Runner.run_test_set(ConfigMan.CURRENT_TESTS_DIR) # !!! RUN THE TEST !!!
    ###########################################################

    ######################
    ### POSTCONDITIONS ###
    exit_code = Runner.get_exit_code(ConfigMan.REPORT_XML_FILE)
    test_result_statuses = Runner.get_exit_code(ConfigMan.REPORT_XML_FILE)
    Runner.copy_results(ConfigMan.LATEST_RESULTS_DIR)
    copy_tree(ConfigMan.LATEST_RESULTS_DIR, ConfigMan.LATEST_DIR)
    Runner.set_exit_code(exit_code)
