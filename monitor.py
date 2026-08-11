import os
import requests
from datetime import datetime

WEBSITES = [
    "https://github.com",
    "https://google.com"
]

def check_websites():
    print(f"Starting check at {datetime.now()}")
    report = f"## Website Status Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n\n"
    report += "| Website | Status | Response Time (s) |\n| :--- | :--- | :--- |\n"
    
    for url in WEBSITES:
        try:
            start_time = datetime.now()
            response = requests.get(url, timeout=10)
            duration = (datetime.now() - start_time).total_seconds()
            
            status = "✅ Up" if response.status_code == 200 else f"⚠️ Down ({response.status_code})"
            report += f"| {url} | {status} | {duration:.2f}s |\n"
        except requests.exceptions.RequestException as e:
            report += f"| {url} | ❌ Error ({type(e).__name__}) | N/A |\n"

    with open("status_report.md", "w") as f:
        f.write(report)
    print("Report generated successfully.")

if __name__ == "__main__":
    check_websites()
