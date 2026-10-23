from behave import given, when, then
from pages.organization_deduction_option_page import OrganizationDeductionOptionPage
import random

@when('User clicks on the Deduction Option tab')
def step_click_deduction_option_tab(context):
    context.deductionoption_page = OrganizationDeductionOptionPage(context.page)
    context.deductionoption_page.click_deduction_option_tab()

@when('User clicks on Add New Deduction Option button')
def step_click_add_deduction_option(context):
    context.deductionoption_page.click_add_deduction_option_btn()

@when('User fills the deduction option form with valid data and clicks Create')
def step_fill_deduction_option_form(context):
    context.deduction_name = f"Deduction_{random.randint(100, 999)}"
    context.deductionoption_page.fill_deduction_option_form(context.deduction_name)

@then('The new deduction option should be created and displayed in the deduction option list successfully')
def step_verify_deduction_option(context):
    context.deductionoption_page.verify_deduction_option_created(context.deduction_name)