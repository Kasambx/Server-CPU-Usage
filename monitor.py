import requests
import json

# Configuration variables
WEBSITE_URL = "https://example.com"  # The website URL to monitor
MONITORING_TOOL_API_KEY = "YOUR_API_KEY"  # The API key/token for the monitoring tool
ALERT_CONTACT_EMAIL = "sre-team@example.com"  # The email address to send alerts to
ALERT_CONTACT_SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL"  # The Slack webhook URL to send alerts to

# Function to send an alert via email
def send_email_alert():
    # Implement code to send email alert using your preferred email API or service
    print("Website is down! Sent an alert via email.")

# Function to send an alert via Slack
def send_slack_alert():
    # Implement code to send Slack alert using the webhook URL and the requests library
    payload = {"text": "Website is down!"}
    response = requests.post(ALERT_CONTACT_SLACK_WEBHOOK_URL, data=json.dumps(payload))
    if response.status_code != 200:
        print("Error sending Slack alert:", response.text)
    else:
        print("Website is down! Sent an alert via Slack.")

# Main function to monitor website uptime and send alerts if site is down
def main():
    # Make a GET request to the website URL and check the response status code
    response = requests.get(WEBSITE_URL)
    if response.status_code != 200:
        # Send an alert via email and/or Slack if the site is down
        send_email_alert()
        send_slack_alert()

if __name__ == "__main__":
    main()
