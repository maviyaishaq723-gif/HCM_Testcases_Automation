from behave import given, when, then
from pages.organization_performance_type_page import OrganizationPerformanceTypePage
import random

@when('User clicks on the Performance Type tab')
def step_click_performance_type_tab(context):
    context.performancetype_page = OrganizationPerformanceTypePage(context.page)
    context.performancetype_page.click_performance_type_tab()

@when('User clicks on Add New Performance Type button')
def step_click_add_performance_type(context):
    context.performancetype_page.click_add_performance_type_btn()

@when('User fills the performance type form with valid data and clicks Create')
def step_fill_performance_type_form(context):
    context.performance_name = f"Performance_{random.randint(100, 999)}"
    context.performancetype_page.fill_performance_type_form(context.performance_name)

@then('The new performance type should be created and displayed in the performance type list successfully')
def step_verify_performance_type(context):
    context.performancetype_page.verify_performance_type_created(context.performance_name)