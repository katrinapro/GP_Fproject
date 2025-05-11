from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fproject.db'
#Создание db
db = SQLAlchemy(app)


class Card(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Заголовок
    title = db.Column(db.String(200), nullable=False)
    #Текст
    text = db.Column(db.Text, nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'


@app.route("/", methods=['GET','POST'])
def first():
        error = ''
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['text']

            post = Card(title=title, text=text)

            try:
                db.session.add(post)
                db.session.commit()
                return redirect("/")
            except:
                return "При добавлении текста произошла ошибка"    
                    
        else:
            return render_template('first.html')

@app.route("/second")
def second():
    return render_template('second.html')

@app.route("/three")
def third():
    return render_template('third.html') 

@app.route("/fourth")
def fourth():
    return render_template('fourth.html')    


if __name__ == "__main__":
    app.run(debug=True) #помогает перезапускать сервер автоматически 
