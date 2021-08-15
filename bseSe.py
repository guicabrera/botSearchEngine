from selenium import webdriver
from selenium.webdriver.common.keys import Keys #lib to use key functions
from selenium.webdriver.support.select import Select #lib to use the select form from


class botSearchEngine:
    def __init__(self, driverPath,linkToFollow):
        try:
            self.driver = webdriver.Chrome(driverPath)
            self.driver.get(linkToFollow)
        except:
            print("We Got an error trying to init the chromeDriver")
            quit()
    
    
    def performByArray(self):
        pass
    
    def actionClick(self,searchValue,actionType):
        try:
            if(actionType.lower() ==  "xpath"):
                self.driver.find_element_by_xpath(searchValue).click()
            elif(actionType.lower() ==  "class_name"):
                self.driver.find_element_by_class_name(searchValue).click()
            elif(actionType.lower() ==  "css_selector"):
                self.driver.find_element_by_css_selector(searchValue).click()
            elif(actionType.lower() ==  "id"):
                self.driver.find_element_by_id(searchValue).click()
            elif(actionType.lower() ==  "link_text"):
                self.driver.find_element_by_link_text(searchValue).click()
            elif(actionType.lower() ==  "name"):
                self.driver.find_element_by_name(searchValue).click()
            elif(actionType.lower() ==  "partial_link_text"):
                self.driver.find_element_by_partial_link_text(searchValue).click()
            elif(actionType.lower() ==  "tag_name"):
                self.driver.find_element_by_tag_name(searchValue).click()
        except:
            print("Try again with valid Values")
    def actionSendKeys(self,searchValue,actionType,keysToSend):
        try:
            if(actionType.lower() ==  "xpath"):
                self.driver.find_element_by_xpath(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "class_name"):
                self.driver.find_element_by_class_name(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "css_selector"):
                self.driver.find_element_by_css_selector(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "id"):
                self.driver.find_element_by_id(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "link_text"):
                self.driver.find_element_by_link_text(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "name"):
                self.driver.find_element_by_name(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "partial_link_text"):
                self.driver.find_element_by_partial_link_text(searchValue).send_keys(keysToSend)
            elif(actionType.lower() ==  "tag_name"):
                self.driver.find_element_by_tag_name(searchValue).send_keys(keysToSend)
        except:
            print("Try again with valid values")
    def finishBSE(self):
        self.driver.close()
        quit()

