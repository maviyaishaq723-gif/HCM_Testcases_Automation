from behave import when
from pages.employee_export_import_page import EmployeeExportImportPage

@when('User navigates to the Employee module')
def step_impl(context):
    context.employee_page = EmployeeExportImportPage(context.page)
    context.employee_page.navigate_to_employee()
    assert context.employee_page.verify_manage_employee_page(), "Failure: Manage Employee page did not open!"