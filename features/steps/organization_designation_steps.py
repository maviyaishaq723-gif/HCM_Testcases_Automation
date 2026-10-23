from behave import given, when, then
from pages.organization_designation_page import OrganizationDesignationPage
import random

@when('User clicks on the Designation tab')
def step_click_designation_tab(context):
    context.desig_page = OrganizationDesignationPage(context.page)
    context.desig_page.click_designation_tab()

@when('User clicks on Add New Designation button')
def step_click_add_designation(context):
    context.desig_page.click_add_designation_btn()

@when('User fills the designation form with valid data and clicks Create')
def step_fill_designation_form(context):
    # Name strictly under 20 characters limit & unique
    context.desig_name = f"Desig_{random.randint(100, 999)}"
    context.desig_page.fill_designation_form(context.desig_name)

@then('The new designation should be created and displayed in the designation list successfully')
def step_verify_designation(context):
    context.desig_page.verify_designation_created(context.desig_name)