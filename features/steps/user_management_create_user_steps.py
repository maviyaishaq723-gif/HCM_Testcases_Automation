import uuid
from datetime import datetime
from behave import when, then
from pages.user_management_create_user_page import UserManagementCreateUserPage


@when('User navigates to the User Management section')
def step_navigate_user_mgmt(context):
    context.create_user_page = UserManagementCreateUserPage(context.page)
    context.create_user_page.navigate_to_user_management()


@when('User clicks on the User tab')
def step_click_user_tab(context):
    context.create_user_page.click_user_tab()


@when('User clicks on Add New User button')
def step_click_add_user(context):
    context.create_user_page.click_add_new_user_btn()


@when('User fills the user form with valid data and selects role and clicks Create')
def step_fill_user_form(context):
    unique = f"{datetime.now():%Y%m%d%H%M%S}{uuid.uuid4().hex[:4]}"
    context.user_name = f"TestUser{unique}"
    context.user_email = f"testuser{unique}@gmail.com"
    context.create_user_page.fill_user_form(
        name=context.user_name,
        email=context.user_email,
        password="Test@1234",
        role_name="hr",
    )


@then('The new user should be created and displayed in the user list successfully')
def step_verify_user(context):
    context.create_user_page.verify_user_created(context.user_name)