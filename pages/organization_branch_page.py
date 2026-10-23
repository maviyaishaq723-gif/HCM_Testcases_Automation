from pages.base_page import BasePage

class OrganizationBranchPage(BasePage):
    CREATE_BRANCH_BTN = "a:has-text('Create New Branch')"
    MODAL_INPUT = "div.modal input[type='text'], div.modal-body input, form input[type='text'], input[name='name'], input[name='branch']"
    SAVE_BTN = "div.modal button:has-text('Create'), button[type='submit'], .btn-primary:has-text('Create')"
    SEARCH_INPUT = ".dataTable-input"

    def navigate_to_branch(self):
        """Organization Setup / Branch page par navigate karta hai"""
        self.page.goto("http://172.16.35.74/hcm/branch")
        self.page.wait_for_load_state("networkidle")

    def click_create_branch(self):
        """Create New Branch button click karke modal kholta hai"""
        btn = self.page.locator(self.CREATE_BRANCH_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_branch_form(self, branch_name):
        """Modal ke andar form fill karke Create button click karta hai"""
        input_box = self.page.locator(self.MODAL_INPUT).last
        input_box.wait_for(state="visible", timeout=10000)
        input_box.click()
        input_box.fill(branch_name)
        self.page.wait_for_timeout(1000)

        save_btn = self.page.locator(self.SAVE_BTN).last
        if save_btn.is_visible():
            save_btn.click()
        
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

    def verify_branch_created(self, branch_name):
        """Branch create hone ke baad search bar mein search karke verify karta hai"""
        search = self.page.locator(self.SEARCH_INPUT).first
        if search.is_visible():
            search.click()
            search.fill(branch_name)
            search.press("Enter")
            self.page.wait_for_timeout(3000)
        
        # Simple aur 100% reliable text locator
        branch_element = self.page.locator(f"text={branch_name}").first
        branch_element.wait_for(state="visible", timeout=15000)
        assert branch_element.is_visible(), "New branch create verify nahi ho saki!"