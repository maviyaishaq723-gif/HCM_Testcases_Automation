from behave import when, then
from pages.employee_create_page import EmployeeCreatePage


@when('User fills out the create new employee form with unique details')
def step_fill_employee_form(context):
    context.employee_create_page = EmployeeCreatePage(context.page)
    context.employee_create_page.create_new_employee_flow()


@then('A new employee should be created successfully')
def step_verify_employee_created(context):
    context.employee_create_page.verify_employee_created()