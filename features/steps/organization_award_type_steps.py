from behave import given, when, then
from pages.organization_award_type_page import OrganizationAwardTypePage
import random

@when('User clicks on the Award Type tab')
def step_click_award_type_tab(context):
    context.awardtype_page = OrganizationAwardTypePage(context.page)
    context.awardtype_page.click_award_type_tab()

@when('User clicks on Add New Award Type button')
def step_click_add_award_type(context):
    context.awardtype_page.click_add_award_type_btn()

@when('User fills the award type form with valid data and clicks Create')
def step_fill_award_type_form(context):
    context.award_name = f"Award_{random.randint(100, 999)}"
    context.awardtype_page.fill_award_type_form(context.award_name)

@then('The new award type should be created and displayed in the award type list successfully')
def step_verify_award_type(context):
    context.awardtype_page.verify_award_type_created(context.award_name)