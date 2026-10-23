from behave import given, when, then
from pages.organization_fiscal_year_page import OrganizationFiscalYearPage
import random

@when('User clicks on the Fiscal Year tab')
def step_click_fiscal_year_tab(context):
    context.fiscalyear_page = OrganizationFiscalYearPage(context.page)
    context.fiscalyear_page.click_fiscal_year_tab()

@when('User clicks on Add New Fiscal Year button')
def step_click_add_fiscal_year(context):
    context.fiscalyear_page.click_add_fiscal_year_btn()

@when('User fills the fiscal year form with valid data and clicks Create')
def step_fill_fiscal_year_form(context):
    start_year = random.randint(2030, 2080)
    context.fiscal_year_name = f"{start_year}-{start_year + 1}"
    context.fiscalyear_page.fill_fiscal_year_form(context.fiscal_year_name)

@then('The new fiscal year should be created and displayed in the fiscal year list successfully')
def step_verify_fiscal_year(context):
    context.fiscalyear_page.verify_fiscal_year_created(context.fiscal_year_name)