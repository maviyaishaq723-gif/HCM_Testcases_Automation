from pages.base_page import BasePage

class OrganizationContractTypePage(BasePage):
    CONTRACTTYPE_TAB = "a:has-text('Contract Type'), a[href*='/contract_type']"
    CONTRACTTYPE_BTN = "a:has-text('Create Contract'), a[data-title*='Create Contract']"
    NAME_INPUT = "input[placeholder='Enter Contract Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button, button:has-text('Create')"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_contract_type_tab(self):
        tab = self.page.locator(self.CONTRACTTYPE_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_contract_type_btn(self):
        btn = self.page.locator(self.CONTRACTTYPE_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_contract_type_form(self, contract_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(contract_name)
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

    def verify_contract_type_created(self, contract_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(contract_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={contract_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Contract Type create verify nahi ho saka!"