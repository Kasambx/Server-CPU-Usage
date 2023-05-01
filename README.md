Project Name:Website Uptime Monitoring

Project Description
This project's objective is to keep track of a website's uptime and notify the team if it goes down. The project will be written in Python, and it will send HTTP requests to the website using the requests package. The project will also keep an eye on the website's availability and deliver notifications if it goes down using a cloud-based monitoring service like Pingdom or Datadog.

Project Structure
README.md: contains project Description, setup instructions, and any other relevant information.
Requirements.txt: lists Python pacakges to be used in the projects.
monitor.py: python script that sends an alert to the SRE team via email,Slack or any other platform incase the platform goes down. It uses the requests library to make HTTP requests  to the website and a API to check for the websites availability.
tests:scripts to ensure  the monitor.py script works erro free.

Project Setup:
1.Clone the repository:'git clone https://github.com/Kasambx/Website-Uptime-Monitoring
2.Install the required packages: pip install -r requirements.txt
3.Set up a monitoring tool such as Pingdom or Datadog and get an API key or token.
4.Add the API key or token to a configuration file, which will be read by the monitoring script.
5.Run the monitoring script: python monitor.py

Goals:
Monitoring of the website's uptime alerts incase of downtime.
Automated testing the python script
