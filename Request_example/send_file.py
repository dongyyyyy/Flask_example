import requests

files = open('C:/Users/ehddm/Desktop/A.jpg', 'rb')
upload = {'file': files}
ress = requests.post('http://210.115.230.164:80/file_upload',files=upload)