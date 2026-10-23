from pages.base_page import BasePage

class OrganizationTrainingTypePage(BasePage):
    TRAININGTYPE_TAB = "a:has-text('Training Type'), a[href*='/trainingtype']"
    TRAININGTYPE_BTN = "a:has-text('Create New Training Type'), a[data-title*='Create New Training Type']"
    NAME_INPUT = "input[placeholder='Enter Traning Type Name'], input[placeholder='Enter Training Type Name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_training_type_tab(self):
        tab = self.page.locator(self.TRAININGTYPE_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_training_type_btn(self):
        btn = self.page.locator(self.TRAININGTYPE_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_training_type_form(self, training_name):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(training_name)
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

    def verify_training_type_created(self, training_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(training_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={training_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Training Type create verify nahi ho saka!"