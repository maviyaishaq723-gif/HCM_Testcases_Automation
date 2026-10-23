import random
import re
import string
import time
from urllib.parse import urlparse

from playwright.sync_api import expect
from pages.base_page import BasePage

EDIT_URL_REGEX = r"/edit/?$"
TEST_EMPLOYEE_PREFIX = "Auto Employee"      # create test isi naam se employee banata hai

_rng = random.SystemRandom()


def _letters(n):
    return "".join(_rng.choice(string.ascii_lowercase) for _ in range(n))


def _digits(n):
    return "".join(_rng.choice(string.digits) for _ in range(n))


class EmployeeEditPage(BasePage):
    TABLE_ROWS = "#pc-dt-simple tbody tr"
    SEARCH_BOX = ".dataTable-input, input[type='search']"
    SAVE_BTN = "button[type='submit']"

    # ---------- helpers ----------
    def origin(self):
        u = urlparse(self.page.url)
        return f"{u.scheme}://{u.netloc}"

    def settle(self):
        """Page ke ajax/reload khatam hone ka wait"""
        try:
            self.page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass
        self.page.wait_for_timeout(800)

    def fill_box(self, selector, value):
        """Text box mein asli typing karta hai (Tab nahi, taake calendar na khule)"""
        box = self.page.locator(selector)
        box.wait_for(state="visible", timeout=10000)
        box.focus()
        box.fill("")
        box.press_sequentially(value, delay=30)
        box.evaluate("e => e.blur()")
        self.page.wait_for_timeout(300)

    def visible_errors(self):
        return self.page.evaluate("""() => [...document.querySelectorAll(
            '.invalid-feedback, .text-danger, .error, label.error, .alert-danger, .toast, .swal2-popup')]
            .filter(e => e.offsetParent !== null)
            .map(e => e.textContent.trim().replace(/\\s+/g, ' '))
            .filter(t => t.length > 3)""")

    def dump_fields(self):
        return self.page.evaluate("""() => ['name','phone','email','username','address','cnicInput','emp_no']
            .map(id => { const e = document.getElementById(id);
                return id + '=' + (e ? e.value : 'NOT FOUND'); })""")

    def button_enabled(self, button, timeout_ms=6000):
        end = time.time() + timeout_ms / 1000
        while time.time() < end:
            if button.is_enabled():
                return True
            self.page.wait_for_timeout(300)
        return False

    def wait_submit_result(self, still_here_regex, timeout_s=20):
        """Save ke baad intezaar: ('done', []) ya ('error', [errors])"""
        start = time.time()
        while time.time() - start < timeout_s:
            if not re.search(still_here_regex, self.page.url):
                return "done", []
            if time.time() - start > 2:
                errs = self.visible_errors()
                if errs:
                    return "error", errs
            self.page.wait_for_timeout(500)
        return "error", self.visible_errors()

    # ---------- list page ----------
    def open_employee_list(self):
        self.page.goto(self.origin() + "/hcm/employee")
        self.page.locator(self.TABLE_ROWS).first.wait_for(state="visible", timeout=20000)
        self.settle()

    def search_box(self):
        box = self.page.locator(self.SEARCH_BOX).first
        try:
            box.wait_for(state="visible", timeout=10000)
        except Exception:
            raise AssertionError("Employee table ka search box nahi mila (selector: " + self.SEARCH_BOX + ")")
        return box

    def search(self, text):
        """Table mein search karke us employee ki row return karta hai"""
        box = self.search_box()
        box.fill("")
        box.press_sequentially(text, delay=20)
        self.page.wait_for_timeout(600)
        row = self.page.locator(self.TABLE_ROWS).filter(has_text=text).first
        row.wait_for(state="visible", timeout=10000)
        return row

    # ---------- edit flow ----------
    def open_edit_for_test_employee(self):
        """Create test ki banayi hui pehli 'Auto Employee' ka Edit kholta hai.
        Asli employees ko kabhi nahi chhoota."""
        self.open_employee_list()
        box = self.search_box()
        box.fill("")
        box.press_sequentially(TEST_EMPLOYEE_PREFIX, delay=20)
        self.page.wait_for_timeout(600)
        rows = self.page.locator(self.TABLE_ROWS).filter(has_text=TEST_EMPLOYEE_PREFIX)
        if rows.count() == 0:
            raise AssertionError(
                f"Koi test employee ('{TEST_EMPLOYEE_PREFIX} ...') list mein nahi mili. "
                "Pehle create test chalao: behave features/employee/employee_create.feature"
            )
        rows.first.locator("a[href$='/edit']").first.click()
        self.page.wait_for_url(re.compile(EDIT_URL_REGEX), timeout=15000)
        self.page.wait_for_selector("#name", timeout=15000)
        expect(self.page.locator("#name")).not_to_have_value("", timeout=15000)   # purana data load hua
        expect(self.page.locator("#name")).to_have_value(re.compile("^" + TEST_EMPLOYEE_PREFIX))

    def update_details_and_save(self):
        new = {
            "name": f"{TEST_EMPLOYEE_PREFIX} {_letters(8)}",     # naam letters-only, aur prefix wahi
            "phone": "03" + _digits(9),
            "address": f"Updated Street {_letters(5)}, Lahore",
        }
        self.fill_box("#name", new["name"])
        self.fill_box("#phone", new["phone"])
        self.fill_box("#address", new["address"])

        save = (self.page.locator(self.SAVE_BTN)
                .filter(has_text=re.compile("create|update|save", re.I)).last)
        save.scroll_into_view_if_needed()
        if not self.button_enabled(save, 8000):
            raise AssertionError(
                "Save button disabled raha. FIELDS: " + " | ".join(self.dump_fields())
                + " || ERRORS: " + str(self.visible_errors())
            )
        save.click()

        outcome, errors = self.wait_submit_result(EDIT_URL_REGEX, timeout_s=20)
        if outcome != "done":
            self.page.screenshot(path="reports/after_edit_submit.png", full_page=True)
            raise AssertionError(
                f"Edit save nahi hua (page /edit pe hi raha). Errors: {errors} || FIELDS: "
                + " | ".join(self.dump_fields())
            )
        return new

    def verify_updated(self, new):
        self.open_employee_list()
        row = self.search(new["name"])
        expect(row).to_be_visible()