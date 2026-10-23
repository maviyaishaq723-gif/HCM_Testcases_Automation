from pages.base_page import BasePage

class OrganizationGoalTypePage(BasePage):
    GOALTYPE_TAB = "a:has-text('Goal Type'), a[href*='/goaltype']"
    GOALTYPE_BTN = "a:has-text('Create New Goal Type'), a[data-title*='Create New Goal Type']"
    NAME_INPUT = "input[placeholder='Enter Goal Type Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_goal_type_tab(self):
        tab = self.page.locator(self.GOALTYPE_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_goal_type_btn(self):
        btn = self.page.locator(self.GOALTYPE_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_goal_type_form(self, goal_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(goal_name)
        self.page.wait_for_timeout(1000)

        create_btn = self.page.locator(self.CREATE_BTN).last
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        
        try:
            self.page.locator(self.MODAL_POPUP).wait_for(state="hidden", timeout=10000)
        except:
            pass
        
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def verify_goal_type_created(self, goal_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(goal_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={goal_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Goal Type create verify nahi ho saka!"