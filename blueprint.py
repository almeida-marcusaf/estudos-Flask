from werkzeug import secure_filename
from flask import Blueprint, render_template, request, abort
from jinja2 import TemplateNotFound
import os

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
