from selenium import webdriver
from selenium.webdriver.common.keys import Keys #lib to use key functions
from selenium.webdriver.support.select import Select #lib to use the select form from


class botSearchEngine:
    def __init__(self, driverPath,linkToFollow):
        try:
            self.driver = webdriver.Chrome(driverPath)
            self.driver.get(linkToFollow)
            self.element = ""
        except:
            print("We Got an error trying to init the chromeDriver")
            quit()
    
    
    def performByArray(self):
        pass
    def getElement(self,searchValue,actionType):
        try:
            if(actionType.lower() ==  "xpath"):
                self.element = self.driver.find_element_by_xpath(searchValue)
            elif(actionType.lower() ==  "class_name"):
                self.element = self.driver.find_element_by_class_name(searchValue)
            elif(actionType.lower() ==  "css_selector"):
                self.element = self.driver.find_element_by_css_selector(searchValue)
            elif(actionType.lower() ==  "id"):
                self.element = self.driver.find_element_by_id(searchValue)
            elif(actionType.lower() ==  "link_text"):
                self.element = self.driver.find_element_by_link_text(searchValue)
            elif(actionType.lower() ==  "name"):
                self.element = self.driver.find_element_by_name(searchValue)
            elif(actionType.lower() ==  "partial_link_text"):
                self.element = self.driver.find_element_by_partial_link_text(searchValue)
            elif(actionType.lower() ==  "tag_name"):
                self.element = self.driver.find_element_by_tag_name(searchValue)
        except:
            print("Try again with valid Values on get element") 
    def actionClick(self,searchValue,actionType):
        try:
            self.getElement(searchValue,actionType)
            self.element.click()
        except:
            print("Try again with valid Values on click")
    def actionSendKeys(self,searchValue,actionType,keysToSend):
        try:
            self.getElement(searchValue,actionType)
            self.element.send_keys(keysToSend)
        except:
            print("Try again with valid Values on click")
    def finishBSE(self):
        self.driver.close()
        quit()

