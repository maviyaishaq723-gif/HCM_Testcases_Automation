from pages.base_page import BasePage

class OrganizationFiscalYearPage(BasePage):
    FISCALYEAR_TAB = "a:has-text('Fiscal Year'), a[href*='/fiscal-years']"
    FISCALYEAR_BTN = "a:has-text('Create New Fiscal Year'), a[data-title*='Create New Fiscal Year']"
    NAME_INPUT = "input[placeholder='Enter Fiscal Year']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button, button:has-text('Create')"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_fiscal_year_tab(self):
        tab = self.page.locator(self.FISCALYEAR_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_fiscal_year_btn(self):
        btn = self.page.locator(self.FISCALYEAR_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_fiscal_year_form(self, fiscal_year_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(fiscal_year_name)
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

    def verify_fiscal_year_created(self, fiscal_year_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        if search.is_visible():
            search.click()
            search.fill(fiscal_year_name)
            search.press("Enter")
            self.page.wait_for_timeout(2000)
        
        element = self.page.locator(f"text={fiscal_year_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Fiscal Year create verify nahi ho saka!"