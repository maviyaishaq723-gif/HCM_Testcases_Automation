from behave import given, when, then
from pages.login_page import LoginPage
from pages.meeting_page import MeetingPage

@given('User is logged into HCM application with valid credentials')
def step_impl(context):
    login_page = LoginPage(context.page)
    # Aapka exact portal URL aur credentials
    login_page.login_to_hcm(
        url="http://172.16.35.74/hcm/login",
        email="nauman.ahmad@ptclgroup.com",
        password="Ufone@123"
    )

@when('User navigates to the Meeting module')
def step_impl(context):
    meeting_page = MeetingPage(context.page)
    meeting_page.navigate_to_meeting()

@when('User creates a new meeting with required details')
def step_impl(context):
    meeting_page = MeetingPage(context.page)
    meeting_page.create_meeting()

@when('User edits the first meeting from the list')
def step_impl(context):
    meeting_page = MeetingPage(context.page)
    meeting_page.edit_first_meeting()

@when('User deletes the first meeting from the list')
def step_impl(context):
    meeting_page = MeetingPage(context.page)
    meeting_page.delete_first_meeting()

@then('Meeting should be successfully created')
@then('Meeting should be successfully edited')
@then('Meeting should be successfully deleted')
def step_impl(context):
    meeting_page = MeetingPage(context.page)
    # Agar toast message ya success indicator visible ho toh test pass hoga
    assert meeting_page.verify_success_action(), "Action completed successfully, but success notification was not verified!"