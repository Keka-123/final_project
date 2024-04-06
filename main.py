#Импорт
from flask import Flask, render_template,request, redirect, send_from_directory



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', 
                           button_python=button_python,
                            button_discord=button_discord)

@app.route('/form', methods=['POST'])
def form_render():
    name = request.form['name']
    text = request.form['text']
    return render_template('form.html',
                            name=name,
                            text=text)

@app.route('/meme', methods=['GET','POST'])
def meme():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")
        # Задание №3. Получаем расположение текста
        text_top_y = request.form["textTop_y"]
        text_bottom_y = request.form["textBottom_y"]
        # Задание №3. Получаем цвет текста
        selected_color = request.form["color-selector"]

        return render_template('index_2.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image, 
                               
         
                               # Задание №2. Отображаем текст
                               text_top = text_top,
                               text_bottom = text_bottom,
         

                               # Задание №3. Отображаем цвет 
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y,
                               selected_color = selected_color
                               
                               #Задание №3. Отоброжаем расположение текста

                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index_2.html', selected_image='logo.svg')

@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

if __name__ == "__main__":
    app.run(debug=True)
