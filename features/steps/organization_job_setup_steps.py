from behave import given, when, then
from pages.organization_job_setup_page import OrganizationJobSetupPage
import random

# --- Job Category Steps ---
@when('User clicks on the Job Category tab')
def step_click_job_category_tab(context):
    context.jobsetup_page = OrganizationJobSetupPage(context.page)
    context.jobsetup_page.click_job_category_tab()

@when('User clicks on Add New Job Category button')
def step_click_add_job_category(context):
    context.jobsetup_page.click_add_job_category_btn()

@when('User fills the job category form with valid data and clicks Create')
def step_fill_job_category_form(context):
    context.category_name = f"JobCategory_{random.randint(100, 999)}"
    context.jobsetup_page.fill_job_category_form(context.category_name)

@then('The new job category should be created and displayed in the job category list successfully')
def step_verify_job_category(context):
    context.jobsetup_page.verify_job_category_created(context.category_name)

# --- Job Stage Steps ---
@when('User clicks on the Job Stage tab')
def step_click_job_stage_tab(context):
    context.jobsetup_page = OrganizationJobSetupPage(context.page)
    context.jobsetup_page.click_job_stage_tab()

@when('User clicks on Add New Job Stage button')
def step_click_add_job_stage(context):
    context.jobsetup_page.click_add_job_stage_btn()

@when('User fills the job stage form with valid data and clicks Create')
def step_fill_job_stage_form(context):
    context.stage_name = f"JobStage_{random.randint(100, 999)}"
    context.jobsetup_page.fill_job_stage_form(context.stage_name)

@then('The new job stage should be created and displayed in the job stage list successfully')
def step_verify_job_stage(context):
    context.jobsetup_page.verify_job_stage_created(context.stage_name)