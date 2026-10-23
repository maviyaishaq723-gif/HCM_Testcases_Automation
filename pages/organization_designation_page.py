from pages.base_page import BasePage

class OrganizationDesignationPage(BasePage):
    DESIGNATION_TAB = "a:has-text('Designation')"
    ADD_DESIGNATION_BTN = "a:has-text('Create New Designation'), a[data-title*='Create New Designation']"
    MODAL_INPUT = "div.modal input[type='text'], input[placeholder='Enter Designation Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create']"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_designation_tab(self):
        self.page.locator(self.DESIGNATION_TAB).first.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_designation_btn(self):
        btn = self.page.locator(self.ADD_DESIGNATION_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_designation_form(self, desig_name):
        try:
            # Choices.js dropdown container click
            dropdown_box = self.page.locator("div.modal div.choices, div.modal div.choices__inner").first
            dropdown_box.click()
            self.page.wait_for_timeout(1000)
            
            # Select valid option
            option = self.page.locator(".choices__item--choice:not(.is-selected)").first
            option.click()
            self.page.wait_for_timeout(1000)
        except Exception as e:
            print(f"Designation dropdown selection error: {e}")

        input_box = self.page.locator(self.MODAL_INPUT).last
        input_box.wait_for(state="visible", timeout=10000)
        input_box.click()
        input_box.fill(desig_name)
        self.page.wait_for_timeout(1000)

        # Create submit button force click
        create_btn = self.page.locator(self.CREATE_BTN).last
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        
        try:
            self.page.locator(self.MODAL_POPUP).wait_for(state="hidden", timeout=10000)
        except:
            pass
        
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def verify_designation_created(self, desig_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(desig_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={desig_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Designation create verify nahi ho saka!"