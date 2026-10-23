import re
import time
from playwright.sync_api import expect


class EmployeeCreatePage:
    def __init__(self, page):
        self.page = page
        self.create_new_btn = "a:has-text('Create New Employee')"
        self.submit_btn = "button[type='submit']:has-text('Create')"
        self.trace_log = []

    # ---------- helper functions ----------
    def settle(self):
        """Page ke ajax/reload khatam hone ka wait"""
        try:
            self.page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass
        self.page.wait_for_timeout(800)

    def selected_text(self, selector):
        return self.page.eval_on_selector(
            selector,
            "e => e.options[e.selectedIndex] ? e.options[e.selectedIndex].text.trim() : ''",
        )

    def trace(self, label):
        """Har step ke baad dept/designation ka haal likh leta hai (debug ke liye)"""
        try:
            d = self.selected_text("#department_id")
            g = self.selected_text("#designation_id")
            self.trace_log.append(f"{label}: dept={d} / desig={g}")
        except Exception:
            pass

    def fill_box(self, selector, value):
        """Text box mein asli typing karta hai"""
        box = self.page.locator(selector)
        box.wait_for(state="visible", timeout=10000)
        box.click()
        box.fill("")
        box.press_sequentially(value, delay=30)
        box.press("Tab")
        self.page.wait_for_timeout(300)
        self.trace(selector)

    def fill_date(self, selector, value):
        """Date box (format hamesha YYYY-MM-DD)"""
        box = self.page.locator(selector)
        box.wait_for(state="visible", timeout=10000)
        box.fill(value)
        box.dispatch_event("input")
        box.dispatch_event("change")
        box.press("Tab")
        self.page.wait_for_timeout(300)
        self.trace(selector)

    def pick_by_text(self, selector, text):
        """Dropdown mein naam se option choose karta hai"""
        self.page.wait_for_function(
            """([sel, t]) => {
                const el = document.querySelector(sel);
                return el && !el.disabled &&
                       [...el.options].some(o => o.textContent.trim() === t);
            }""",
            arg=[selector, text],
            timeout=15000,
        )
        self.page.select_option(selector, label=text)
        self.settle()
        self.trace(selector)

    def pick_first(self, selector):
        """Dropdown ka pehla asli option choose karta hai"""
        self.page.wait_for_function(
            """(sel) => {
                const el = document.querySelector(sel);
                return el && !el.disabled && el.options.length > 1;
            }""",
            arg=selector,
            timeout=15000,
        )
        self.page.select_option(selector, index=1)
        self.settle()
        self.trace(selector)

    def ensure_dependents(self):
        """Branch / Department / Designation bhare hone chahiye. Reset hon to dobara select."""
        for _ in range(4):
            if self.selected_text("#branch_id").startswith("Select"):
                self.pick_by_text("#branch_id", "Ufone")
            if self.selected_text("#department_id").startswith("Select"):
                self.pick_by_text("#department_id", "Ufone Customer Care")
            if self.selected_text("#designation_id").startswith("Select"):
                self.pick_first("#designation_id")
            self.settle()
            if (not self.selected_text("#branch_id").startswith("Select")
                    and not self.selected_text("#department_id").startswith("Select")
                    and not self.selected_text("#designation_id").startswith("Select")):
                break

    def touch_dates(self):
        """Dates dobara chhoo kar app ko validation dobara chalane ka mauka do"""
        self.fill_date("#company_doj", "2026-10-19")
        self.fill_date("#employment_type_effective_date", "2026-10-19")

    def button_enabled(self, timeout_ms=6000):
        btn = self.page.locator(self.submit_btn).last
        end = time.time() + timeout_ms / 1000
        while time.time() < end:
            if btn.is_enabled():
                return True
            self.page.wait_for_timeout(300)
        return False

    def dump_fields(self):
        return self.page.evaluate("""() => {
            const ids = ['name','phone','dob','email','username','password-input','address',
              'cnicInput','emp_no','branch_id','department_id','designation_id','region_id',
              'grade','employment_city','employment_type','employment_status',
              'company_doj','employment_type_effective_date'];
            const out = ids.map(id => {
                const e = document.getElementById(id);
                if (!e) return id + '=NOT FOUND';
                if (e.tagName === 'SELECT')
                    return id + '=' + (e.options[e.selectedIndex] ? e.options[e.selectedIndex].text : '');
                if (id === 'password-input') return id + '=len' + e.value.length;
                return id + '=' + e.value;
            });
            out.push('gender_male=' + document.getElementById('g_male').checked);
            const errs = [...document.querySelectorAll('.text-danger, .error, .invalid-feedback, label.error')]
                .filter(e => e.offsetParent !== null && e.textContent.trim())
                .map(e => e.textContent.trim());
            out.push('VISIBLE_ERRORS=' + JSON.stringify(errs));
            return out;
        }""")

    # ---------- main flow ----------
    def create_new_employee_flow(self):
        page = self.page
        uid = str(int(time.time()))[-7:]                        # numbers (emp no, phone, email)
        uid_letters = "".join(chr(97 + int(c)) for c in uid)    # Name ke liye sirf letters

        # 1. Create New Employee page kholo
        page.click(self.create_new_btn)
        page.wait_for_url(re.compile(r".*/employee/create"))
        page.wait_for_selector("#name", timeout=15000)

        # 2. Personal Detail
        self.fill_box("#name", f"Auto Employee {uid_letters}")
        self.fill_box("#phone", f"033{uid}0")
        self.fill_date("#dob", "1995-05-15")
        page.click("label[for='g_male']")
        self.fill_box("#email", f"atest_{uid}@gmail.com")
        self.fill_box("#username", f"atest_{uid}")
        self.fill_box("#password-input", "EasyPass@1")
        self.fill_box("#address", "123 Test Street, Lahore")
        self.fill_box("#cnicInput", f"35202-{uid}-1")

        # 3. Company Detail
        self.fill_box("#emp_no", f"38{uid}")
        self.pick_by_text("#branch_id", "Ufone")
        self.pick_by_text("#department_id", "Ufone Customer Care")
        self.pick_first("#designation_id")
        self.pick_by_text("#region_id", "Central")
        self.pick_by_text("#grade", "g1")
        self.pick_by_text("#management_level_id", "l2")
        self.pick_by_text("#employment_city", "Adilpur")
        self.pick_by_text("#employment_type", "Outsource")
        self.pick_by_text("#employment_status", "Permanent")
        self.fill_date("#company_doj", "2026-10-19")
        self.fill_date("#employment_type_effective_date", "2026-10-19")

        # 4. Agar app ne kuch reset kiya ho to theek karo, phir validation dobara chalao
        self.ensure_dependents()
        self.touch_dates()
        self.ensure_dependents()
        page.screenshot(path="reports/before_submit.png", full_page=True)

        # 5. Create button: enable hone ka wait, na ho to poora haal error mein likho
        enabled = self.button_enabled(8000)
        if not enabled:
            self.touch_dates()
            enabled = self.button_enabled(6000)
        if not enabled:
            raise AssertionError(
                "Create button disabled raha. FIELDS: " + " | ".join(self.dump_fields())
                + " || TRACE: " + " | ".join(self.trace_log[-14:])
            )

        btn = page.locator(self.submit_btn).last
        btn.scroll_into_view_if_needed()
        btn.click()
        self.settle()

    def verify_employee_created(self):
        page = self.page
        try:
            expect(page).not_to_have_url(re.compile(r".*/employee/create/?$"), timeout=15000)
        except AssertionError:
            page.screenshot(path="reports/after_submit.png", full_page=True)
            msgs = page.evaluate("""() => [...document.querySelectorAll(
                '.invalid-feedback, .text-danger, .alert, .toast, .swal2-popup')]
                .filter(e => e.offsetParent !== null && e.textContent.trim())
                .map(e => e.textContent.trim())""")
            raise AssertionError(
                f"Employee create nahi hua. Page ke errors: {msgs} || TRACE: "
                + " | ".join(self.trace_log[-14:])
            )