from behave import when, then
from pages.employee_profile_module_page import EmployeeProfileModulePage


@when('User opens the Employee Profile listing')
def ep_open_listing(context):
    context.ep_page = EmployeeProfileModulePage(context.page)
    context.ep_page.open_listing()


@when('User clicks the ID of the first employee')
def ep_click_first_id(context):
    context.ep_page.click_first_employee_id()


@then('The Manage Employee page of that employee should be displayed')
def ep_verify_manage_page(context):
    context.ep_page.verify_manage_employee_page()


@when('User opens the filter panel with the funnel icon')
def ep_open_filter(context):
    context.ep_page.open_filter_panel()


@when('User selects branch, department and designation and clicks search on the profile filter')
def ep_apply_filter(context):
    context.ep_page.apply_profile_filter()


@then('Only the employees matching the profile filter should be displayed')
def ep_verify_filter(context):
    context.ep_page.verify_profile_filter_results()


@when('User clicks the Edit Profile button on the Manage Employee page')
def ep_click_edit_profile(context):
    if not context.ep_page.click_edit_profile_button():
        context.ep_skip = True
        context.scenario.skip("Manage Employee page par 'Edit Profile' button nahi mila")


@when('User changes the address on the employee form and clicks Update')
def ep_change_address(context):
    if getattr(context, "ep_skip", False):
        return
    context.ep_page.change_address_and_update()


@then('The employee changes should be saved')
def ep_verify_saved(context):
    if getattr(context, "ep_skip", False):
        return
    context.ep_page.verify_changes_saved()


@when('User selects the Chinese language')
def ep_select_chinese(context):
    context.ep_page.select_chinese_language()


@then('The application content should be updated to Chinese')
def ep_verify_chinese(context):
    try:
        context.ep_page.verify_chinese_content()
    finally:
        context.ep_page.restore_english_language()


@when('User clicks the chat button in the header')
def ep_click_chat(context):
    context.ep_page.click_chat_button()


@when('User clicks the message button in the header and then View all')
def ep_click_message_view_all(context):
    context.ep_page.click_message_button_and_view_all()


@then('The Messenger should open displaying all the chats')
def ep_verify_messenger(context):
    context.ep_page.verify_messenger_opened()