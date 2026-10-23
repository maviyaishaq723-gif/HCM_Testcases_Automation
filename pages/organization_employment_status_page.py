from pages.base_page import BasePage

class OrganizationEmploymentStatusPage(BasePage):
    EMPSTATUS_TAB = "a:has-text('Employment Status'), a[href*='/employment_statuses']"
    EMPSTATUS_BTN = "a:has-text('Create New Employment Status'), a[data-title*='Create New Employment Status']"
    NAME_INPUT = "input[placeholder='Enter Employment Status Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button, button:has-text('Create')"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_emp_status_tab(self):
        tab = self.page.locator(self.EMPSTATUS_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_emp_status_btn(self):
        btn = self.page.locator(self.EMPSTATUS_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_emp_status_form(self, status_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(status_name)
        self.page.wait_for_timeout(1000)

        create_btn = self.page.locator(self.CREATE_BTN).last
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        
        try:
            self.page.locator(self.MODAL_POPUP).wait_for(state="hidden", timeout=10000)
        except:
            pass
        
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)

    def verify_emp_status_created(self, status_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(status_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={status_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Employment Status create verify nahi ho saka!"