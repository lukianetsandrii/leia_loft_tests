import time

from locators.main_locators import MainLocators
from locators.search_locators import SearchLocators
from locators.app_page_locators import AppPageLocators

from static_data import StaticData

from actions import Actions
from drivers import Driver as driver


class Test_Search_Page(driver, Actions):
    """
    Pre-conditions:


    Post-conditions:
    """

    def test_search(self, driver):
        Actions.clickButtonID(self, driver, MainLocators.SEARCH_BUTTON_ID)

        # Check first part of word
        Actions.search_field(self, driver).set_value(StaticData.FIRST_PART_OF_WORD)
        time.sleep(2)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is True

        first_autocomplete_result_name = Actions.getTextXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP)
        assert first_autocomplete_result_name == StaticData.RED_PLAYER_NAME

        assert Actions.count_of_elements_id(self, driver, SearchLocators.RESULTS_APP_COVER_IMAGE) == 0

        driver.long_press_keycode(66)

        assert Actions.count_of_elements_id(self, driver, SearchLocators.RESULTS_APP_COVER_IMAGE) == 3

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is False
        assert Actions.isObjectExistsXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP) is False
        # TODO assert Actions.isObjectExistsID() check more than 1 result

        # Check middle part of word
        Actions.search_field(self, driver).set_value(StaticData.MIDDLE_PART_OF_WORD)
        time.sleep(2)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is True

        first_autocomplete_result_name = Actions.getTextXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP)
        assert first_autocomplete_result_name == StaticData.RED_PLAYER_NAME

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is False
        assert Actions.isObjectExistsXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP) is False
        # TODO check that 1 result

        # Check end part of word
        Actions.search_field(self, driver).set_value(StaticData.END_PART_OF_WORD)
        time.sleep(2)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is True

        first_autocomplete_result_name = Actions.getTextXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP)
        assert first_autocomplete_result_name == StaticData.RED_PLAYER_NAME

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is False
        assert Actions.isObjectExistsXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP) is False
        # TODO check that 1 result

        # Check two symbols - no results
        Actions.search_field(self, driver).set_value(StaticData.TWO_SYMBOLS)

        assert Actions.count_of_elements_id(self, driver, SearchLocators.APP_NAME_ID) == 0

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

        # Check more than 3 symbols
        Actions.search_field(self, driver).set_value(StaticData.SIX_SYMBOLS)

        assert Actions.isObjectExistsID(self, driver, SearchLocators.RED_PLAYER_ICON_ID) is True

        first_autocomplete_result_name = Actions.getTextXP(self, driver, SearchLocators.RED_PLAYER_NAME_XP)
        assert first_autocomplete_result_name == StaticData.RED_PLAYER_NAME
        assert Actions.count_of_elements_id(self, driver, SearchLocators.APP_NAME_ID) == 1

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

        # Check not existing app
        Actions.search_field(self, driver).set_value(StaticData.NOT_EXISTING_APP)

        assert Actions.count_of_elements_id(self, driver, SearchLocators.APP_NAME_ID) == 0

        Actions.clickButtonID(self, driver, SearchLocators.CLEAR_FIELD_BUTTON_ID)

    def test_open_app_page(self, driver):
        Actions.clickButtonID(self, driver, MainLocators.SEARCH_BUTTON_ID)

        # Check "<-" button
        Actions.clickButtonID(self, driver, SearchLocators.BACK_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, MainLocators.LOGO_ID) is True

        Actions.clickButtonID(self, driver, MainLocators.SEARCH_BUTTON_ID)

        # Check placeholder
        search_field_text = Actions.getTextID(self, driver, SearchLocators.SEARCH_FIELD_ID)

        assert search_field_text[0:6] == StaticData.SEARCH_FIELD_TEXT

        # Open app from autocomplete results
        Actions.search_field(self, driver).set_value(StaticData.FIRST_PART_OF_WORD)
        time.sleep(2)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False

        Actions.clickButtonID(self, driver, SearchLocators.RED_PLAYER_ICON_ID)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is True

        Actions.clickButtonID(self, driver, AppPageLocators.BACK_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False

        # Open app from general results
        driver.long_press_keycode(66)

        Actions.clickButtonID(self, driver, SearchLocators.RESULTS_APP_COVER_IMAGE)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is True

        Actions.clickButtonID(self, driver, AppPageLocators.BACK_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False
