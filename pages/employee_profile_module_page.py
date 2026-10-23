import re
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import expect
from pages.base_page import BasePage


class EmployeeProfileModulePage(BasePage):
    FILTER_FORM = "form#employee_profile_filter"
    FILTER_TOGGLE = "a[href$='#multiCollapseExample1'], [data-bs-target='#multiCollapseExample1']"
    BRANCH = "select[name='branch']"
    DEPARTMENT = "select[name='department']"
    DESIGNATION = "select#designation_id"
    SEARCH_BTN = (
        "form#employee_profile_filter :is(button[type='submit'], input[type='submit'], "
        "button.btn-primary, a.btn-primary)"
    )
    ID_LINKS = "a.btn-outline-primary[href*='/hcm/employee/']"

    LANG_TOGGLE = "#dropdownLanguage"
    LANG_ITEMS = ".drp-language .dropdown-menu :is(a, .dropdown-item)"
    CHAT_BTN = "header a.dash-head-link:has(i.ti-message-circle)"
    MSG_BTN = "header a#msg-btn"
    VIEW_ALL = ".dropdown-menu.show a:has-text('View all')"

    ADDRESS_SELECTORS = ["textarea[name='address']", "textarea#address", "textarea"]
    UPDATE_SELECTORS = [
        "input[type='submit'][value='Update' i]",
        "button:has-text('Update')",
        "input[value='Update' i]",
        "input.update-button",
        ".update-button",
    ]

    # ---------- helpers ----------
    def _base(self):
        p = urlparse(self.page.url)
        return f"{p.scheme}://{p.netloc}"

    def _first_visible(self, selectors, timeout=10000):
        end = self.page.evaluate("Date.now()") + timeout
        while self.page.evaluate("Date.now()") < end:
            for sel in selectors:
                loc = self.page.locator(sel).first
                if loc.count() and loc.is_visible():
                    return loc
            self.page.wait_for_timeout(250)
        raise AssertionError(f"Koi locator visible nahi mila: {selectors}")

    def _card_of(self, link):
        """ID button ka card container (sabse qareeb ka div jisme designation <small> ho)."""
        return link.locator("xpath=ancestor::div[.//small][1]")

    # ---------- navigation ----------
    def open_listing(self):
        self.page.goto(f"{self._base()}/hcm/employee-profile", wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.ID_LINKS).first).to_be_visible(timeout=20000)

    def click_first_employee_id(self):
        link = self.page.locator(self.ID_LINKS).first
        expect(link).to_be_visible(timeout=15000)
        self.employee_id = link.inner_text().strip()
        card = self._card_of(link)
        name_el = card.locator(".text-primary").first
        self.employee_name = name_el.inner_text().strip() if name_el.count() else ""
        link.click()
        self.page.wait_for_load_state("networkidle")

    def open_employee_by_id(self):
        link = self.page.locator(self.ID_LINKS).filter(
            has_text=re.compile(rf"^\s*{re.escape(self.employee_id)}\s*$")
        ).first
        expect(link).to_be_visible(timeout=15000)
        link.click()
        self.page.wait_for_load_state("networkidle")

    # ---------- TC_15 ----------
    def verify_manage_employee_page(self):
        expect(self.page).to_have_url(re.compile(r"/hcm/employee/"), timeout=20000)
        self.page.wait_for_load_state("networkidle")

        id_core = self.employee_id.lstrip("#").strip()
        keys = [k for k in (self.employee_name, id_core) if k]
        assert keys, "Employee ka naam/ID card se nahi mila"
        pattern = re.compile("|".join(re.escape(k) for k in keys), re.I)

        end = self.page.evaluate("Date.now()") + 15000
        while self.page.evaluate("Date.now()") < end:
            text = self.page.evaluate(
                "document.body.innerText + ' ' + "
                "Array.from(document.querySelectorAll('input,textarea')).map(e => e.value).join(' ')"
            )
            if pattern.search(text):
                return
            self.page.wait_for_timeout(500)
        raise AssertionError(
            f"Manage Employee page par employee ({self.employee_name} / {self.employee_id}) nahi dikha"
        )

    # ---------- TC_16 ----------
    def open_filter_panel(self):
        form = self.page.locator(self.FILTER_FORM)
        if not form.is_visible():
            self.page.locator(self.FILTER_TOGGLE).first.click()
        expect(form).to_be_visible(timeout=10000)

    def _options(self, selector):
        return self.page.locator(f"{selector} option").evaluate_all(
            "els => els.map(e => [e.value, (e.textContent || '').trim()])"
        )

    def _pick(self, selector, prefer, wait_ms=10000):
        """Options aane ka wait karke 'prefer' wala (warna pehla) option chunta hai."""
        end = self.page.evaluate("Date.now()") + wait_ms
        candidates = []
        while self.page.evaluate("Date.now()") < end:
            candidates = [
                (v, t) for v, t in self._options(selector)
                if v and t and t.lower() != "all" and not t.lower().startswith("select")
            ]
            if candidates:
                break
            self.page.wait_for_timeout(300)
        if not candidates:
            return None
        chosen = next((c for c in candidates if prefer in c[1].lower()), candidates[0])
        self.page.locator(selector).select_option(value=chosen[0], force=True)
        self.page.wait_for_load_state("networkidle")
        return chosen

    def apply_profile_filter(self):
        self.page.wait_for_timeout(500)
        self._pick(self.BRANCH, "ufone")
        self._pick(self.DEPARTMENT, "customer care")
        designation = self._pick(self.DESIGNATION, "executive")
        self.designation_text = designation[1] if designation else ""
        self.page.locator(self.SEARCH_BTN).first.click()
        self.page.wait_for_load_state("networkidle")

    def verify_profile_filter_results(self):
        links = self.page.locator(self.ID_LINKS)
        expect(links.first).to_be_visible(timeout=15000)
        count = links.count()
        assert count > 0, "Filter ke baad koi employee nahi dikha"
        if self.designation_text:
            term = self.designation_text.lower()
            for i in range(count):
                small = self._card_of(links.nth(i)).locator("small").first
                text = small.inner_text().strip().lower()
                assert term in text, f"Card {i + 1} ki designation '{text}' hai, expected '{term}'"

    # ---------- TC_17 / TC_20 ----------
    def click_edit_profile_button(self):
        """Manage Employee page par 'Edit Profile' button. Na mile to False."""
        end = self.page.evaluate("Date.now()") + 8000
        while self.page.evaluate("Date.now()") < end:
            for sel in ["a:has-text('Edit Profile')", "button:has-text('Edit Profile')"]:
                loc = self.page.locator(sel).first
                if loc.count() and loc.is_visible():
                    loc.click()
                    self.page.wait_for_load_state("networkidle")
                    return True
            self.page.wait_for_timeout(300)
        return False

    def _address_box(self):
        return self._first_visible(self.ADDRESS_SELECTORS, timeout=15000)

    def _click_update(self):
        for sel in self.UPDATE_SELECTORS:
            loc = self.page.locator(sel).first
            if loc.count() and loc.is_visible():
                loc.scroll_into_view_if_needed()
                loc.click()
                return
        subs = self.page.locator("form input[type='submit'], form button[type='submit']")
        for i in reversed(range(subs.count())):
            if subs.nth(i).is_visible():
                subs.nth(i).scroll_into_view_if_needed()
                subs.nth(i).click()
                return
        raise AssertionError("Update button nahi mila")

    def change_address_and_update(self):
        self.new_address = f"Address_Updated_Auto_{datetime.now():%Y%m%d%H%M%S}"
        self._address_box().fill(self.new_address)
        self._click_update()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1500)

    def verify_changes_saved(self):
        # Update ke baad dobara employee kholo, Edit Profile dabao aur address check karo
        self.open_listing()
        self.open_employee_by_id()
        assert self.click_edit_profile_button(), "Verify ke waqt Edit Profile button nahi mila"
        expect(self._address_box()).to_have_value(self.new_address, timeout=15000)

    # ---------- TC_21 ----------
    def current_language(self):
        return self.page.locator(f"{self.LANG_TOGGLE} .drp-text").first.inner_text().strip()

    def _select_language(self, name):
        self.page.locator(self.LANG_TOGGLE).first.click()
        item = self.page.locator(self.LANG_ITEMS).filter(
            has_text=re.compile(rf"^\s*{name}\s*$", re.I)
        ).first
        expect(item).to_be_visible(timeout=10000)
        item.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def select_chinese_language(self):
        if self.current_language().lower() != "english":  # pichla run Chinese me chhod gaya ho
            self._select_language("English")
        self._select_language("Chinese")

    def verify_chinese_content(self):
        assert self.current_language().lower() == "chinese", "Language dropdown Chinese nahi dikha raha"
        expect(self.page.locator("nav.dash-sidebar")).to_contain_text(
            re.compile(r"[\u4e00-\u9fff]"), timeout=15000
        )

    def restore_english_language(self):
        """Test ke baad language wapas English, warna baqi tests Chinese me chalenge."""
        try:
            if self.current_language().lower() != "english":
                self._select_language("English")
        except Exception:
            pass

    # ---------- TC_22 / TC_23 ----------
    def click_chat_button(self):
        btn = self.page.locator(self.CHAT_BTN).first
        expect(btn).to_be_visible(timeout=10000)
        btn.click()

    def click_message_button_and_view_all(self):
        self.page.locator(self.MSG_BTN).first.click()
        view_all = self.page.locator(self.VIEW_ALL).first
        expect(view_all).to_be_visible(timeout=10000)
        view_all.click()

    def verify_messenger_opened(self):
        expect(self.page).to_have_url(re.compile(r"/hcm/chats"), timeout=20000)
        expect(self.page.locator(".messenger").first).to_be_visible(timeout=15000)
        expect(self.page.locator(".messenger-listView").first).to_be_visible(timeout=15000)
        expect(self.page.get_by_text("Saved Messages").first).to_be_visible(timeout=15000)