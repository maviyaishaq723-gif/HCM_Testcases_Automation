from behave import given, when, then
from pages.organization_employment_status_page import OrganizationEmploymentStatusPage
import random

@when('User clicks on the Employment Status tab')
def step_click_emp_status_tab(context):
    context.empstatus_page = OrganizationEmploymentStatusPage(context.page)
    context.empstatus_page.click_emp_status_tab()

@when('User clicks on Add New Employment Status button')
def step_click_add_emp_status(context):
    context.empstatus_page.click_add_emp_status_btn()

@when('User fills the employment status form with valid data and clicks Create')
def step_fill_emp_status_form(context):
    context.status_name = f"EmpStatus_{random.randint(100, 999)}"
    context.empstatus_page.fill_emp_status_form(context.status_name)

@then('The new employment status should be created and displayed in the employment status list successfully')
def step_verify_emp_status(context):
    context.empstatus_page.verify_emp_status_created(context.status_name)