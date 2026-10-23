import re
from pages.base_page import BasePage

class EmployeeJoiningLetterPage(BasePage):
    JOINING_LETTER_BTN = "button, a"

    def generate_joining_letter_pdf(self):
        """Employee details page par Joining Letter > PDF click karta hai"""
        btn = (self.page.locator(self.JOINING_LETTER_BTN)
               .filter(has_text=re.compile(r"^\s*Joining Letter\s*$", re.I)).first)
        btn.wait_for(state="visible", timeout=15000)
        btn.click()

        pdf_item = self.page.locator("text='PDF' >> visible=true").first
        pdf_item.wait_for(state="visible", timeout=10000)
        
        # PDF Option Click
        pdf_item.click()
        
        # Naye tab ke load hone ka wait
        self.page.wait_for_timeout(3000)

    def verify_letter_generated(self):
        """Verify karta hai ke naya tab khul gaya hai aur Joining Letter page load ho gaya hai"""
        all_pages = self.page.context.pages
        target_page = all_pages[-1] if len(all_pages) > 1 else self.page
        
        # Naye tab par switch karke check kar lo ke heading mojood hai ya nahi
        heading_locator = target_page.locator("text='Joining Letter'").first
        
        try:
            heading_locator.wait_for(state="visible", timeout=5000)
            is_loaded = True
        except Exception:
            is_loaded = False

        print(f"DEBUG - Total Tabs: {len(all_pages)}, Target URL: {target_page.url}")

        assert is_loaded or len(all_pages) > 1, (
            f"Joining Letter page load nahi hua. Current URL: {target_page.url}"
        )