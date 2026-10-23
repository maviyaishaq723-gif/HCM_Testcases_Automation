from behave import when, then
from pages.employee_messenger_page import EmployeeMessengerPage

@when('User clicks on the header message icon and clicks View All')
def step_click_view_all_messages(context):
    context.messenger_page = EmployeeMessengerPage(context.page)
    context.messenger_page.click_view_all_messages()

@then('The Messenger page should open successfully')
def step_verify_messenger_opened(context):
    context.messenger_page.verify_messenger_opened()

@when('User selects a chat from the messenger list')
def step_select_chat(context):
    context.messenger_page.select_chat()

@when('User types an automated test message and clicks send')
def step_send_message(context):
    context.messenger_page.send_message("Hello, this is an automated test message.")

@then('The message should be sent successfully in the chat')
def step_verify_message_sent(context):
    context.messenger_page.verify_message_sent()