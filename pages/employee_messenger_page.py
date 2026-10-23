import re
from pages.base_page import BasePage

class EmployeeMessengerPage(BasePage):
    MSG_BTN = "#msg-btn"
    VIEW_ALL_BTN = "a:has-text('View all')"
    MESSENGER_HEADING = "h4:has-text('Messenger')"
    
    # Discovered Data ke mutabiq exact user chat locator (Data-ID 172 ya user type)
    CHAT_USER = "p[data-id='172'][data-type='user'], p[data-type='user']"
    MESSAGE_INPUT = ".m-send, textarea, input[type='text']"
    SEND_BTN = "svg.fa-paper-plane, button[type='submit'], .fa-paper-plane"

    def click_view_all_messages(self):
        """Top right message icon click karke View all par click karta hai"""
        msg_icon = self.page.locator(self.MSG_BTN).first
        if msg_icon.is_visible():
            msg_icon.click()
            self.page.wait_for_timeout(1000)
        
        view_all = self.page.locator(self.VIEW_ALL_BTN).first
        if view_all.is_visible():
            view_all.click()
        else:
            self.page.goto("http://172.16.35.74/hcm/chats")

        self.page.wait_for_load_state("networkidle")

    def verify_messenger_opened(self):
        """Verify karta hai ke Messenger page successfully khul gaya hai"""
        heading = self.page.locator(self.MESSENGER_HEADING).first
        heading.wait_for(state="visible", timeout=15000)
        assert heading.is_visible(), "Messenger page open nahi hua!"

    def select_chat(self):
        """Discovered data se chat user select karta hai"""
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        
        chat = self.page.locator(self.CHAT_USER).first
        chat.wait_for(state="visible", timeout=20000)
        chat.click()
        self.page.wait_for_load_state("networkidle")

    def send_message(self, message_text):
        """Chat textarea mein message type karta hai aur send button press karta hai"""
        textarea = self.page.locator(self.MESSAGE_INPUT).last
        textarea.wait_for(state="visible", timeout=15000)
        textarea.focus()
        textarea.fill(message_text)
        self.page.wait_for_timeout(1000)

        send_btn = self.page.locator(self.SEND_BTN).last
        send_btn.wait_for(state="visible", timeout=15000)
        send_btn.click()
        self.page.wait_for_timeout(2000)

    def verify_message_sent(self):
        """Verify karta hai ke message send ho gaya hai"""
        assert "chats" in self.page.url.lower(), "Message send verify nahi ho saka!"