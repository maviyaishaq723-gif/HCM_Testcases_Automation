from pages.base_page import BasePage

class OrganizationCompetenciesPage(BasePage):
    COMPETENCIES_TAB = "a:has-text('Competencies'), a[href*='/competencies']"
    COMPETENCIES_BTN = "a:has-text('Create New Competencies'), a[data-title*='Create New Competencies']"
    NAME_INPUT = "input[placeholder='Enter Competencies Name']"
    TYPE_DROPDOWN = "select#type.form-control, select[name='type']"
    CREATE_BTN = "input.create-button, input[type='submit'][value='Create'], button.create-button"
    SEARCH_INPUT = ".dataTable-input"
    MODAL_POPUP = "div.modal, div#commonModal"

    def click_competencies_tab(self):
        tab = self.page.locator(self.COMPETENCIES_TAB).first
        tab.wait_for(state="visible", timeout=15000)
        tab.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def click_add_competencies_btn(self):
        btn = self.page.locator(self.COMPETENCIES_BTN).first
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        self.page.wait_for_timeout(2000)

    def fill_competencies_form(self, competency_name, competency_type="Individual"):
        name_box = self.page.locator(self.NAME_INPUT).first
        name_box.wait_for(state="visible", timeout=10000)
        name_box.click()
        name_box.fill(competency_name)
        self.page.wait_for_timeout(1000)

        # Dropdown selection handling
        dropdown = self.page.locator(self.TYPE_DROPDOWN).first
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.select_option(label=competency_type)
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

    def verify_competencies_created(self, competency_name):
        search = self.page.locator(self.SEARCH_INPUT).first
        search.wait_for(state="visible", timeout=15000)
        search.click()
        search.fill(competency_name)
        search.press("Enter")
        self.page.wait_for_timeout(3000)
        
        element = self.page.locator(f"text={competency_name}").first
        element.wait_for(state="visible", timeout=15000)
        assert element.is_visible(), "Competencies create verify nahi ho saka!"