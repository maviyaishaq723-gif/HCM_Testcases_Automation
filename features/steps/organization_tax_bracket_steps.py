from behave import given, when, then
from pages.organization_tax_bracket_page import OrganizationTaxBracketPage
import random

@when('User clicks on the Tax Bracket tab')
def step_click_tax_bracket_tab(context):
    context.taxbracket_page = OrganizationTaxBracketPage(context.page)
    context.taxbracket_page.click_tax_bracket_tab()

@when('User clicks on Add New Tax Bracket button')
def step_click_add_tax_bracket(context):
    context.taxbracket_page.click_add_tax_bracket_btn()

@when('User fills the tax bracket form with valid data and clicks Submit')
def step_fill_tax_bracket_form(context):
    # Generating unique numbers for tax bracket
    context.income_over = random.randint(7000000, 8000000)
    context.income_not_over = context.income_over + 1000000
    context.tax_col1 = random.randint(100000, 500000)
    context.tax_excess = random.randint(10, 30)

    context.taxbracket_page.fill_tax_bracket_form(
        context.income_over,
        context.income_not_over,
        context.tax_col1,
        context.tax_excess
    )

@then('The new tax bracket should be created and displayed in the tax bracket list successfully')
def step_verify_tax_bracket(context):
    context.taxbracket_page.verify_tax_bracket_created(context.income_over)