from pages.base_page import BasePage

class OrganizationJobSetupPage(BasePage):
    # Selectors for Job Category
    JOBCATEGORY_TAB = "a:has-text('Job Category'), a[href*='/job-category']"
    JOBCATEGORY_BTN = "a:has-text('Create New Job Category'), a[data-title*='Create New Job Category']"
    JOBCATEGORY_NAME_INPUT = "input[placeholder='Enter Category Title']"

    # Selectors for Job Stage
    JOBSTAGE_TAB = "a:has-text('Job Stage'), a[href*='/job-stage']"
    JOBSTAGE_BTN = "a:has-text('Create New Job Stage'), a[data-title*='Create New Job Stage']"
    JOBSTAGE_NAME_INPUT = "input[placeholder='Enter Stage Title']"

    # Common Selectors
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    # --- Job Category Methods ---
    def click_job_category_tab(self):
        tab = self.page.locator(self.JOBCATEGORY_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_job_category_btn(self):
        btn = self.page.locator(self.JOBCATEGORY_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_job_category_form(self, category_name):
        name_box = self.page.locator(self.JOBCATEGORY_NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(category_name)
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

    def verify_job_category_created(self, category_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(category_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={category_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Job Category create verify nahi ho saka!"

    # --- Job Stage Methods ---
    def click_job_stage_tab(self):
        tab = self.page.locator(self.JOBSTAGE_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_job_stage_btn(self):
        btn = self.page.locator(self.JOBSTAGE_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_job_stage_form(self, stage_name):
        name_box = self.page.locator(self.JOBSTAGE_NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(stage_name)
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

    def verify_job_stage_created(self, stage_name):
        element = self.page.locator(f"text={stage_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Job Stage create verify nahi ho saka!"