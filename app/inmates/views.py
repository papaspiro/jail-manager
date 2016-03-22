from app import app
from flask import render_template ,flash ,redirect,request,g,session,url_for,Blueprint

from app.inmates.forms import *
from app.inmates.models import Inmate
from datetime import datetime
from werkzeug import secure_filename

inmate_blueprint = Blueprint('inmates',__name__,url_prefix='/inmates')

from app import db
import os
import uuid
from flask import jsonify
from config import UPLOAD_FOLDER



from flask.ext.superadmin import BaseView, expose

from app import admin

#list of inmates with a query form
#paginates through the lastest ten inmates added as default
#and lattest ten inmates that matches a particular criteria
#result features 
#inmate url: link to image via serial number
#inmate  last name, middle + other names , picture,link to next of kin, link to penal records,link to tranfers 

def allowed_file(filename):
	return  '.' in filename and  filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

@inmate_blueprint.route('/upload',methods=['POST'])
def upload():
	file = request.files('file')
	if file and allowed_file(file.filename):
		#make filename save 
		filename = secure_filename(file.filename)
		#ove file from temporal to upload folder
		file.save(os.path.join(UPLOAD_FOLDER,filename))

		return jsonify({"success":"yes"})


@inmate_blueprint.route('/uploads/<filename>')
def uploads(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@inmate_blueprint.route('/',methods=['GET','POST'])
def inmate_list():
	return 	render_template('/inmates/search.html')


#add an imate
@inmate_blueprint.route('/add',methods=['GET','POST'])
def add_inmate():
	form = InmateForm()
	if form.validate_on_submit():
		
		#to do set a default avartar 
		#fname = ''
		#try :
		file = request.files['picture']

		if file:    # and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			extension = os.path.splitext(file.filename)[1]

			f_name = str(uuid.uuid4()) + extension

			#todo find means to verify if upload was a success
			file.save(os.path.join(UPLOAD_FOLDER,f_name))


		inmate = Inmate(
		serial_number = form.serial_number.data,
		first_name = form.first_name.data ,
		last_name = form.last_name.data,
		middle_name = form.middle_name.data,
		alias = form.alias.data,
		date_of_birth = form.date_of_birth.data,
		gender = form.gender.data,
		distinctive_marks = form.distinctive_marks.data ,
		picture = f_name ,#form.picture.data,
		place_of_birth_country = form.place_of_birth_country.data,
		place_of_birth_region = form.place_of_birth_region.data,
		place_of_birth_locality = form.place_of_birth_locality.data,

	 	language = form.language.data,
		education = form.education.data,

		place_of_offence_country = form.place_of_offence_country.data,
		place_of_offence_region = form.place_of_offence_region.data,
		place_of_offence_locality = form.place_of_offence_locality.data,

		place_of_conviction = form.place_of_conviction.data,
		date_of_sentence = form.date_of_sentence.data,
		date_of_admission = form.date_of_admission.data, #datetime.strptime(form.date_of_admission.data,'%Y-%m-%d'),

		sentence_years = form.sentence_years.data,
		sentence_months = form.sentence_months.data,
		sentence_days = form.sentence_days.data,

		block_cell = form.block_cell.data )

		db.session.add(inmate)
		db.session.commit()

		flash(" inmate successfully added ")
		#postal_address
		#residential_address
		#address on release
		#mext of kin
		
		#return render_template('/inmates/search.html',fname=first_name)
		return redirect(url_for('add_inmate'))
	return render_template("/inmates/new.html",form=form)



#a particular inmate
@inmate_blueprint.route('/inmates/<inmate_id>',methods=['GET','Post'])
def inmate(inmate_id):
	return render_template('/inmates/inmate.html')


#edit particular inmate
@inmate_blueprint.route('/inmate/edit',methods=['POST','GET'])
def new_inmate(inmate_id):
	return render_template('/inmates/update.html')



@inmate_blueprint.route('/nextofkin',methods=['GET','POST'])
def add_next_of_kin():
	form = NextOfKinForm()
	if request.method == "POST":
		if form.validate_on_submit():
			return redirect(url_for(add_next_of_kin,form=form))
	return render_template('/inmates/nextofkin.html',form=form)





@inmate_blueprint.route('/penalrecords',methods=['GET','POST'])
def penal_record():
	form = PenalRecordForm()
	if request.method == "POST":
		if form.validate_on_submit():
			return redirect(url_for(penal_record,form=form))
	return render_template('/inmates/penalrecords.html',form=form)



@inmate_blueprint.route('/transfers',methods=['GET','POST'])
def transfer():
	form = TransferForm()
	if request.method == "POST":
		if form.validate_on_submit():
			return redirect(url_for(transfer,form=form))
	return render_template('/inmates/transfers.html',form=form)






@inmate_blueprint.route('/discharge',methods=['GET','POST'])
def discharge():
	form = DischargeForm()
	if request.method == "POST":
		if form.validate_on_submit():
			return redirect(url_for(discharge,form=form))
	return render_template('/inmates/discharge.html',form=form)




from .models import *

admin.register(Inmate,session=db.session)
admin.register(NextOfKin,session=db.session)
admin.register(PostalAddress,session=db.session)
admin.register(ResidentialAddress,session=db.session)
admin.register(PenalRecord,session=db.session)
admin.register(PreviousConviction	,session=db.session)
admin.register(Discharge,session=db.session)
admin.register(Property,session=db.session)
admin.register(Transfer	,session=db.session)


