from flask import Flask, render_template, request

# Flask 앱 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')



@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        result_data = request.form.to_dict()
        lang_list = request.form.getlist('languages')
        lang_str = ", ".join(lang_list)
        result_data['languages'] = lang_str
        return render_template('result.html', result=result_data)

if __name__ == '__main__':
    app.run(debug=True)