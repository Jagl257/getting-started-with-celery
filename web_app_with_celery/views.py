from flask import redirect, flash, render_template, request, url_for

from web_app_with_celery import app
from web_app_with_celery.services import (
    generate_file,
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', num=10)

    num = int(request.form.get('num'))
    if request.form.get('submit') == "Generate":
        generate_file(num)
    else:
        generate_file.delay(num)
        
    return redirect(url_for('index'))
