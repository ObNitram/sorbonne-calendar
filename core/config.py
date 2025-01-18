import configparser
from requests.auth import HTTPBasicAuth

config = configparser.ConfigParser()
config.read('config.ini')

username = config['credentials']['username']
password = config['credentials']['password']
auth = HTTPBasicAuth(username, password)

host = config['paths']['host']
publish_dir = config['paths']['publish_dir']