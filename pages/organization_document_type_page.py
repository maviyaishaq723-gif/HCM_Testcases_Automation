import re
import uuid
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import expect
from pages.base_page import BasePage


class OrganizationDocumentTypePage(BasePage):
    CREATE_BTN = "a.btn-primary:has-text('Create New Document Type')"
    FORM = "form:has(input#name):has(select#is_required)"
    NAME_INPUT = "input#name"
    REQUIRED_SELECT = "select#is_required"
    SUBMIT_BTN = "input.create-button"
    TABLE_SEARCH = "input.dataTable-input"
    ROWS = "table tbody tr"

    # ---------- helpers ----------
    def _base(self):
        p = urlparse(self.page.url)
        return f"{p.scheme}://{p.netloc}"

    def _search(self, text):
        """Keyboard se type karta hai taake table ka keyup filter chale (fill() se nahi chalta)."""
        box = self.page.locator(self.TABLE_SEARCH)
        expect(box).to_be_visible(timeout=10000)
        box.click()
        box.fill("")
        box.press_sequentially(text, delay=60)
        self.page.wait_for_timeout(1000)

    # ---------- navigation ----------
    def navigate_to_document_type(self):
        self.page.goto(f"{self._base()}/hcm/document", wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.CREATE_BTN).first).to_be_visible(timeout=20000)

    def click_create_document_type(self):
        btn = self.page.locator(self.CREATE_BTN).first
        btn.scroll_into_view_if_needed()
        btn.click()
        form = self.page.locator(self.FORM).first
        expect(form).to_be_visible(timeout=15000)
        expect(form.locator(self.NAME_INPUT)).to_be_visible(timeout=10000)

    # ---------- form ----------
    def fill_document_type_form(self):
        # System ki limit: naam 20 characters se zyada nahi ho sakta (ye 17 characters ka hai)
        unique = f"{datetime.now():%y%m%d%H%M%S}{uuid.uuid4().hex[:2]}"
        self.document_name = f"Doc{unique}"
        assert len(self.document_name) <= 20, "Document name 20 characters se zyada ho gaya"

        form = self.page.locator(self.FORM).first
        form.locator(self.NAME_INPUT).fill(self.document_name)
        self._select_required(form, "Is Required")

        submit = form.locator(self.SUBMIT_BTN)
        submit.scroll_into_view_if_needed()
        expect(submit).to_be_enabled(timeout=10000)
        submit.click()

        # Create hone par popup band ho jata hai
        expect(self.page.locator(self.FORM)).to_be_hidden(timeout=20000)
        self.page.wait_for_load_state("networkidle")

    def _select_required(self, form, option_text):
        exact = re.compile(rf"^\s*{re.escape(option_text)}\s*$", re.I)
        choices = form.locator(f"div.choices:has({self.REQUIRED_SELECT})")
        choices.click()
        option = choices.locator(
            ".choices__list--dropdown .choices__item--choice", has_text=exact
        ).first
        option.wait_for(state="visible", timeout=10000)
        option.click()
        # selected value hidden <select> se verify (UI text me "Remove item" bhi hota hai)
        expect(form.locator(f"{self.REQUIRED_SELECT} option:checked")).to_have_text(exact)

    # ---------- verification ----------
    def verify_document_type_created(self):
        self.navigate_to_document_type()
        # table 10 rows per page hai, isliye search se naam dhoondte hain
        self._search(self.document_name)
        rows = self.page.locator(self.ROWS)
        expect(rows.first).to_be_visible(timeout=10000)

        names = []
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            if cells.count() >= 2:
                names.append(cells.first.inner_text().strip())
        assert self.document_name in names, (
            f"Naya document type '{self.document_name}' list me nahi mila. Search results: {names}"
        )