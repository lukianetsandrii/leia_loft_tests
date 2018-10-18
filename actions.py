import os
import time

from locators.search_locators import SearchLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction

import drivers


class Actions(drivers.Driver):

    def isObjectExistsID(self, driver, object):
        objects_list = driver.find_elements_by_id(object)

        if len(objects_list) < 1:
            return False
        elif len(objects_list) > 1:
            return False
        else:
            return True

    def isObjectExistsXP(self, driver, object):
        objects_list = driver.find_elements_by_xpath(object)

        if len(objects_list) < 1:
            return False
        elif len(objects_list) > 1:
            return False
        else:
            return True

    def getTextID(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        result_text = driver.find_element_by_id(locator).text

        return result_text

    def getTextXP(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        result_text = driver.find_element_by_xpath(locator).text

        return result_text

    def getAttributeValueID(self, driver, locator, attribute):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        attribute_value = driver.find_element_by_id(locator).get_attribute(attribute)

        return attribute_value

    def getAttributeValueXP(self, driver, locator, attribute):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        attribute_value = driver.find_element_by_xpath(locator).get_attribute(attribute)

        return attribute_value

    def getFewTextsID(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        elements_list = driver.find_elements_by_id(locator)
        texts_list = []
        for element in elements_list:
            text = element.text
            texts_list.append(text)
        return texts_list

    def getFewTextsXP(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        elements_list = driver.find_elements_by_xpath(locator)
        texts_list = []
        for element in elements_list:
            text = element.text
            texts_list.append(text)
        return texts_list

    def clickButtonID(self, driver, button):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, button)))
        some_button = driver.find_element_by_id(button)
        some_button.click()

    def clickButtonXP(self, driver, button):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button)))
        some_button = driver.find_element_by_xpath(button)
        some_button.click()

    def swipeSectionsToLeft(self, driver):
        driver.swipe(1200, 1950, 300, 1950, 500)
        time.sleep(1)

    def swipeSectionsToRight(self, driver):
        driver.swipe(300, 1950, 1200, 1950, 500)
        time.sleep(1)

    def swipeSliderToLeft(self, driver):
        driver.swipe(1200, 650, 300, 650, 500)
        time.sleep(1)

    def swipeSliderToRight(self, driver):
        driver.swipe(300, 650, 1200, 650, 500)
        time.sleep(1)

    def scrollPageToUp(self, driver):
        driver.swipe(100, 2000, 300, 200, 500)
        time.sleep(1)

    def is3DBacklightOn(self):
        is_on = False
        backlight_3d_int = int(os.popen('adb shell cat /sys/class/leds/LM36923H-BL/brightness').read())
        backlight_2d_int = int(os.popen('adb shell cat /sys/class/leds/lcd-backlight/brightness').read())
        if (backlight_2d_int < backlight_3d_int):
            is_on = True
        return is_on

    # def fill_field_id(self, driver):
    #     atime = str(time.clock())
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.POPUP_FIELD_XP)))
    #     field = driver.find_element_by_xpath(Locators.POPUP_FIELD_XP)
    #     field.send_keys(Locators.FOLDER_NAME_TEXT + atime)
    #
    # def version_text(self, driver):
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.VERSION_TEXT)))
    #     textik = driver.find_element_by_id(Locators.VERSION_TEXT).text
    #     version_text = textik[:8]
    #
    #     return version_text

    def count_of_elements_id(self, driver, element):
        elements_list = driver.find_elements_by_id(element)

        return len(elements_list)

    def longtap(self, driver, element):
        actions = TouchAction(driver)
        el = driver.find_element_by_xpath(element)
        actions.long_press(el)
        actions.perform()

    def search_field(self, driver):
         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, SearchLocators.SEARCH_FIELD_ID)))
         search_field = driver.find_element_by_id(SearchLocators.SEARCH_FIELD_ID)

         return search_field

    def get_attribute_value_from_element_id(self, driver, locator, attribute):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        element = driver.find_element_by_id(locator)
        attrib = element.get_attribute(attribute)

        return attrib



