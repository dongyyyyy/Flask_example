import numpy as np
import requests
import json
import cv2
import base64

res = requests.get('http://210.115.230.164:80/csv_file_download_with_file')
res = res.content.decode('utf-8')
res = eval(res)
img = res['img']
img = base64.b64decode(img)
jpg_arr = np.frombuffer(img,dtype=np.uint8)
img = cv2.imdecode(jpg_arr,cv2.IMREAD_COLOR)
cv2.imshow('img',img)
cv2.waitKey(0)
