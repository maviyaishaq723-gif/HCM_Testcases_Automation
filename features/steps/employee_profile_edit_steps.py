from behave import when, then
from pages.employee_profile_edit_page import EmployeeProfileEditPage

@when('User clicks on Edit Profile button from profile view')
def step_click_edit_profile_view(context):
    context.employee_profile_edit_page = EmployeeProfileEditPage(context.page)
    context.employee_profile_edit_page.click_edit_profile_button()

@when('User updates details and clicks Update button')
def step_update_profile_details(context):
    context.employee_profile_edit_page.update_profile_and_save()

@then('The employee profile details should be updated successfully from profile')
def step_verify_profile_updated_view(context):
    context.employee_profile_edit_page.verify_profile_updated()