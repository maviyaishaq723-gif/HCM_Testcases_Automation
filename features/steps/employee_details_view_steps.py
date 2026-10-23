from behave import when, then
from pages.employee_details_view_page import EmployeeDetailsViewPage


@when('User clicks on an employee ID from the list')
def step_click_employee_id(context):
    context.details_view_page = EmployeeDetailsViewPage(context.page)
    context.details_view_page.open_first_employee_details()


@then('Employee details page should open with detailed information')
def step_verify_details_page(context):
    context.details_view_page.verify_details_page()