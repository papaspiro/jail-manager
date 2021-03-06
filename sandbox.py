#ra = ResidentialAddress(county="rr",address_area='Tema',address_locality='comm3',address_street="lovehill",address_housenumber ="1234")
#pa = PostalAddress(country="ghana",city="accra",zipcode="0000",box_number="563")


''' @app.route('/upload', methods=['GET', 'POST'])
 def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return json.dumps({'filename':f_name})


<!DOCTYPE html>
<html lang="en">
  <head>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"
          rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h3 class="text-muted">How To Upload a File</h3>
      </div>
      <hr/>
      <div>
      
      <form action="upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file"><br /><br />
        <input type="submit" value="Upload">
      </form>
      </div>
    </div>
  </body>
</html>
  	

 import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    ) 	

'''

 #api.add_resource(UploadImage, '/api/uploadimage/<string:fname>')
 #   <input type="file" name="file">



from flask import Flask
from flask import render_template,session ,send_from_directory
from werkzeug import secure_filename
from flask import request
import os
from flask import jsonify
from config import UPLOAD_FOLDER

application = Flask(__name__)


@application.route('/')
def hello():
  return "<h1 style='color:blue'> hello world </h1>"


if __name__ == "__main__":
  application.run(host="0.0.0.0")



'''

@app.route('/upload',methods=['POST','PUT'])
def upload():
  file = request.files['picture']
  #if request.method == 'GET':
  filename = secure_filename(file.filename)
  file.save(os.path.join(UPLOAD_FOLDER, filename))
  return jsonify({"success":True})



@app.route("/uploadform")
def uploadform():
  return render_template('sandbox.html')

if __name__ == '__main__':
  app.run(debug=True)

  '''