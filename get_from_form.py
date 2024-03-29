from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from flask import request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'c:/Users/Admin/Desktop/PythonPDFRW/Write_File'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])
app.config['SECRET_KEY'] = 'catchmeifyoucan'


class ChangeForm(FlaskForm):
    bizAuth = FileField('Additional Sign-off:')
    newDoc = FileField('Training/Documentation')
    submit = SubmitField('Save')


@app.route('/change', methods=['GET','POST'])
def form():
    fUp = FileUpload()  # File Upload class - detailed below.
    chgForm = ChangeForm()
    chgDetail = dict()

    # Change 1
    if request.method == "POST" and chgForm.validate_on_submit():
        bizAuth = chgForm.bizAuth.data
        chgDetail['bizAuth'] = fUp.upload(bizAuth)

        newDoc = chgForm.newDoc.data
        chgDetail['newDoc'] = fUp.upload(newDoc)

    return render_template('index.html', form=chgForm)


class FileUpload():

    def allowed_files(self, file_name):
        allowed_extensions = ['txt', 'pdf']
        return '.' in file_name and file_name.rsplit('.',1)[1].lower() in allowed_extensions

    def upload(self, file):
        file_name = file.filename
        if file_name == '':
            return 'NULL'

        elif file_name and self.allowed_files(file_name):
            secure_file_name = secure_filename(file_name)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],'Normal Changes Docs\\' + secure_file_name))

        return str(os.path.join(app.config['UPLOAD_FOLDER'],'Normal Changes Docs\\' + secure_file_name))


if __name__ == "__main__":
    app.run(debug=True)
