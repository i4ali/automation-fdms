"""
@package global

Global config file
"""

# Use the below conn_URI for testing locally
# postgres_conn_URI = "postgres://stack-user:stack-password@127.0.0.1:43000/toolkit-docker"

# Use the below conn_URI for testing in AWS
postgres_conn_URI = "postgres://service_toolkit_user:zMw1$ak85N^Zqa@toolkit-qa.cqztu6sln31x.us-east-1.rds.amazonaws.com:5432/service_toolkit_qa"

browser = "firefox"

# List of arguments to provide to the driver. Default is empty list with no arguments.
# It is best to use 'start-maximized' option for the browser window all the time to avoid issues with finding elements
# For testing in AWS, use the --headless option
browser_arguments = ["start-maximized", "--headless"]

# Use the below conn_URI for testing in AWS
base_url = 'http://toolk-publi-1kaic7bnh5sva-448940884.us-east-1.elb.amazonaws.com'

# Use the below conn_URI for testing locally
# base_url = 'http://127.0.0.1:30000'

browser_implicit_wait_in_secs = 2
pagination_limit = 10
