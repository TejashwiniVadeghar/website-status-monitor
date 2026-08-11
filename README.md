# 🌐 website-status-monitor
An automated Python tool that checks website status daily that is checks if websites are online every day and updates a status report using GitHub Actions;
logs historical performance metrics to a CSV file, and generates a live uptime analytics dashboard using GitHub Actions.


An automated, serverless uptime monitoring tool that checks the status of target websites daily and generates a live markdown status report. 

Powered by Python and GitHub Actions.

## 🚀 How It Works
* **Automation:** A GitHub Actions workflow triggers every day automatically using a midnight UTC cron schedule.
* **Health Check:** The Python script makes network requests to test server responsiveness and handles potential connection timeouts cleanly.
* **Data Persistence:** Appends every health check to a flat-file database (`uptime_history.csv`) to store historical tracking data over time.
* **Analytics Engine:** Automatically reads your history logs on every run to compute a lifetime uptime reliability percentage for each website.
* **Artifact Generation:** Updates a dynamic markdown dashboard (`status_report.md`) directly inside the repository without external hosting costs.

## ⚙️ Tech Stack & Concepts Demonstrated
* **Language:** Python 3.10
* **Data Layer:** Flat-file database storage (`csv`) and stream log parsing (`DictReader`)
* **Libraries:** `requests` (API communication), `datetime` (timestamp tracking)
* **DevOps & CI/CD:** GitHub Actions (cron job scheduling, workflow environment permissions, automated repository commits)
* **Code Quality:** Automated style checking logs via integrated lint steps

## 📁 Repository Structure
```text
├── .github/workflows/
│   └── run_monitor.yml   # CI/CD automation workflow
├── monitor.py            # Main application & analytics logic
├── uptime_history.csv    # Persistent tracking log database
└── status_report.md      # Auto-generated markdown dashboard
```
