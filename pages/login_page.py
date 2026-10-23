from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "input[name='email']"
        self.password_input = "input#password"
        self.login_btn = "button[type='submit']"

    def login_to_hcm(self, url, email, password):
        self.navigate_to(url)
        if self.is_visible(self.email_input):
            self.fill(self.email_input, email)
            self.fill(self.password_input, password)
            self.click(self.login_btn)