"""
@package global

Global config file
"""

# mongoDB_conn_URI = "mongodb://localhost:31001/service-fdms"
# postgres_conn_URI = "postgres://stack-user:stack-password@dev.toolkit.wdvglab.com:43000/toolkit-docker"
postgres_conn_URI = "postgres://service_toolkit_user:zMw1$ak85N^Z@toolkit-dev.czh4kwywizqc.us-west-2.rds.amazonaws.com:5432/service_toolkit_dev"
browser = "firefox"
# List of arguments to provide to the driver. Default is empty list with no arguments.
# It is best to use 'start-maximized' option for the browser window all the time to avoid issues with finding elements
browser_arguments = ["--headless"]
base_url = 'http://dev.toolkit.wdvglab.com/wells'
browser_implicit_wait_in_secs = 2
pagination_limit = 10
