import re
from urllib.parse import urlparse
from playwright.sync_api import expect
from pages.base_page import BasePage


class UserManagementCreateUserPage(BasePage):
    NEW_USER_BTN = "a.btn-addnew-project"
    FORM = "form:has(input#name):has(select#role)"
    CREATE_BTN = "input.create-button"

    # ---------- navigation ----------
    def navigate_to_user_management(self):
        p = urlparse(self.page.url)
        self.page.goto(f"{p.scheme}://{p.netloc}/hcm/user", wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

    def click_user_tab(self):
        if not re.search(r"/hcm/user/?(#.*)?$", self.page.url):
            self.page.locator("a.dash-link", has_text="User Management").first.click()
            self.page.locator("a.dash-link[href$='/hcm/user']").first.click()
            self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.NEW_USER_BTN).first).to_be_visible(timeout=20000)

    def click_add_new_user_btn(self):
        btn = self.page.locator(self.NEW_USER_BTN).first
        btn.scroll_into_view_if_needed()
        btn.wait_for(state="visible", timeout=15000)
        btn.click()
        expect(self.page.locator(self.FORM).first).to_be_visible(timeout=15000)

    # ---------- form ----------
    def fill_user_form(self, name, email, password, role_name="hr"):
        form = self.page.locator(self.FORM).first

        form.locator("input#name").fill(name)
        form.locator("input#email, input[name='email']").first.fill(email)
        form.locator("input#password").fill(password)

        self._select_role(form, role_name)

        create_btn = form.locator(self.CREATE_BTN)
        create_btn.scroll_into_view_if_needed()
        expect(create_btn).to_be_enabled(timeout=10000)
        create_btn.click()

        # Create hone par popup band ho jata hai
        expect(self.page.locator(self.FORM)).to_be_hidden(timeout=20000)
        self.page.wait_for_load_state("networkidle")

    def _select_role(self, form, role_name):
        exact = re.compile(rf"^\s*{re.escape(role_name)}\s*$", re.I)
        choices = form.locator("div.choices:has(select#role)")
        choices.click()
        option = choices.locator(
            ".choices__list--dropdown .choices__item--choice", has_text=exact
        ).first
        option.wait_for(state="visible", timeout=10000)
        option.click()
        # selected value hidden <select> se verify (UI text me "Remove item" bhi hota hai)
        expect(form.locator("select#role option:checked")).to_have_text(exact)

    # ---------- verification ----------
    def verify_user_created(self, name):
        self.navigate_to_user_management()
        expect(
            self.page.get_by_text(re.compile(rf"^\s*{re.escape(name)}\s*$", re.I)).first
        ).to_be_visible(timeout=15000)