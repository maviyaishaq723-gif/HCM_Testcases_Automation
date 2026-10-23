import os
from pages.base_page import BasePage

class EmployeeExportImportPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.employee_menu = "//a[@class='dash-link']//span[text()='Employee']"
        self.heading_tag = "h4"
        self.export_btn = "a.btn.btn-sm.btn-primary:has-text('Export Employee')"
        self.downloaded_file = None
        
        # Import Selectors
        self.import_btn = "a:has-text('Import Employee')"
        self.file_input = "#file"
        self.upload_submit_btn = "input[type='submit'][value='Upload']"

    def navigate_to_employee(self):
        self.click(self.employee_menu)
        self.page.wait_for_timeout(2000)

    def verify_manage_employee_page(self) -> bool:
        heading = self.page.locator(self.heading_tag).first
        heading.wait_for(state="visible", timeout=5000)
        return heading.inner_text().strip() == "Manage Employee"

    def click_export_employee(self):
        with self.page.expect_download() as download_info:
            export_loc = self.page.locator(self.export_btn).first
            export_loc.wait_for(state="visible", timeout=5000)
            export_loc.click()
        self.downloaded_file = download_info.value
        self.page.wait_for_timeout(5000)

    def upload_employee_file(self):
        imp_loc = self.page.locator(self.import_btn).first
        imp_loc.wait_for(state="visible", timeout=5000)
        imp_loc.click()
        self.page.wait_for_timeout(2000)

        file_name = "sample-employee.xlsx"
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                f.write("Dummy employee data for import testing")
        file_path = os.path.abspath(file_name)

        file_input_loc = self.page.locator(self.file_input)
        file_input_loc.set_input_files(file_path)
        self.page.wait_for_timeout(2000)

        upload_loc = self.page.locator(self.upload_submit_btn).first
        upload_loc.wait_for(state="visible", timeout=5000)
        upload_loc.click()
        self.page.wait_for_timeout(5000)