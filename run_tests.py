import os
import subprocess
from datetime import datetime

def run_automation():
    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"reports/HCM_Execution_Report_{timestamp}.html"

    print(f"\n🚀 Running Playwright BDD Automation Tests...")
    print(f"📊 Generating HTML Report: {report_name}\n")

    command = f"behave -f html -o {report_name}"
    subprocess.run(command, shell=True)

    print(f"\n✅ Execution Finished! Report saved at: {report_name}")

if __name__ == "__main__":
    run_automation()