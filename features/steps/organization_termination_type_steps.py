from behave import given, when, then
from pages.organization_termination_type_page import OrganizationTerminationTypePage
import random

@when('User clicks on the Termination Type tab')
def step_click_termination_type_tab(context):
    context.terminationtype_page = OrganizationTerminationTypePage(context.page)
    context.terminationtype_page.click_termination_type_tab()

@when('User clicks on Add New Termination Type button')
def step_click_add_termination_type(context):
    context.terminationtype_page.click_add_termination_type_btn()

@when('User fills the termination type form with valid data and clicks Create')
def step_fill_termination_type_form(context):
    context.termination_name = f"Termination_{random.randint(100, 999)}"
    context.terminationtype_page.fill_termination_type_form(context.termination_name)

@then('The new termination type should be created and displayed in the termination type list successfully')
def step_verify_termination_type(context):
    context.terminationtype_page.verify_termination_type_created(context.termination_name)