from behave import given, when, then
from pages.organization_training_type_page import OrganizationTrainingTypePage
import random

@when('User clicks on the Training Type tab')
def step_click_training_type_tab(context):
    context.trainingtype_page = OrganizationTrainingTypePage(context.page)
    context.trainingtype_page.click_training_type_tab()

@when('User clicks on Add New Training Type button')
def step_click_add_training_type(context):
    context.trainingtype_page.click_add_training_type_btn()

@when('User fills the training type form with valid data and clicks Create')
def step_fill_training_type_form(context):
    context.training_name = f"Training_{random.randint(100, 999)}"
    context.trainingtype_page.fill_training_type_form(context.training_name)

@then('The new training type should be created and displayed in the training type list successfully')
def step_verify_training_type(context):
    context.trainingtype_page.verify_training_type_created(context.training_name)