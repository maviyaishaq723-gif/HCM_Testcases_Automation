from behave import when, then
from pages.employee_joining_letter_page import EmployeeJoiningLetterPage


@when('User clicks on Joining Letter and selects PDF')
def step_generate_joining_letter(context):
    context.joining_letter_page = EmployeeJoiningLetterPage(context.page)
    context.joining_letter_page.generate_joining_letter_pdf()


@then('The joining letter should be generated and displayed in a new tab')
def step_verify_joining_letter(context):
    context.joining_letter_page.verify_letter_generated()