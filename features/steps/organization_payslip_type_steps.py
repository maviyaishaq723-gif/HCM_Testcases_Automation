from behave import given, when, then
from pages.organization_payslip_type_page import OrganizationPayslipTypePage
import random

@when('User clicks on the Payslip Type tab')
def step_click_payslip_type_tab(context):
    context.paysliptype_page = OrganizationPayslipTypePage(context.page)
    context.paysliptype_page.click_payslip_type_tab()

@when('User clicks on Add New Payslip Type button')
def step_click_add_payslip_type(context):
    context.paysliptype_page.click_add_payslip_type_btn()

@when('User fills the payslip type form with valid data and clicks Create')
def step_fill_payslip_type_form(context):
    context.payslip_name = f"Payslip_{random.randint(100, 999)}"
    context.paysliptype_page.fill_payslip_type_form(context.payslip_name)

@then('The new payslip type should be created and displayed in the payslip type list successfully')
def step_verify_payslip_type(context):
    context.paysliptype_page.verify_payslip_type_created(context.payslip_name)