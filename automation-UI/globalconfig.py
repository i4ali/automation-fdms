"""
@package global

Global config file
"""

# mongoDB_conn_URI = "mongodb://localhost:31001/service-fdms"
postgres_conn_URI = "postgres://fdms-user:fdms-test@127.0.0.1:31002/fdms"
browser = "chrome"
# list of arguments to provide to the driver. Default is empty list with no arguments
browser_arguments = []
base_url = 'http://localhost:9000/'
browser_implicit_wait_in_secs = 2
pagination_limit = 10
