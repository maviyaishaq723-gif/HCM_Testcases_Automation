import re
from urllib.parse import urlparse
from playwright.sync_api import expect
from pages.base_page import BasePage


class RoleManagementPage(BasePage):
    CREATE_ROLE_BTN = "a.btn-primary:has-text('Create New Role')"
    MODAL = "#commonModal.show, .modal.show"
    NAME_INPUT = "input#name"
    SUBMIT_BTN = "input.create-button"
    TOAST = ".toast-body"
    TABLE_SEARCH = "input.dataTable-input"
    ROWS = "table tbody tr"

    # TC_12 me ye dono naam search hote hain (order yehi rahega)
    SEARCH_TERMS = ["hr", "test hr"]

    # ---------- helpers ----------
    def _base(self):
        p = urlparse(self.page.url)
        return f"{p.scheme}://{p.netloc}"

    def _wait_table(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.ROWS).first).to_be_visible(timeout=15000)

    @staticmethod
    def _norm(text):
        return re.sub(r"\s+", " ", text or "").strip().lower()

    def _role_names_on_page(self):
        names = []
        rows = self.page.locator(self.ROWS)
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            if cells.count() >= 2:
                name = cells.first.inner_text().strip()
                if name:
                    names.append(name)
        return names

    def _first_role_name(self):
        names = self._role_names_on_page()
        assert names, "Roles table me koi role nahi mila"
        return names[0]

    def _search(self, text):
        """Keyboard se type karta hai taake table ka keyup filter chale (fill() se nahi chalta)."""
        box = self.page.locator(self.TABLE_SEARCH)
        expect(box).to_be_visible(timeout=10000)
        box.click()
        box.fill("")
        box.press_sequentially(text, delay=60)
        self.page.wait_for_timeout(1000)

    # ---------- navigation ----------
    def navigate_to_role_page(self):
        self.page.goto(f"{self._base()}/hcm/roles", wait_until="domcontentloaded")
        self._wait_table()

    # ---------- TC_11 ----------
    def click_create_new_role(self):
        btn = self.page.locator(self.CREATE_ROLE_BTN).first
        expect(btn).to_be_visible(timeout=15000)
        btn.click()
        modal = self.page.locator(self.MODAL).first
        expect(modal).to_be_visible(timeout=15000)
        expect(modal.locator(self.NAME_INPUT)).to_be_visible(timeout=10000)

    def create_role_with_existing_name(self):
        self.existing_role = self._first_role_name()
        modal = self.page.locator(self.MODAL).first
        modal.locator(self.NAME_INPUT).fill(self.existing_role)
        submit = modal.locator(self.SUBMIT_BTN)
        submit.scroll_into_view_if_needed()
        expect(submit).to_be_enabled(timeout=10000)
        submit.click()

    def verify_role_already_exists_error(self):
        toast = self.page.locator(self.TOAST).filter(
            has_text=re.compile(r"already\s+been\s+taken|already\s+exist", re.I)
        ).first
        expect(toast).to_be_visible(timeout=15000)

    # ---------- TC_12 ----------
    def search_existing_role(self):
        # pehla search: "hr" (doosra "test hr" verify step me hota hai)
        self._search(self.SEARCH_TERMS[0])

    def _check_search(self, term):
        """Ek search term check karta hai. Problem mile to text return, sahi ho to None."""
        self._search(term)
        rows = self.page.locator(self.ROWS)
        expect(rows.first).to_be_visible(timeout=10000)

        roles = []
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            if cells.count() < 2:  # "No data available" row
                return f"'{term}' search par koi role nahi aayi"
            role = self._norm(cells.first.inner_text())
            if term not in role:
                return (f"'{term}' search par role '{role}' aayi, jiske naam me ye text nahi "
                        f"(permissions se match hui)")
            roles.append(role)

        if term not in roles:
            return f"'{term}' role khud search results me nahi dikhi. Results: {roles}"
        return None

    def verify_role_search_results(self):
        """'hr' aur 'test hr', dono search karke role naam verify karta hai."""
        problems = []
        for term in self.SEARCH_TERMS:
            problem = self._check_search(term)
            if problem:
                problems.append(problem)
        assert not problems, "Role search verify nahi hui: " + " | ".join(problems)