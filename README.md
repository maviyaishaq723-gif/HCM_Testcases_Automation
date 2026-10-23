# HCM Testcases Automation

UI test automation for HCM (Amplify) using Python, Behave and Playwright.

## Setup (first time)

```powershell
git clone <repository-url>
cd hcm-testcases-automation
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

In VS Code: Ctrl+Shift+P -> Python: Select Interpreter -> choose the `.venv` one.
Python 3.14 and access to the HCM test server (office network/VPN) are required.

## Run

```powershell
behave                                                       # all tests
behave features/role/role_management.feature                 # one feature
behave features/role/role_management.feature --tags=@TC_11   # one test case
behave --tags=@employee_profile_module                       # one module
```

Report: `reports/latest_execution_report.html`