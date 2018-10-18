import time
from locators.main_locators import MainLocators
from locators.app_page_locators import AppPageLocators
from actions import Actions
from drivers import Driver as driver


class Test_Main_Page(driver, Actions):
    """
    Pre-conditions:


    Post-conditions:
    """

    # def test_slider_page_scroll(self, driver):
    #
    #     # Slider testing is works
    #     time.sleep(5)
    #     assert Actions.isObjectExistsID(self, driver, MainLocators.LOGO_ID) is True
    #
    #     # Test swipe to right
    #     slider_app_name_before_swipe = Actions.getTextID(self, driver, MainLocators.SLIDER_APP_NAME_ID)
    #     Actions.swipeSliderToRight(self, driver)
    #     slider_app_name_after_swipe = Actions.getTextID(self, driver, MainLocators.SLIDER_APP_NAME_ID)
    #
    #     assert slider_app_name_before_swipe != slider_app_name_after_swipe
    #
    #     # Test swipe to left
    #     Actions.swipeSliderToLeft(self, driver)
    #     Actions.swipeSliderToLeft(self, driver)
    #     Actions.swipeSliderToLeft(self, driver)
    #
    #     slider_app_name_after_after_swipe = Actions.getTextID(self, driver, MainLocators.SLIDER_APP_NAME_ID)
    #
    #     assert slider_app_name_after_after_swipe != slider_app_name_after_swipe
    #     assert  slider_app_name_after_after_swipe != slider_app_name_before_swipe
    #
    #     # Test open app page
    #     assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False
    #
    #     Actions.clickButtonID(self, driver, MainLocators.SLIDER_WHOLE_APP_BLOCK_ID)
    #
    #     assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is True
    #
    #     Actions.clickButtonID(self, driver, AppPageLocators.BACK_BUTTON_ID)
    #
    #     assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False
    #
    #     # Vertical scrolling testing
    #     assert Actions.isObjectExistsID(self, driver, MainLocators.SEARCH_BUTTON_ID) is True
    #     assert Actions.isObjectExistsID(self, driver, MainLocators.EDITOR_CHOICE_TITLE_ID) is False
    #
    #     Actions.scrollPageToUp(self, driver)
    #
    #     assert Actions.isObjectExistsID(self, driver, MainLocators.SEARCH_BUTTON_ID) is False
    #     assert Actions.isObjectExistsID(self, driver, MainLocators.EDITOR_CHOICE_TITLE_ID) is True

    def test_top_picks_editors_choice_blocks(self, driver):
        # Top picks block swipe
        assert Actions.getTextID(self, driver, MainLocators.TOP_PICKS_TITLE_ID) == 'Top Picks'
        assert Actions.getFewTextsXP(self, driver, MainLocators.OVERALL_TABS_XP) == ['Games', 'Apps']
        # assert Actions.getAttributeValueXP(self, driver, MainLocators.FIRST_TAB_XP, 'selected') == 'true'
        # assert Actions.getAttributeValueXP(self, driver, MainLocators.SECOND_TAB_XP, 'selected') == 'false'
        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 7
        assert Actions.count_of_elements_id(self, driver, MainLocators.SUBTITLE_APP_ID) == 7

        Actions.swipeSectionsToLeft(self, driver)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 4
        assert Actions.count_of_elements_id(self, driver, MainLocators.SUBTITLE_APP_ID) >= 4

        Actions.swipeSectionsToRight(self, driver)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 7
        assert Actions.count_of_elements_id(self, driver, MainLocators.SUBTITLE_APP_ID) == 7

        # Top picks block click
        Actions.clickButtonXP(self, driver, MainLocators.SECOND_TAB_XP)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 4
        assert Actions.count_of_elements_id(self, driver, MainLocators.SUBTITLE_APP_ID) >= 4

        Actions.clickButtonXP(self, driver, MainLocators.FIRST_TAB_XP)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 7
        assert Actions.count_of_elements_id(self, driver, MainLocators.SUBTITLE_APP_ID) == 7

        # Test open app page from top picks block
        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False

        Actions.clickButtonXP(self, driver, MainLocators.APP_TO_OPEN_TOP_PICKS_XP)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is True

        Actions.clickButtonID(self, driver, AppPageLocators.BACK_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False

        Actions.scrollPageToUp(self, driver)

        # Editor's choice block swipe
        assert Actions.getFewTextsXP(self, driver, MainLocators.OVERALL_TABS_XP) == ['Games', 'Apps', 'Games', 'Apps']

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 13

        Actions.swipeSectionsToLeft(self, driver)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 10

        Actions.swipeSectionsToRight(self, driver)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 13

        # Editor's choice block click
        Actions.clickButtonXP(self, driver, MainLocators.FOURTH_TAB_XP)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 10

        Actions.clickButtonXP(self, driver, MainLocators.THIRD_TAB_XP)

        assert Actions.count_of_elements_id(self, driver, MainLocators.APP_ICON_ID) == 13

        # Test open app page from editors choice  block
        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False

        Actions.clickButtonXP(self, driver, MainLocators.APP_TO_OPEN_EDITORS_CHOICE_XP)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is True

        Actions.clickButtonID(self, driver, AppPageLocators.BACK_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, AppPageLocators.GALLERY_BLOCK_ID) is False
