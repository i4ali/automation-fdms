"""
@package global

Global config file
"""
import logging

# Use the below conn_URI for testing locally
# postgres_conn_URI = "postgres://stack-user:stack-password@127.0.0.1:43000/toolkit-docker"

# Use the below conn_URI for testing in AWS
postgres_conn_URI = ""

browser = "firefox"

# List of arguments to provide to the driver. Default is empty list with no arguments.
# Browser arguments supported: 1) start-maximized 2) headless
# It is best to use 'start-maximized' option for the browser window all the time to avoid issues with finding elements
# For testing in AWS, use the headless option
browser_arguments = ["start-maximized", "headless"]

# Use the below conn_URI for testing in AWS
base_url = ""

# Use the below conn_URI for testing locally
# base_url = 'http://127.0.0.1:30000'

browser_implicit_wait_in_secs = 4
pagination_limit = 10

logging_level = logging.DEBUG