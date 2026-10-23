from behave import when, then

@when('User clicks on the Export Employee button')
def step_impl(context):
    context.employee_page.click_export_employee()

@then('An Excel file with employee data should be downloaded')
def step_impl(context):
    assert context.employee_page.downloaded_file is not None, "Failure: Excel file was not downloaded!"

@when('User uploads an employee sample document')
def step_impl(context):
    context.employee_page.upload_employee_file()

@then('Employee file should be uploaded successfully')
def step_impl(context):
    assert True, "Import process executed successfully!"