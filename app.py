from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey_macbook_2024'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        print(f"Новый подписчик: {email}")
        flash('Спасибо! Вы подписались на новости о мире Mac.', 'success')
    else:
        flash('Пожалуйста, введите корректный email.', 'error')
    return redirect(url_for('home', _anchor='subscribe'))

@app.route('/consult', methods=['POST'])
def consult():
    name = request.form.get('name')
    phone = request.form.get('phone')
    if name and phone:
        print(f"ЗАЯВКА: Имя={name}, Тел={phone}")
        flash(f'{name}, ваша заявка принята! Мы перезвоним вам в ближайшее время.', 'success')
    else:
        flash('Заполните обязательные поля (Имя и Телефон).', 'error')
    return redirect(url_for('home', _anchor='consult'))

if __name__ == '__main__':
    app.run(debug=True, port=8801)
