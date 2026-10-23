from behave import given, when, then
from pages.user_management_logs_page import UserManagementLogsPage


@when('User opens the Users page')
def step_open_users(context):
    context.logs_page = UserManagementLogsPage(context.page)
    context.logs_page.open_users_page()


@when('User clicks on the Manage User Logs History button')
def step_click_logs_btn(context):
    context.logs_page.click_logs_button()


@then('The Manage User Logs History page should be opened')
def step_verify_logs_page(context):
    context.logs_page.verify_logs_page_opened()


@given('User is on the Manage User Logs History page')
def step_on_logs_page(context):
    context.logs_page = UserManagementLogsPage(context.page)
    context.logs_page.open_logs_page()


@when('User selects the current month and an employee and clicks search')
def step_apply_filter(context):
    context.logs_page.apply_filter()


@then('The filter should be applied and the logs table should be displayed')
def step_verify_filter(context):
    context.logs_page.verify_filter_applied()


@when('User applies the filter and clicks the reset button')
def step_filter_then_reset(context):
    context.logs_page.apply_filter()
    context.logs_page.click_reset()


@then('The filter should be reset to default')
def step_verify_reset(context):
    context.logs_page.verify_filter_reset()


@when('User searches an existing user name in the logs search bar')
def step_search(context):
    context.logs_page.search_existing_name()


@then('Only the logs matching that user name should be displayed')
def step_verify_search(context):
    context.logs_page.verify_search_results()


@when('User clicks the view button of the first log')
def step_view_log(context):
    context.logs_page.click_view_first_log()


@then('The log details popup should be displayed')
def step_verify_popup(context):
    context.logs_page.verify_log_details_popup()


@when('User clicks the delete button of the first log and confirms with Yes')
def step_delete_log(context):
    context.logs_page.click_delete_first_log()
    context.logs_page.confirm_delete()


@then('That log should be deleted successfully')
def step_verify_deleted(context):
    context.logs_page.verify_log_deleted()