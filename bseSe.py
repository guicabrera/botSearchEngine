from selenium import webdriver
from selenium.webdriver.common.keys import Keys #lib to use key functions
from selenium.webdriver.support.select import Select #lib to use the select form from

"""
########################################################################################################
                                        Copy and Paste to test

        newbot = botSearchEngine(r"C:\driver\chromedriver.exe","https://www.google.com.br/")
        newbot.actionClick("ValueToSearch","actionType") 
        newbot.actionSendKeys(searchValue,actionType,keysToSend) --> actionType {
                                                                xpath,
                                                                class_name,
                                                                css_selector,
                                                                id,
                                                                link_text,
                                                                name,
                                                                partial_link_text,
                                                                tag_name
                                                                }
########################################################################################################
"""

class botSearchEngine:
    def __init__(self, driverPath,linkToFollow):
        try:
            self.__driver = webdriver.Chrome(driverPath)
            self.__driver.get(linkToFollow)
            self.__getElement = ""
        except:
            print("We Got an error trying to init the chromeDriver")
            quit()

    @property
    def getElement(self):
        return self.__getElement
    @property
    def driver(self):
        return self.__driver
    def performByArray(self):
        pass
    def setElement(self,searchValue,actionType):
        try:
            if(actionType.lower() ==  "xpath"):
                self.getElement = self.driver.find_element_by_xpath(searchValue)
            elif(actionType.lower() ==  "class_name"):
                self.getElement = self.driver.find_element_by_class_name(searchValue)
            elif(actionType.lower() ==  "css_selector"):
                self.getElement = self.driver.find_element_by_css_selector(searchValue)
            elif(actionType.lower() ==  "id"):
                self.getElement = self.driver.find_element_by_id(searchValue)
            elif(actionType.lower() ==  "link_text"):
                self.getElement = self.driver.find_element_by_link_text(searchValue)
            elif(actionType.lower() ==  "name"):
                self.getElement = self.driver.find_element_by_name(searchValue)
            elif(actionType.lower() ==  "partial_link_text"):
                self.getElement = self.driver.find_element_by_partial_link_text(searchValue)
            elif(actionType.lower() ==  "tag_name"):
                self.getElement = self.driver.find_element_by_tag_name(searchValue)
        except:
            print("Try again with valid Values on get element") 
    def actionClick(self,searchValue,actionType):
        #try:
        self.setElement(searchValue,actionType)
        self.getElement.click()
        #except:
           # print("Try again with valid Values on click")
    def actionSendKeys(self,searchValue,actionType,keysToSend):
        try:
            self.setElement(searchValue,actionType)
            self.getElement.send_keys(keysToSend)
        except:
            print("Try again with valid Values on click")
    def goBack(self):
        self.driver.execute_script("window.history.go(-1)")
    def go(self):
        self.driver.execute_script("window.history.go(1)")
    def finishBSE(self):
        self.driver.close()
        quit()

