from behave import when, then
from pages.role_management_page import RoleManagementPage


@when('User navigates to the Role page')
def step_navigate_role(context):
    context.role_page = RoleManagementPage(context.page)
    context.role_page.navigate_to_role_page()


@when('User clicks on Create New Role button')
def step_click_create_role(context):
    context.role_page.click_create_new_role()


@when('User fills the role form with an already existing role name and clicks Create')
def step_create_existing_role(context):
    context.role_page.create_role_with_existing_name()


@then('An error should be displayed that the role already exists')
def step_verify_error(context):
    context.role_page.verify_role_already_exists_error()


@when('User searches an existing role in the roles search bar')
def step_search_role(context):
    context.role_page.search_existing_role()


@then('Only the roles matching the searched name should be displayed')
def step_verify_search(context):
    context.role_page.verify_role_search_results()