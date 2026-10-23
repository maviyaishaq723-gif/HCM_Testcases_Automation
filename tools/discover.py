import time
from playwright.sync_api import sync_playwright

def capture(page):
    print("1. Login kar rahe hain...")
    page.goto("http://172.16.35.74/hcm/login")
    page.fill("input[name='email'], input[type='email']", "nauman.ahmad@ptclgroup.com")
    page.fill("input[name='password'], input[type='password']", "Ufone@123")
    page.click("button[type='submit'], button:has-text('Login')")
    page.wait_for_load_state("networkidle")
    time.sleep(2)

    print("2. Organization Setup page par ja rahe hain...")
    page.goto("http://172.16.35.74/hcm/branch")
    page.wait_for_load_state("networkidle")
    time.sleep(2)

    data = {"department": [], "sub_department": []}

    print("3. Department tab aur modal inspect ho raha hai...")
    dept_tab = page.locator("a:has-text('Department')").first
    if dept_tab.is_visible():
        dept_tab.click()
        page.wait_for_load_state("networkidle")
        time.sleep(3)
        
        # Add button click karne ke liye broader selector
        add_btn = page.locator("a:has-text('Department'), a.btn, button.btn").filter(has_text=re.compile(r"Add|Create", re.IGNORECASE)).first
        if not add_btn.is_visible():
            add_btn = page.locator("a:has-text('Add'), button:has-text('Add'), a:has-text('Create')").first
            
        if add_btn.is_visible():
            add_btn.click()
            time.sleep(2)
            
            # Modal inputs capture karein
            inputs = page.locator("div.modal input, form input, input[type='text'], input.form-control").all()
            for el in inputs:
                try:
                    if el.is_visible():
                        data["department"].append(f"Input Name: {el.get_attribute('name')} | ID: {el.get_attribute('id')} | Placeholder: {el.get_attribute('placeholder')}")
                except:
                    pass
            
            # Modal buttons capture karein
            buttons = page.locator("div.modal button, div.modal .btn, form button").all()
            for el in buttons:
                try:
                    if el.is_visible():
                        data["department"].append(f"Button Text: {el.inner_text().strip()} | Class: {el.get_attribute('class')}")
                except:
                    pass
            
            # Modal close karein
            close_btn = page.locator("div.modal button.btn-close, div.modal button:has-text('Cancel')").first
            if close_btn.is_visible():
                close_btn.click()
                time.sleep(1)

    print("4. Sub Department tab aur modal inspect ho raha hai...")
    sub_dept_tab = page.locator("a:has-text('Sub Department')").first
    if sub_dept_tab.is_visible():
        sub_dept_tab.click()
        page.wait_for_load_state("networkidle")
        time.sleep(3)
        
        add_sub_btn = page.locator("a:has-text('Sub Department'), a.btn, button.btn").filter(has_text=re.compile(r"Add|Create", re.IGNORECASE)).first
        if not add_sub_btn.is_visible():
            add_sub_btn = page.locator("a:has-text('Add'), button:has-text('Add'), a:has-text('Create')").first
            
        if add_sub_btn.is_visible():
            add_sub_btn.click()
            time.sleep(2)
            
            inputs = page.locator("div.modal input, form input, input[type='text'], input.form-control").all()
            for el in inputs:
                try:
                    if el.is_visible():
                        data["sub_department"].append(f"SubDept Input Name: {el.get_attribute('name')} | ID: {el.get_attribute('id')} | Placeholder: {el.get_attribute('placeholder')}")
                except:
                    pass
            
            buttons = page.locator("div.modal button, div.modal .btn, form button").all()
            for el in buttons:
                try:
                    if el.is_visible():
                        data["sub_department"].append(f"SubDept Button Text: {el.inner_text().strip()} | Class: {el.get_attribute('class')}")
                except:
                    pass

    return data

def save(data):
    filename = "tools/output/discover_output.txt"
    import re
    with open(filename, "w", encoding="utf-8") as f:
        f.write("--- DEPARTMENT LOCATORS ---\n")
        for item in data["department"]:
            f.write(item + "\n")
        f.write("\n--- SUB DEPARTMENT LOCATORS ---\n")
        for item in data["sub_department"]:
            f.write(item + "\n")
    return filename

if __name__ == "__main__":
    import re
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        data = capture(page)
        path = save(data)
        print(f"Discovery complete! File saved at: {path}")
        browser.close()