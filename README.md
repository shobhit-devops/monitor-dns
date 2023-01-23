## DNS TXT Record Monitor

This script monitors DNS TXT records of a specified hostname every n seconds and prints the date and time every time a specified substring is detected in any TXT record.

### Dependency Management

The script requires the following dependencies:

- dnspython

You can install the dependencies by running the command:
```bash
pip install -r requirements.txt
```
### Running the script
The script can be run with the command:

```bash
python monitor_dns_script.py --hostname <hostname> --interval <interval> --substring <substring>
```
Where:

- hostname: The hostname to monitor. (default: futurestay.com)
- interval: The interval in seconds between DNS queries. (default: 5)
- substring: The substring to search for in the TXT records. (default: google-site)

### Handling Variables
The script uses command-line arguments to pass in the values for the hostname, interval, and substring.

However, it may not be suitable for sensitive information such as secret credentials, as the command-line arguments may be visible in the process list. In such cases, it's better to use environment variables or a secure configuration store like AWS Secrets Manager to store and retrieve the credentials.

### Deployment
The script can be run on a local machine or in a containerized environment. To run the script in an EC2 instance, you could use the command:

```bash
python monitor_dns_script.py --hostname <hostname> --interval <interval> --substring <substring>
```

### Testing
This script includes test cases for the script, which check whether the script is running as expected or not.

To run the test cases, you can use the command:

```bash
python -m unittest discover -s test/ -p "*_test.py"
```

This command will run all the test files in the test/ directory that match the pattern "*_test.py".

### Monitoring
To monitor the script, we can use a tool like AWS CloudWatch, which can be used to check the script's logs and set up alerts to notify of any issues.

### Conclusion
This script provides an easy way to monitor DNS TXT records and alert when a specified substring is detected. The script is easy to run, manage dependencies, and test. With the use of command-line arguments, the script can be run dynamically. This script can also be run in an EC2 instance or in a containerized environment.
