# website-status-monitor
A simple Python script that automatically checks if websites are online every day and updates a status report using GitHub Actions.

An automated, serverless uptime monitoring tool that checks the status of target websites daily and generates a live markdown status report. 

Powered by Python and GitHub Actions.

## 🚀 How It Works
* **Automation:** A GitHub Actions workflow triggers every day at midnight UTC.
* **Health Check:** The Python script makes asynchronous HTTP requests to test server responsiveness and handle potential connection timeouts.
* **Code Quality:** Integrated code formatting validation via `black` ensures strict adherence to clean-code standards before execution.
* **Artifact Generation:** Updates a dynamic markdown status dashboard (`status_report.md`) directly inside the repository without external hosting costs.

## ⚙️ Tech Stack & Concepts Demonstrated
* **Language:** Python 3.10
* **Libraries:** `requests` (API communication), `datetime` (log parsing)
* **DevOps & CI/CD:** GitHub Actions (cron job scheduling, workflow environments, automated commits)
* **Code Quality:** Black Formatter (Linter automation)
