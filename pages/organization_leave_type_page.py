from pages.base_page import BasePage

class OrganizationLeaveTypePage(BasePage):
    LEAVETYPE_TAB = "a:has-text('Leave Type'), a[href*='/leavetype']"
    ADD_LEAVETYPE_BTN = "a:has-text('Create New Leave Type'), a[data-title*='Create New Leave Type']"
    NAME_INPUT = "input[placeholder='Enter Leave Type Name']"
    DAYS_INPUT = "input[placeholder='Enter Days / Year']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_leave_type_tab(self):
        tab = self.page.locator(self.LEAVETYPE_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_leave_type_btn(self):
        btn = self.page.locator(self.ADD_LEAVETYPE_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_leave_type_form(self, leave_name, days_val="90"):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(leave_name)
        self.page.wait_for_timeout(1000)

        days_box = self.page.locator(self.DAYS_INPUT).first
        days_box.wait_for(state="visible", timeout=10000)
        days_box.click()
        days_box.fill(str(days_val))
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

    def verify_leave_type_created(self, leave_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(leave_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={leave_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Leave Type create verify nahi ho saka!"