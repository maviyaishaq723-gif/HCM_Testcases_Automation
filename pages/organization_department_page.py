from pages.base_page import BasePage

class OrganizationDepartmentPage(BasePage):
    DEPT_TAB = "a:has-text('Department')"
    SUB_DEPT_TAB = "a:has-text('Sub Department')"
    
    ADD_DEPT_BTN = "a:has-text('Create New Department'), a:has-text('Add')"
    ADD_SUB_DEPT_BTN = "a:has-text('Create New Sub Department'), a:has-text('Add')"
    
    MODAL_INPUT = "div.modal input[type='text'], input[name='name'], input[name='sub_department_name']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create']"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_department_tab(self):
        self.page.locator(self.DEPT_TAB).first.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def click_add_department_btn(self):
        btn = self.page.locator(self.ADD_DEPT_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_department_form(self, dept_name):
        try:
            # Choices.js dropdown container par click karein taake list khul jaye
            dropdown_box = self.page.locator("div.modal div.choices, div.modal div.choices__inner").first
            dropdown_box.click()
            self.page.wait_for_timeout(1000)
            
            # Choices.js ki valid option select karein
            option = self.page.locator(".choices__item--choice:not(.is-selected)").first
            option.click()
            self.page.wait_for_timeout(1000)
        except Exception as e:
            print(f"Dropdown selection error: {e}")

        input_box = self.page.locator(self.MODAL_INPUT).last
        input_box.wait_for(state="visible", timeout=10000)
        input_box.click()
        input_box.fill(dept_name)
        self.page.wait_for_timeout(1000)

        # Create submit input button ko force click karein[cite: 16]
        create_btn = self.page.locator(self.CREATE_BTN).last
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        
        try:
            self.page.locator(self.MODAL_POPUP).wait_for(state="hidden", timeout=10000)
        except:
            pass
        
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def verify_department_created(self, dept_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(dept_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={dept_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Department create verify nahi ho saka!"

    def click_sub_department_tab(self):
        try:
            cancel_btn = self.page.locator("div.modal button:has-text('Cancel'), div.modal button.btn-close").first
            if cancel_btn.is_visible():
                cancel_btn.click()
                self.page.wait_for_timeout(1000)
        except:
            pass

        sub_tab = self.page.locator(self.SUB_DEPT_TAB).first
        sub_tab.wait_for(state="visible", timeout=15000)
        sub_tab.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def click_add_sub_department_btn(self):
        btn = self.page.locator(self.ADD_SUB_DEPT_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_sub_department_form(self, subdept_name):
        try:
            # Choices.js dropdown container par click karein taake list khul jaye
            dropdown_box = self.page.locator("div.modal div.choices, div.modal div.choices__inner").first
            dropdown_box.click()
            self.page.wait_for_timeout(1000)
            
            # Choices.js ki valid option select karein
            option = self.page.locator(".choices__item--choice:not(.is-selected)").first
            option.click()
            self.page.wait_for_timeout(1000)
        except Exception as e:
            print(f"Sub Department dropdown selection error: {e}")

        input_box = self.page.locator(self.MODAL_INPUT).last
        input_box.wait_for(state="visible", timeout=10000)
        input_box.click()
        input_box.fill(subdept_name)
        self.page.wait_for_timeout(1000)

        # Create submit input button ko force click karein[cite: 16]
        create_btn = self.page.locator(self.CREATE_BTN).last
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        
        try:
            self.page.locator(self.MODAL_POPUP).wait_for(state="hidden", timeout=10000)
        except:
            pass
        
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def verify_sub_department_created(self, subdept_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(subdept_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={subdept_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Sub Department create verify nahi ho saka!"