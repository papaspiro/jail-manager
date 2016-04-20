from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from sqlalchemy.ext.associationproxy import association_proxy
from flask.ext.sqlalchemy import SQLAlchemy

from wtforms import TextAreaField
from wtforms.widgets import TextArea
import  os.path as op
import os

from flask_admin.contrib.sqla import ModelView
from flask_admin import form
from flask_admin.form import rules
from flask_admin.contrib import sqla

file_path = os.path.join(os.path.dirname(__file__) ,'static')

path = op.join(op.join(op.dirname(__file__)),'static')

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECREET_KEY']='123456'

#app.config['SQLALCHEMY_DATABASE_URI'] = 	'sqlite:///' + os.path.join(os.path.abspath(__file__), 'hello.db')
SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'hello.db')
 #os.path.abspath(os.path.join('sqlite:///','hello.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

#models
class User(db.Model):
	id = db.Column(db.Integer(),nullable=False, primary_key=True)
	first_name = db.Column(db.String(120), nullable=False)
	last_name = db.Column(db.String(120),nullable=False)
	email = db.Column(db.String(120),nullable=False,unique=True)

	def __str__(self):
		return " < User %s  %s>" %(self.first_name,self.last_name)

class Community(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(40),unique=True)

	def __str__(self):
		return "<Community> %s"  %self.name


#association/bridge object
class Membership(db.Model):
	#__tablename__ = 'community_members'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
	community_id = db.Column(db.Integer(),db.ForeignKey('community.id'))
	serial_number = db.Column(db.String(14),unique=True)

	user = db.relationship(User,backref='memberships')
	community = db.relationship(Community,backref='memberships')


Community.members = association_proxy('memberships','user')
User.communities  = association_proxy('memberships','community')


class Place(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='')

class FacilityType(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	#facility_code = db.Column(db.String,unique=True,nullable=False)
	type = db.Column(db.String(120),nullable=False,unique=True)

	def __str__(self):
		return " %s " %self.type

class CorrectionalFacility(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(120),nullable=False)
	facility_type_id = db.Column(db.Integer(),db.ForeignKey('facility_type.id'))
	capacity_female = db.Column(db.Integer(),nullable=False ,default=0.0)
	capacity_male = db.Column(db.Integer(),nullable=False,default=0.0)

	db.relationship(FacilityType,backref='correctional_facility')

	def __str__(self):
		return " %s " %self.name

class ResidentialAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	house_number = db.Column(db.String(120), nullable=False,default="")
	street = db.Column(db.String(120))
	place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))	

	#relationship
	place = db.relationship(Place,backref="residential_addresses")


class PostalAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	box_number = db.Column(db.String(40))
	place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))	
	
	#relationship
	place = db.relationship(Place,backref="postal_addresses")




'''
class PostalAddressPlace(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	postal_addresses_id = db.Column(db.Integer(),db.ForeignKey('postal_address.id'))
	place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))
'''

'''
class ResidentialAddressPlace(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	residential_address_id = db.Column(db.Integer(),db.ForeignKey('residential_address.id'))
	place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))



class CourtType(db.Model):
	pass

class Court(db.Model):
	pass

class Offence(db.Model):
	pass

class Sentence(db.Model):
	pass

'''
class Inmate(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	serial_number = db.Column(db.String(24),unique=True,nullable=False)
	picture = db.Column(db.String(120))
	first_name = db.Column(db.String(120),nullable=False)
	middle_name = db.Column(db.String(12))
	last_name = db.Column(db.String(120),nullable=False)
	distinctive_marks = db.Column(db.String(250))


	date_of_birth = db.Column(db.Date())
	#place_of_birth_id = db.Column(db.Integer(),db.ForeignKey('place.id'))
	languages = db.Column(db.String(120))
	education = db.Column(db.String(120))

	complexion = db.Column(db.String(120),nullable=False)
	nationality = db.Column(db.String(120),nullable=False)
	tribe = db.Column(db.String(120),nullable=False)
	thumbprint = db.Column(db.String(),nullable=False)



	def __str__(self):
		return "inmate  %s %s %s"  %(self.last_name , self.first_name ,self.serial_number) 


class PenalRecord(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	years_of_sentence = db.Column(db.Float(),nullable=False,default=0)
	months_of_sentence = db.Column(db.Float(),nullable=False,default=0)
	days_of_sentence = db.Column(db.Float(),nullable=False,default=0)
	date_of_sentence = db.Column(db.DateTime(),nullable=False)	
	earliest_discharge_date = db.Column(db.DateTime(),nullable=False)
	lattest_discharge_date = db.Column(db.DateTime(),nullable=False)
	remission = db.Column(db.String(120))
	date_of_addmission = db.Column(db.Date(),nullable=False)
	
	#place_of_committal = db.String(db.String(120))
	#how do we represent life sentence a 1000 years ?

	#foreign keys
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	#offence_id = db.Column(db.Integer(),db.ForeignKey('offence.id'))
	offence = db.Column(db.String(500),nullable=False)
	#place_of_conviction1 = db.Column(db.String('120'),nullable=False)
	#court.id = db.Column(db.Integer(),db.ForeignKey('court.id'))
	place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))
	correctional_facility_id = db.Column(db.Integer(),db.ForeignKey('correctional_facility.id'))


	#relationships

	#relations
	inmate = db.relationship(Inmate,backref='penal_records')
	place_of_conviction = db.relationship(Place,backref = "penal_records")
	place_of_committal = db.relationship(CorrectionalFacility,backref = "penal_records")


class NextOfKin(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	first_name = db.Column(db.String(120),nullable=False)
	middle_name = db.Column(db.String(120))
	last_name = db.Column(db.String(120) ,nullable=False)
	relation = db.String(120)
	po_address = db.Column(db.String(250))
	res_address = db.Column(db.String(250))
	email = db.Column(db.String(120),nullable=False)

	#foreign keys
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))

	#relations
	inmate = db.relationship(Inmate,backref='next_of_kin')

	def __str__(self):
		return  " %s of %s" %(unicode(self.relation),unicode(self.inmate.serial_number))

	def get_inmate_by_id(id):
		pass

class PreviousConviction(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	date_of_conviction = db.Column(db.Date())
	place_of_conviction = db.Column(db.String()) #court of conviction
	sentence = db.Column(db.String(100))
	offence = db.Column(db.String(150))

	#foreignkeys
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	#place_id = db.Column(db.Integer(),db.ForeignKey(place.id))
	correctional_facility_id = db.Column(db.Integer(),db.ForeignKey('correctional_facility.id'))

	#relationship
	inmate = db.relationship(Inmate,backref="previous_conviction")
	place_sentence = db.relationship(CorrectionalFacility,backref="previous_convictions")


class Discharge(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_discharge = db.Column(db.Date())
	reason_for_discharge = db.Column(db.String(100))

	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="discharge")


class Property(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	items = db.Column(db.String(500))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="property")


class Transfer(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(300))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="transfers")
	



#bridge tables
class NOKPostalAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	postal_addresses_id = db.Column(db.Integer(),db.ForeignKey('postal_address.id'))
	next_of_kin_id = db.Column(db.Integer(),db.ForeignKey('next_of_kin.id'))

	#relationships
	postal_address = db.relationship(PostalAddress,backref="nok_residential_address")
	next_of_kin = db.relationship(NextOfKin,backref="nok_postal_address")


class NOKResidentialAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	#foreignkeys
	residential_addresses_id = db.Column(db.Integer(),db.ForeignKey('residential_address.id'))
	next_of_kin_id = db.Column(db.Integer(),db.ForeignKey('next_of_kin.id'))

	#relationships
	residential_address = db.relationship(ResidentialAddress,backref="nok_residential_address")
	next_of_kin = db.relationship(NextOfKin,backref="nok_residential_address")



class InmatePostalAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	postal_address_id = db.Column(db.Integer(),db.ForeignKey('postal_address.id'))
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))

	#relationship
	postal_address = db.relationship(PostalAddress,backref='inmate_postal_address')
	inmate = db.relationship(Inmate,backref='inmate_postal_address')

	inline_models = [PostalAddress]


class InmateResidentialAddress(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	residential_address_id = db.Column(db.Integer(),db.ForeignKey('residential_address.id'))
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))

	#relationship
	residential_address = db.relationship(ResidentialAddress,backref="inmate_residential_address")
	inmate = db.relationship(Inmate,backref='inmate_residential_address')









class InmateView(ModelView):
	column_auto_select_related = True
	page_size = 50
	
	can_delete = True
	can_create = True
	can_edit = True
	can_view_details = True

	#fast insitu edit
	#column_editing_list = []
	inline_models = [PostalAddress]
	column_auto_selected_related=True
	

	'''column_exclude_list = ['date_created','language','education','date_of_sentence','place_of_conviction',
	'place_of_birth_country','place_of_birth_region','place_of_birth_locality','place_of_offence_country',
	'place_of_offence_region','place_of_offence_locality','distinctive_marks']
	'''


	form_excluded_columns = ['previous_convictions','inmate_postal_address','inmate_residential_address','property',
	'penal_records','discharge','transfers','previous_conviction','next_of_kin_id']


	column_searchable_list = ['serial_number','last_name','first_name']
	#column_editable_list = ['serial_number','last_name','first_name','offence']
	

	'''create_modal = True
	edit_modal = True''
	'''
	

	

	def _list_thumbnail(view,context,model , name):
		if not model.picture:
			return ''
		return Markup('<img src="%s">' % url_for('static',
			filename=form.thumbgen_filename(model.picture)))


	column_formatters = {
			'picture' : _list_thumbnail
	} 

	form_extra_fields = {
			'picture' : form.ImageUploadField('Picture',
				base_path=file_path,
				thumbnail_size = (100,100,True))

	}

class ResidentialAddressView(ModelView):
	page_size = 50
	can_delete = True
	can_create = True
	can_edit = True
	can_view_details = True
	#fast insitu edit
	#column_editing_list = []
	inline_models = (Place)


class InmateResidentialAddressView(ModelView):
	page_size = 50
	
	can_delete = True
	can_create = True
	can_edit = True
	can_view_details = True
	#fast insitu edit
	#column_editing_list = []
	inline_models = (ResidentialAddress)





#views
admin = Admin(app,name='what the what', template_mode="bootstrap3")
admin.add_view(FileAdmin(path,'/static/',name='Static Files'))


admin.add_view(InmateView(Inmate,db.session))
admin.add_view(ModelView(PenalRecord,db.session))
admin.add_view(ModelView(NextOfKin,db.session))
admin.add_view(ModelView(PreviousConviction,db.session))
admin.add_view(ModelView(Discharge,db.session))
admin.add_view(ModelView(Property,db.session))
admin.add_view(ModelView(Transfer,db.session))





if __name__ == '__main__':
	app.run(debug=True)