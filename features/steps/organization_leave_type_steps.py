from behave import given, when, then
from pages.organization_leave_type_page import OrganizationLeaveTypePage
import random

@when('User clicks on the Leave Type tab')
def step_click_leave_type_tab(context):
    context.leavetype_page = OrganizationLeaveTypePage(context.page)
    context.leavetype_page.click_leave_type_tab()

@when('User clicks on Add New Leave Type button')
def step_click_add_leave_type(context):
    context.leavetype_page.click_add_leave_type_btn()

@when('User fills the leave type form with valid data and clicks Create')
def step_fill_leave_type_form(context):
    context.leave_name = f"Leave_{random.randint(100, 999)}"
    context.leavetype_page.fill_leave_type_form(context.leave_name, days_val="90")

@then('The new leave type should be created and displayed in the leave type list successfully')
def step_verify_leave_type(context):
    context.leavetype_page.verify_leave_type_created(context.leave_name)