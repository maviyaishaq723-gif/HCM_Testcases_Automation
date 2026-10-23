from behave import when, then
from pages.employee_edit_page import EmployeeEditPage


@when('User clicks the edit button for a test employee')
def step_open_edit(context):
    context.employee_edit_page = EmployeeEditPage(context.page)
    context.employee_edit_page.open_edit_for_test_employee()


@when('User updates the employee details and saves')
def step_update_and_save(context):
    context.updated_details = context.employee_edit_page.update_details_and_save()


@then('The employee details should be updated successfully')
def step_verify_updated(context):
    context.employee_edit_page.verify_updated(context.updated_details)