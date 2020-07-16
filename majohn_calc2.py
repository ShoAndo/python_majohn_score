from flask import Flask, render_template, request
app = Flask(__name__)

def calc_point(point, rank):
    result = 0
    if rank == 1:
        result = int(point / 1000) - 35 + 20 + 15
    elif rank == 2:
        result = int(point / 1000) - 35 + 10
    else:
        result = int(point / 1000) - 35 - 30
    return result

def validation(name,val):
    err_msg = ''
    if not val:
        err_msg = f'{name}を入力してください'
    return err_msg
    

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        res = {}
        res['point'] = int(request.form.get('point', ''))
        res['rank'] = int(request.form.get('rank', ''))
        res['err_point'] = validation('得点', res['point'])
        res['err_rank'] = validation('順位', res['rank'])

        if not res['err_point'] and not res['err_rank']:
            res['result'] = calc_point(res['point'], res['rank'])

        return render_template('index14.html', res=res)
    else:
        return render_template('index14.html')



if __name__ == '__main__':
    app.run()