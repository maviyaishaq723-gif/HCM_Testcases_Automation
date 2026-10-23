from behave import given, when, then
from pages.organization_competencies_page import OrganizationCompetenciesPage
import random

@when('User clicks on the Competencies tab')
def step_click_competencies_tab(context):
    context.competencies_page = OrganizationCompetenciesPage(context.page)
    context.competencies_page.click_competencies_tab()

@when('User clicks on Add New Competencies button')
def step_click_add_competencies(context):
    context.competencies_page.click_add_competencies_btn()

@when('User fills the competencies form with name and selects type from dropdown and clicks Create')
def step_fill_competencies_form(context):
    context.competency_name = f"Competency_{random.randint(100, 999)}"
    context.competencies_page.fill_competencies_form(context.competency_name, competency_type="Individual")

@then('The new competencies should be created and displayed in the competencies list successfully')
def step_verify_competencies(context):
    context.competencies_page.verify_competencies_created(context.competency_name)