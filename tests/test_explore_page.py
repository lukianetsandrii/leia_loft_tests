import time

from locators.main_locators import MainLocators
from locators.search_locators import SearchLocators
from locators.app_page_locators import AppPageLocators
from locators.explore_page_locators import ExplorePageLocators

from static_data import StaticData

from actions import Actions
from drivers import Driver as driver


class Test_Expllore_Page(driver, Actions):
    """
    Pre-conditions:


    Post-conditions:
    """

    def test_explore_page_view(self, driver):
        time.sleep(2)
        Actions.clickButtonXP(self, driver, MainLocators.EXPLORE_BUTTON_XP)

        assert Actions.getTextXP(self, driver, ExplorePageLocators.TITLE_XP) == StaticData.EXPLORE_PAGE_TITLE
        assert Actions.isObjectExistsID(self, driver, ExplorePageLocators.SEARCH_BUTTON_ID) is True
        assert Actions.isObjectExistsID(self, driver, ExplorePageLocators.SORT_BUTTON_ID) is True
        assert Actions.isObjectExistsID(self, driver, ExplorePageLocators.MENU_BUTTON_ID) is True
        assert Actions.getTextXP(self, driver,
                                 ExplorePageLocators.GAMES_TAB_XP) == StaticData.EXPLORE_PAGE_GAMES_TAB_NAME
        assert Actions.getTextXP(self, driver,
                                 ExplorePageLocators.APPS_TAB_XP) == StaticData.EXPLORE_PAGE_APPS_TAB_NAME

        assert Actions.getAttributeValueXP(self, driver, ExplorePageLocators.GAMES_TAB_XP, 'selected') == StaticData.EXPLORE_PAGE_GAMES_TAB_SELECTED
        assert Actions.getAttributeValueXP(self, driver, ExplorePageLocators.APPS_TAB_XP,
                                           'selected') == StaticData.EXPLORE_PAGE_APPS_TAB_NOT_SELECTED
