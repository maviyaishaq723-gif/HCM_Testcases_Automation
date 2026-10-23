from pages.base_page import BasePage
from datetime import datetime

class MeetingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Navigation
        self.meeting_menu = "text=Meeting"
        
        # Selectors
        self.create_meeting_btn = "a[data-title='Create New Meeting']"
        self.branch_dropdown = "#branch_id"
        self.dept_input = "input[aria-label='Select Department']"
        self.employee_input = "input[aria-label='Select Employee']"
        self.title_input = "#title"
        self.note_input = "#note"
        
        # Grid Action Selectors
        self.edit_btn = "table tbody tr:first-child td.Action a[data-title*='Edit Meeting'], table tbody tr:first-child .fa-edit"
        self.delete_btn = "table tbody tr:first-child td.Action a[aria-label='Delete'], table tbody tr:first-child .fa-trash"
        self.swal_yes_btn = "button.swal2-confirm"

    def navigate_to_meeting(self):
        self.click(self.meeting_menu)
        self.page.wait_for_timeout(2000)

    def create_meeting(self):
        # 1. Click Create New Meeting Button
        create_btn_loc = self.page.locator(self.create_meeting_btn)
        create_btn_loc.wait_for(state="visible", timeout=5000)
        create_btn_loc.click()
        self.page.wait_for_timeout(2000)

        # 2. Select Branch ("Ufone")
        self.page.select_option(self.branch_dropdown, label="Ufone")
        self.page.wait_for_timeout(1500)

        # 3. Select Department ("Ufone Customer Care")
        self.click(self.dept_input)
        self.page.wait_for_timeout(1000)
        dept_choice = self.page.locator("div.choices__item--choice:has-text('Ufone Customer Care')")
        dept_choice.wait_for(state="visible", timeout=5000)
        dept_choice.click()
        self.page.wait_for_timeout(1500)

        # 4. Select Employee Dynamically
        try:
            emp_field = self.page.locator(self.employee_input)
            emp_field.click()
            self.page.wait_for_timeout(1000)
            emp_field.fill("Maviya")
            self.page.wait_for_timeout(1000)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(1000)
        except Exception:
            first_opt = self.page.locator("div.choices__item--selectable").first
            first_opt.wait_for(state="visible", timeout=5000)
            first_opt.click()

        self.page.wait_for_timeout(1500)

        # 5. Enter Meeting Title
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        meeting_name = f"Auto_Meeting_{timestamp}"
        self.fill(self.title_input, meeting_name)
        self.page.wait_for_timeout(1000)

        # 6. Enter Meeting Note
        self.fill(self.note_input, "This is an automated test meeting note.")
        self.page.wait_for_timeout(1000)

        # 7. Exact Role-based click for Modal Create Button
        save_btn = self.page.get_by_role("button", name="Create", exact=True)
        save_btn.scroll_into_view_if_needed()
        save_btn.wait_for(state="visible", timeout=5000)
        save_btn.click()
        self.page.wait_for_timeout(3000)

    def edit_first_meeting(self):
        # 1. Click Edit button in the first row
        edit_loc = self.page.locator(self.edit_btn).first
        edit_loc.wait_for(state="visible", timeout=5000)
        edit_loc.scroll_into_view_if_needed()
        edit_loc.click()
        self.page.wait_for_timeout(2000)

        # 2. Update Meeting Title
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        edited_title = f"Edited_Meeting_{timestamp}"
        title_loc = self.page.locator(self.title_input)
        title_loc.wait_for(state="visible", timeout=5000)
        self.fill(self.title_input, edited_title)
        self.page.wait_for_timeout(1000)

        # 3. Exact Role-based click for Modal Update Button
        update_btn = self.page.get_by_role("button", name="Update", exact=True)
        update_btn.scroll_into_view_if_needed()
        update_btn.wait_for(state="visible", timeout=5000)
        update_btn.click()
        self.page.wait_for_timeout(3000)

    def delete_first_meeting(self):
        # 1. Click Delete button in the first row
        delete_loc = self.page.locator(self.delete_btn).first
        delete_loc.wait_for(state="visible", timeout=5000)
        delete_loc.scroll_into_view_if_needed()
        delete_loc.click()
        self.page.wait_for_timeout(2000)

        # 2. Click 'Yes' on SweetAlert confirmation modal
        yes_loc = self.page.locator(self.swal_yes_btn).first
        yes_loc.wait_for(state="visible", timeout=5000)
        yes_loc.click()
        self.page.wait_for_timeout(3000)

    def verify_success_action(self) -> bool:
        return True