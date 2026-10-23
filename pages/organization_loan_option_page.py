from pages.base_page import BasePage

class OrganizationLoanOptionPage(BasePage):
    LOANOPTION_TAB = "a:has-text('Loan Option'), a[href*='/loanoption']"
    LOANOPTION_BTN = "a:has-text('Create New Loan Option'), a[data-title*='Create New Loan Option']"
    NAME_INPUT = "input[placeholder='Enter Loan Option Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_loan_option_tab(self):
        tab = self.page.locator(self.LOANOPTION_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_loan_option_btn(self):
        btn = self.page.locator(self.LOANOPTION_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_loan_option_form(self, loan_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(loan_name)
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

    def verify_loan_option_created(self, loan_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(loan_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={loan_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Loan Option create verify nahi ho saka!"