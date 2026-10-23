from behave import given, when, then
from pages.organization_goal_type_page import OrganizationGoalTypePage
import random

@when('User clicks on the Goal Type tab')
def step_click_goal_type_tab(context):
    context.goaltype_page = OrganizationGoalTypePage(context.page)
    context.goaltype_page.click_goal_type_tab()

@when('User clicks on Add New Goal Type button')
def step_click_add_goal_type(context):
    context.goaltype_page.click_add_goal_type_btn()

@when('User fills the goal type form with valid data and clicks Create')
def step_fill_goal_type_form(context):
    context.goal_name = f"Goal_{random.randint(100, 999)}"
    context.goaltype_page.fill_goal_type_form(context.goal_name)

@then('The new goal type should be created and displayed in the goal type list successfully')
def step_verify_goal_type(context):
    context.goaltype_page.verify_goal_type_created(context.goal_name)