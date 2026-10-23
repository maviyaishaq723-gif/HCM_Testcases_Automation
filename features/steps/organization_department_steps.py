import time
import random
from behave import when, then
from pages.organization_department_page import OrganizationDepartmentPage

@when('User clicks on the Department tab')
def step_click_dept_tab(context):
    context.dept_page = OrganizationDepartmentPage(context.page)
    context.dept_page.click_department_tab()

@when('User clicks on Add New Department button')
def step_click_add_dept(context):
    context.dept_page.click_add_department_btn()

@when('User fills the department form with valid data and clicks Create')
def step_fill_dept_form(context):
    context.dept_name = f"Auto Dept {int(time.time())}"
    context.dept_page.fill_department_form(context.dept_name)

@then('The new department should be created and displayed in the department list successfully')
def step_verify_dept(context):
    context.dept_page.verify_department_created(context.dept_name)

@when('User clicks on the Sub Department tab')
def step_click_subdept_tab(context):
    context.dept_page = OrganizationDepartmentPage(context.page)
    context.dept_page.click_sub_department_tab()

@when('User clicks on Add New Sub Department button')
def step_click_add_subdept(context):
    context.dept_page.click_add_sub_department_btn()

@when('User fills the sub department form with valid data and clicks Create')
def step_fill_subdept_form(context):
    context.subdept_name = f"Sub_{random.randint(10, 99)}"
    context.dept_page.fill_sub_department_form(context.subdept_name)

@then('The new sub department should be created and displayed in the sub department list successfully')
def step_verify_subdept(context):
    context.dept_page.verify_sub_department_created(context.subdept_name)