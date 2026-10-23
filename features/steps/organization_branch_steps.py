import time
from behave import when, then
from pages.organization_branch_page import OrganizationBranchPage

@when('User navigates to the Organization Setup section')
def step_navigate_org(context):
    context.org_page = OrganizationBranchPage(context.page)
    context.org_page.navigate_to_branch()

@when('User clicks on Create New Branch button')
def step_click_create(context):
    context.org_page.click_create_branch()

@when('User fills the branch form with valid data and clicks Save')
def step_fill_branch_form(context):
    # Har run par unique name banane ke liye current timestamp attach kar rahe hain
    context.branch_name = f"Auto Branch {int(time.time())}"
    context.org_page.fill_branch_form(context.branch_name)

@then('The new branch should be created and displayed in the branch list successfully')
def step_verify_branch_created(context):
    # Wahi unique branch name search karke verify hoga
    context.org_page.verify_branch_created(context.branch_name)