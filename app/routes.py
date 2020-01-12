from flask import render_template, url_for, redirect, Markup
from app import app
from app.forms import SubmitTextForm
import app.storage as st
import os


def render_list():
    li = st.list_texts()
    renders = []
    for file in li:
        text, name = st.read(file)
        if len(text) > 181:
            text = text[:180] + '…'
        if text.count('\n') > 1:
            i = text.index('\n', text.index('\n') + 1)
            text = text[:i] + ' …'
        renders.append(render_template('article.html', name=name, summary=text))
    if not renders:
        return '<p class="lead">No Text files.</p>'
    return ''.join(renders)


@app.route('/', methods=["GET", "POST"])
def root(error=''):
    form = SubmitTextForm()

    if form.validate_on_submit():
        text = form.file.data.stream.read()
        if form.name.data:
            name = form.name.data
        else:
            name = os.path.splitext(form.file.data.filename)[0]
        if not st.available(name):
            return root(render_template('nametaken.html'))
        st.save(name, text.decode())
        return redirect(url_for('root'))

    return render_template('main.html', form=form, texts=Markup(render_list()), errors=Markup(error))


@app.route('/<text>')
def show_text(text):
    if ' ' in text:
        return redirect(st.url_name(text))
    if not st.available(text):
        text, name = st.read(text)
        return render_template('text.html', name=name, text=text)
    return 'Not Found.'


@app.route('/delete/<text>')
def delete_text(text):
    if ' ' in text:
        return redirect('/delete/' + st.url_name(text))
    if not st.available(text):
        st.delete(text)
        return 'Deleted.'
    return 'Not Found.'
