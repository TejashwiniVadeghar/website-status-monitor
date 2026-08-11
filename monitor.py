import os
import csv
from datetime import datetime
import requests

WEBSITES = ["https://github.com", "https://google.com"]
HISTORY_FILE = "uptime_history.csv"
REPORT_FILE = "status_report.md"


def log_to_csv(timestamp, url, status, duration):
    """Appends the raw ping result into a historical CSV file."""
    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            # Create headers if the file is brand new
            writer.writerow(["Timestamp", "URL", "Status", "ResponseTime"])
        writer.writerow([timestamp, url, status, f"{duration:.2f}"])


def calculate_metrics():
    """Reads the CSV file to calculate the historical uptime percentage for each site."""
    stats = {}
    if not os.path.isfile(HISTORY_FILE):
        return stats

    with open(HISTORY_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row["URL"]
            status = row["Status"]

            if url not in stats:
                stats[url] = {"total": 0, "up": 0}

            stats[url]["total"] += 1
            if status == "✅ Up":
                stats[url]["up"] += 1

    # Calculate percentages
    for url in stats:
        uptime_pct = (stats[url]["up"] / stats[url]["total"]) * 100
        stats[url]["percentage"] = f"{uptime_pct:.2f}%"
        stats[url]["total_checks"] = stats[url]["total"]

    return stats


def check_websites():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Starting check at {timestamp}")

    current_results = []

    # 1. Perform health checks and log them to history
    for url in WEBSITES:
        try:
            start_time = datetime.now()
            response = requests.get(url, timeout=10)
            duration = (datetime.now() - start_time).total_seconds()

            status = (
                "✅ Up"
                if response.status_code == 200
                else f"⚠️ Down ({response.status_code})"
            )
        except requests.exceptions.RequestException as e:
            status = f"❌ Error ({type(e).__name__})"
            duration = 0.0

        log_to_csv(timestamp, url, status, duration)
        current_results.append(
            {"url": url, "status": status, "duration": f"{duration:.2f}s"}
        )

    # 2. Calculate lifetime performance metrics from history
    historical_stats = calculate_metrics()

    # 3. Generate the Markdown Dashboard report
    report = f"## 📈 Website Performance Dashboard\n"
    report += f"*Last updated: {timestamp}*\n\n"

    report += "### ⏱️ Latest Status\n"
    report += (
        "| Website | Current Status | Response Time |\n| :--- | :--- | :--- |\n"
    )
    for res in current_results:
        report += f"| {res['url']} | {res['status']} | {res['duration']} |\n"

    report += "\n### 📊 Historical Reliability Metrics\n"
    report += "| Website | Lifetime Uptime | Total Checks Logged |\n| :--- | :--- | :--- |\n"
    for url, data in historical_stats.items():
        report += (
            f"| {url} | **{data['percentage']}** | {data['total_checks']} |\n"
        )

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print("Dashboard and historical records updated successfully.")


if __name__ == "__main__":
    check_websites()
