from behave import given, when, then
from pages.organization_loan_option_page import OrganizationLoanOptionPage
import random

@when('User clicks on the Loan Option tab')
def step_click_loan_option_tab(context):
    context.loanoption_page = OrganizationLoanOptionPage(context.page)
    context.loanoption_page.click_loan_option_tab()

@when('User clicks on Add New Loan Option button')
def step_click_add_loan_option(context):
    context.loanoption_page.click_add_loan_option_btn()

@when('User fills the loan option form with valid data and clicks Create')
def step_fill_loan_option_form(context):
    context.loan_name = f"Loan_{random.randint(100, 999)}"
    context.loanoption_page.fill_loan_option_form(context.loan_name)

@then('The new loan option should be created and displayed in the loan option list successfully')
def step_verify_loan_option(context):
    context.loanoption_page.verify_loan_option_created(context.loan_name)