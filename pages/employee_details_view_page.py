import re

from playwright.sync_api import expect
from pages.base_page import BasePage

LIST_URL_REGEX = r"/hcm/employee/?$"
SECTIONS = ["letter", "warning", "award", "leave", "training",
            "personal", "company", "bank", "document"]      # expected result mein diye gaye sections
MIN_SECTIONS = 4        # kam az kam itne sections page pe hone chahiye


class EmployeeDetailsViewPage(BasePage):
    TABLE_ROWS = "#pc-dt-simple tbody tr"

    def open_first_employee_details(self):
        """List ki pehli employee ka Employee ID click karta hai (sirf dekhna, kuch change nahi hota)"""
        row = self.page.locator(self.TABLE_ROWS).first
        row.wait_for(state="visible", timeout=20000)
        id_cell = row.locator("td").first
        self.emp_no = id_cell.inner_text().strip()
        self.emp_name = row.locator("td").nth(1).inner_text().strip()

        link = id_cell.locator("a")
        (link.first if link.count() > 0 else id_cell).click()

        expect(self.page).not_to_have_url(re.compile(LIST_URL_REGEX), timeout=15000)
        self.page.wait_for_load_state("domcontentloaded")
        try:
            self.page.wait_for_load_state("networkidle", timeout=8000)
        except Exception:
            pass

    def verify_details_page(self):
        text = self.page.evaluate(
            "() => (document.querySelector('.pc-container') || document.body).textContent.toLowerCase()"
        )
        text = re.sub(r"\s+", " ", text)

        who = [self.emp_name.lower(), self.emp_no.lstrip("#").lower()]
        assert any(w and w in text for w in who), (
            f"Employee details page par '{self.emp_name}' / '{self.emp_no}' nahi mila. URL: {self.page.url}"
        )

        found = [s for s in SECTIONS if s in text]
        missing = [s for s in SECTIONS if s not in text]
        assert len(found) >= MIN_SECTIONS, (
            f"Details page par sirf {len(found)} sections mile (chahiye {MIN_SECTIONS}+). "
            f"Mile: {found} | Nahi mile: {missing} | URL: {self.page.url}"
        )