from behave import given, when, then
from pages.organization_allowance_type_page import OrganizationAllowanceTypePage
import random

@when('User clicks on the Allowance Type tab')
def step_click_allowance_type_tab(context):
    context.allowancetype_page = OrganizationAllowanceTypePage(context.page)
    context.allowancetype_page.click_allowance_type_tab()

@when('User clicks on Add New Allowance Type button')
def step_click_add_allowance_type(context):
    context.allowancetype_page.click_add_allowance_type_btn()

@when('User fills the allowance type form with valid data and clicks Create')
def step_fill_allowance_type_form(context):
    context.allowance_name = f"Allowance_{random.randint(100, 999)}"
    context.allowancetype_page.fill_allowance_type_form(context.allowance_name)

@then('The new allowance type should be created and displayed in the allowance type list successfully')
def step_verify_allowance_type(context):
    context.allowancetype_page.verify_allowance_type_created(context.allowance_name)