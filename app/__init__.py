from flask import Flask
from config import Config
import os
from flask_uploads import UploadSet, configure_uploads, patch_request_class

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOADED_PLAINTEXT_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text')

plaintext = UploadSet('plaintext')
configure_uploads(app, plaintext)
patch_request_class(app)

from app import routes
