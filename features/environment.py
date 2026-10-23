import os
from datetime import datetime
from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=300)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_viewport_size({"width": 1366, "height": 768})

def after_scenario(context, scenario):
    if scenario.status == "failed":
        if not os.path.exists("reports/screenshots"):
            os.makedirs("reports/screenshots")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"reports/screenshots/failed_{scenario.name}_{timestamp}.png"
        context.page.screenshot(path=screenshot_path)

    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()