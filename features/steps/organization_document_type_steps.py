from behave import when, then
from pages.organization_document_type_page import OrganizationDocumentTypePage


@when('User opens the Document Type page under Organization Setup')
def doc_open_page(context):
    context.doc_type_page = OrganizationDocumentTypePage(context.page)
    context.doc_type_page.navigate_to_document_type()


@when('User clicks on Create New Document Type button')
def doc_click_create(context):
    context.doc_type_page.click_create_document_type()


@when('User fills the document type form with valid data and clicks Create')
def doc_fill_form(context):
    context.doc_type_page.fill_document_type_form()


@then('The new document type should be created and displayed in the document type list successfully')
def doc_verify_created(context):
    context.doc_type_page.verify_document_type_created()