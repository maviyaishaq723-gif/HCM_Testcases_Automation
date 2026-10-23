class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        self.page.goto(url, wait_until="networkidle")

    def click(self, selector):
        self.page.wait_for_selector(selector, state="visible")
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.wait_for_selector(selector, state="visible")
        self.page.fill(selector, value)

    def get_text(self, selector):
        self.page.wait_for_selector(selector, state="visible")
        return self.page.inner_text(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)