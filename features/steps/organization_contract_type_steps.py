from behave import given, when, then
from pages.organization_contract_type_page import OrganizationContractTypePage
import random

@when('User clicks on the Contract Type tab')
def step_click_contract_type_tab(context):
    context.contracttype_page = OrganizationContractTypePage(context.page)
    context.contracttype_page.click_contract_type_tab()

@when('User clicks on Add New Contract Type button')
def step_click_add_contract_type(context):
    context.contracttype_page.click_add_contract_type_btn()

@when('User fills the contract type form with valid data and clicks Create')
def step_fill_contract_type_form(context):
    context.contract_name = f"Contract_{random.randint(100, 999)}"
    context.contracttype_page.fill_contract_type_form(context.contract_name)

@then('The new contract type should be created and displayed in the contract type list successfully')
def step_verify_contract_type(context):
    context.contracttype_page.verify_contract_type_created(context.contract_name)