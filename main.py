from flask import Flask,request,send_file  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import pymysql # MySQL 연동
#import sys
import json
import os
import base64

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

conn = pymysql.connect(host='localhost',port=3306,user='root',password='a88110474',db='face_recognition',charset='utf8')
curs = conn.cursor()

@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {"hello": "world!"}

@app.route('/select_checks', methods=['POST'])
def select_checks():
    # params = json.loads(request.get_data(), encoding='utf-8')
    params = json.loads(request.get_data(),encoding='utf-8')
    print(params)
    name = params['name']
    query = params['select']
    # query = request.form.get('select')
    # name = request.form.get('name')
    print(f'name = {name} // query = {query}')
    curs.execute(query)
    # 데이타 Fetch
    rows = curs.fetchall()
    is_check = False
    # 아랫 부분 restful로 수정
    for row in rows:
        current_time = datetime.today().strftime('%Y-%m-%d')
        check_time = row[0].strftime('%Y-%m-%d')
        # print(f'current_time = {current_time} // check_time = {check_time}')
        if current_time == check_time:
            is_check = True
    if is_check:
        return_str = '이미 출석한 사람'
    else:
        sql = f"insert into checks(name) values(%s)"
        curs.execute(sql, (f'{name}'))
        conn.commit()
        return_str = '출근'
    return return_str

@app.route('/new_picture', methods=['POST'])
def new_picture():
    # params = json.loads(request.get_data(), encoding='utf-8')
    params = json.loads(request.get_data(),encoding='utf-8')
    name = params['name']
    query = params['select']

    curs.execute(query)
    # 데이타 Fetch
    rows = curs.fetchall()
    print(rows)
    str = '%d'%(len(rows))
    # print(len(rows))
    return str

@app.route('/file_upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        path = os.path.join('D:/', fname)
        f.save(path)
        return 'File upload complete (%s)' % path

@app.route('/csv_file_download_with_file')
def csv_file_download_with_file():
    file_name = f"D:/encoding_csv.csv"
    # json.dumps({'token': token}), 200
    return send_file(file_name,
                     mimetype='text/csv',
                     download_name='downloaded_file_name.csv',# 다운받아지는 파일 이름.
                     as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)