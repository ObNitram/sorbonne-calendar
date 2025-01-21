from requests.auth import HTTPBasicAuth

username = 'student.master'
password = 'guest'
auth = HTTPBasicAuth(username, password)

host = 'https://obnitram.github.io/sorbonne-calendar/'
publish_dir = 'public'