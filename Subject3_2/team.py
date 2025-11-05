# team.py

from flask import Flask, render_template, request

# Flask 앱 생성합니다.
app = Flask(__name__)

# 팀원 데이터
team_members = [
    {'name': '팀원1', 'role': 'AI 엔지니어', 'motto': '세상을 바꾸는 코드'},
    {'name': '팀원2', 'role': '프로젝트 매니저', 'motto': '일정은 생명이다'},
    {'name': '팀원3', 'role': '백엔드 개발자', 'motto': '버그 없는 세상'}
]

# --- 라우트(Route) 정의 ---
# 라우트: 특정 URL로 접속했을 때 실행될 함수를 연결해줍니다.

@app.route('/')
def home():
    """
    메인 페이지 (http://.../)
    - index.html을 렌더링(표시)합니다.
    - 팀원 목록 데이터를 HTML로 전달합니다.
    """
    return render_template('index.html', members=team_members)

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    """
    팀원 추가 페이지 (http://.../input)
    - GET 방식: input.html 폼을 보여줍니다.
    - POST 방식: 폼에서 전송된 데이터를 처리합니다.
    """
    if request.method == 'POST':
        # 1. 폼에서 전송된 데이터를 받습니다.
        new_name = request.form['name']
        new_role = request.form['role']
        new_motto = request.form['motto']
        
        # 2. (임시) 받은 데이터로 새 팀원 딕셔너리를 만듭니다.
        new_member = {'name': new_name, 'role': new_role, 'motto': new_motto}
        team_members.append(new_member) # 실제로는 DB에 저장해야 합니다.
        
        # 3. result.html 페이지로 결과를 보여줍니다.
        return render_template('result.html', 
                               title="팀원 추가 완료", 
                               message=f"{new_name}({new_role}) 님이 팀에 합류했습니다!")
    
    # GET 요청일 경우 (그냥 페이지에 접속했을 때)
    return render_template('input.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    """
    연락처 페이지 (http://.../contact)
    - GET 방식: contact.html 폼을 보여줍니다.
    - POST 방식: 폼 데이터를 처리합니다.
    """
    if request.method == 'POST':
        # 1. 폼 데이터(문의 내용)를 받습니다.
        email = request.form['email']
        message = request.form['message']
        
        # 2. (임시) 받은 데이터를 서버 콘솔에 출력합니다.
        # (실제로는 이메일을 보내거나 DB에 저장합니다)
        print(f"--- 새 문의 접수 ---")
        print(f"보낸 사람: {email}")
        print(f"내용: {message}")
        print(f"-------------------")
        
        # 3. result.html 페이지로 처리 완료를 알립니다.
        return render_template('result.html',
                               title="문의 접수 완료",
                               message="소중한 의견 감사합니다. 곧 회신 드리겠습니다.")
    
    # GET 요청일 경우
    return render_template('contact.html')

# 이 스크립트가 메인으로 실행될 때만 웹 서버를 가동합니다.
if __name__ == '__main__':
    app.run(debug=True) # debug=True는 개발 중 오류를 쉽게 볼 수 있게 해줍니다.
