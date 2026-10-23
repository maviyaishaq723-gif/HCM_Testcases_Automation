import re
from datetime import date
from urllib.parse import urlparse
from playwright.sync_api import expect
from pages.base_page import BasePage


class UserManagementLogsPage(BasePage):
    LOGS_BTN = ".page-header a[href*='/hcm/lastlogin']"
    MONTH_INPUT = "form#employee_filter input[type='month']"
    EMPLOYEE_SELECT = "select#employee_id"
    SEARCH_BTN = "form#employee_filter :is(button[type='submit'], input[type='submit'], .btn-primary)"
    RESET_BTN = "form#employee_filter :is(.btn-danger, button[type='reset'], a[href*='lastlogin'])"
    TABLE_SEARCH = "input.dataTable-input"
    ROWS = "table tbody tr"
    MODAL = ".modal.show"
    SWAL = ".swal2-popup"

    # ---------- helpers ----------
    def _base(self):
        p = urlparse(self.page.url)
        return f"{p.scheme}://{p.netloc}"

    def _wait_table(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.ROWS).first).to_be_visible(timeout=15000)

    def first_row_name(self):
        return self.page.locator(self.ROWS).first.locator("td").first.inner_text().strip()

    def logged_in_name(self):
        """Header ke 'Hi, <name>!' se login user ka naam."""
        try:
            txt = self.page.get_by_text(re.compile(r"Hi,\s*.+!")).first.inner_text()
            m = re.search(r"Hi,\s*(.+?)\s*!", txt)
            if m:
                return m.group(1).strip()
        except Exception:
            pass
        return "HR User"

    def _protected_names(self):
        return {self.logged_in_name().lower(), "hr user"}

    # ---------- TC_04 ----------
    def open_users_page(self):
        self.page.goto(f"{self._base()}/hcm/user", wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

    def click_logs_button(self):
        btn = self.page.locator(self.LOGS_BTN).first
        expect(btn).to_be_visible(timeout=15000)
        btn.click()

    def verify_logs_page_opened(self):
        expect(self.page).to_have_url(re.compile(r"/hcm/lastlogin"), timeout=15000)
        expect(self.page.get_by_text("Manage User Logs History").first).to_be_visible(timeout=15000)

    def open_logs_page(self):
        self.open_users_page()
        self.click_logs_button()
        self.verify_logs_page_opened()
        self._wait_table()

    # ---------- TC_05 / TC_06 ----------
    def apply_filter(self):
        name = self.first_row_name()
        self.month = date.today().strftime("%Y-%m")
        self.page.locator(self.MONTH_INPUT).fill(self.month)

        select = self.page.locator(self.EMPLOYEE_SELECT)
        chosen = None
        for opt in select.locator("option").all():
            val = opt.get_attribute("value")
            if not val:
                continue
            if chosen is None:
                chosen = val
            if name.lower() in opt.inner_text().strip().lower():
                chosen = val
                break
        assert chosen, "Employee dropdown me koi employee option nahi mila"
        select.select_option(value=chosen)
        self.employee_value = chosen

        self.page.locator(self.SEARCH_BTN).first.click()
        self.page.wait_for_load_state("networkidle")

    def verify_filter_applied(self):
        expect(self.page).to_have_url(re.compile(rf"month={self.month}"), timeout=15000)
        expect(self.page).to_have_url(re.compile(rf"employee={self.employee_value}"), timeout=15000)
        expect(self.page.locator(self.EMPLOYEE_SELECT)).to_have_value(self.employee_value)
        expect(self.page.locator(self.ROWS).first).to_be_visible(timeout=15000)

    def click_reset(self):
        self.page.locator(self.RESET_BTN).first.click()
        self.page.wait_for_load_state("networkidle")

    def verify_filter_reset(self):
        expect(self.page.locator(self.EMPLOYEE_SELECT)).to_have_value("", timeout=15000)
        expect(self.page).not_to_have_url(re.compile(rf"employee={self.employee_value}"))
        expect(self.page.locator(self.ROWS).first).to_be_visible(timeout=15000)

    # ---------- TC_07 ----------
    def search_existing_name(self):
        self.search_text = self.first_row_name()
        self.page.locator(self.TABLE_SEARCH).fill(self.search_text)
        self.page.wait_for_timeout(800)

    def verify_search_results(self):
        rows = self.page.locator(self.ROWS)
        expect(rows.first).to_be_visible(timeout=10000)
        for i in range(rows.count()):
            assert self.search_text.lower() in rows.nth(i).inner_text().lower(), \
                f"Row {i} me '{self.search_text}' nahi mila"

    # ---------- TC_08 ----------
    def click_view_first_log(self):
        self.page.locator(self.ROWS).first.locator("a.btn-sm").first.click()

    def verify_log_details_popup(self):
        modal = self.page.locator(self.MODAL)
        expect(modal).to_be_visible(timeout=15000)
        expect(modal).to_contain_text("View User Logs")
        expect(modal).to_contain_text("Browser Name")
        modal.locator(".btn-close, [data-bs-dismiss='modal']").first.click()
        expect(modal).to_be_hidden(timeout=10000)

        # ---------- TC_09 ----------
    def click_delete_first_log(self):
        row = self.page.locator(self.ROWS).first
        cells = row.locator("td")
        assert cells.count() >= 5, "Table me koi log nahi hai"
        self.deleted_name = cells.first.inner_text().strip()
        self.deleted_login = cells.nth(2).inner_text().strip()
        row.locator("td").last.locator(".btn-danger, [class*='danger']").first.click()

    def confirm_delete(self):
        dialog = self.page.locator(self.SWAL).first
        expect(dialog).to_be_visible(timeout=10000)
        expect(dialog).to_contain_text("Are you sure")
        dialog.locator("button.swal2-confirm").click()
        self.page.wait_for_load_state("networkidle")
        # agar success popup aaye to OK kar do
        try:
            expect(self.page.locator("button.swal2-confirm")).to_be_hidden(timeout=6000)
        except AssertionError:
            self.page.locator("button.swal2-confirm").first.click()
        self.page.wait_for_load_state("networkidle")

    def verify_log_deleted(self):
        self.page.goto(f"{self._base()}/hcm/lastlogin", wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        # last-login timestamp unique hota hai, usse search karo
        self.page.locator(self.TABLE_SEARCH).fill(self.deleted_login)
        self.page.wait_for_timeout(800)
        rows = self.page.locator(self.ROWS)
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            if cells.count() >= 5:
                assert not (
                    cells.first.inner_text().strip() == self.deleted_name
                    and cells.nth(2).inner_text().strip() == self.deleted_login
                ), f"Log ({self.deleted_name} - {self.deleted_login}) abhi bhi table me hai"