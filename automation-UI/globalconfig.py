"""
@package global

Global config file
"""

mongoDB_conn_URI = "mongodb://localhost:31001/"
mongoDB = 'service-fdms'
browser = "chrome"
# list of arguments to provide to the driver. Default is empty list with no arguments
browser_arguments = ["--headless"]
base_url = 'http://localhost:9000/'
browser_implicit_wait_in_secs = 2
