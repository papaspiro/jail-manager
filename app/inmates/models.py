from app import db
#from passlib.apps import custom_app_context as pwd_context
#from itsdangerous import (TimedJSONWebSignatureSerializer
#  as Serializer, BadSignature, SignatureExpired)
#	from flask import current_app
# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
   # date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    #updated_on = db.Column(db.DateTime,  default=db.func.now(), onupdate=db.func.now())

class Role(Base):
        id = db.Column(db.Integer,primary_key=True)
        rolename = db.Column(db.String(64))
        users = db.relationship('User',backref="role")


class User(Base):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64) ,index=True)
        password_hash = db.Column(db.String(128))
        role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


        def hash_password(self,password):
                self.password_hash = pwd_context.encrypt(password)

        def verify_password(self,password):
                return pwd_context.verify(password, self.password_hash)


        def generate_auth_token(self,expiration=600):
                s = Serializer(current_app.config['SECRET_KEY'],expires=expiration)
                #s = Serializer(current_app.config['SECRET_KEY'],expires=expiration)

                return s.dumps({'id',self.id})

class Inmate(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	serial_number = db.Column(db.String(100))
	first_name = db.Column(db.String(100))
	middle_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	alias = db.Column(db.String(60))
	date_of_birth= db.Column(db.Date())
	gender = db.Column(db.String(6))


	distinctive_marks = db.Column(db.String(250))
	picture = db.Column(db.String(150))

	place_of_birth_country = db.Column(db.String(100))
	place_of_birth_region = db.Column(db.String(100))
	place_of_birth_locality = db.Column(db.String(100))
	language = db.Column(db.String(100))
	education = db.Column(db.String(100))

	place_of_offence_country = db.Column(db.String(100))
	place_of_offence_region = db.Column(db.String(100))
	place_of_offence_locality = db.Column(db.String(100))
 

	#administrative data
	date_of_admission = db.Column(db.Date())
	place_of_conviction = db.Column(db.String())
	offence = db.Column(db.String(100))
	date_of_sentence = db.Column(db.Date())
	sentence_years = db.Column(db.Integer())
	sentence_months = db.Column(db.Integer())
	sentence_days = db.Column(db.Integer()) 
	block_cell = db.Column(db.String())

	#foreignkeys
	residential_address_id = db.Column(db.Integer,db.ForeignKey('residential_address.id'))
	#release_address_id = db.Column(db.Integer,db.ForeignKey('residential_address.id'))
	postal_address_id = db.Column(db.Integer,db.ForeignKey('postal_address.id'))



	#relationships
	next_of_kin = db.relationship('NextOfKin',backref="inmate_related_to")
	penal_records = db.relationship('PenalRecords',backref='inmate',lazy='dynamic')
	discharge = db.relationship('Discharge',backref="inmate",lazy='dynamic')

	residential_address = db.relationship('ResidentialAddress',backref='inmate_residence')
	address_on_release = db.relationship("ResidentialAddress",backref='inmate_release_residence')
	postal_address = db.relationship('PostalAddress',backref='inmate_pobox')
	
	def	__repr__(self):
		return "Inmate : %s %s %s" %(self.serial_number,self.first_name,self.last_name)


#the next of kin
class NextOfKin(Base):
	id = db.Column(db.Integer,primary_key=True )
	first_name = db.Column(db.String(100))
	middle_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	postal_address_id = db.Column(db.Integer,db.ForeignKey('postal_address.id'))

	#foreignkey
	inmate_id = db.Column(db.ForeignKey('inmate.id',))
	
	#relationship
	postal_address = db.relationship('PostalAddress',backref="inmate_next_of_kin")


class PenalRecords(Base):
	id = db.Column(db.Integer,primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey("inmate.id"))
	date_of_conviction = db.Column(db.Date())
	place_of_conviction = db.Column(db.String(100))
	remission = db.Column(db.String(100))
	Sentence = db.String(100)
	earliest_possible_dishcharge = db.Column(db.Date())
	lattest_possible_discharge = db.Column(db.Date())
	offence = db.Column(db.String(100))

class PreviousConviction(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_conviction = db.Column(db.Date())
	place_of_conviction = db.Column(db.String())
	place_where_sentence_was_served = db.Column(db.String(100))
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	list_of_properties = db.Column(db.String(400))
	#inmate = db.relationship('Inmate',backref="property")

	sentence = db.Column(db.String(100))
	offence = db.Column(db.String(100))

class Discharge(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_discharge = db.Column(db.Date())
	reason_for_discharge = db.Column(db.String(100))

class Property(Base):
	id = db.Column(db.Integer(),primary_key=True)
class Transfer(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(200))


#Residential Address
class ResidentialAddress(Base):
	id = db.Column(db.Integer,primary_key=True)
	country = db.Column(db.String(60))
	region = db.Column(db.String(60))
	area = db.Column(db.String(100))
	locality = db.Column(db.String(100))
	street = db.Column(db.String(100))
	housenumber = db.Column(db.String(20))

	'''addressCountry
	address_region
	address_locality
	postOfficeBoxNumber
	streetAddress
	postalCode
ra = ResidentialAddress(country="Ghana",region="Greater Accra",area="Ringway",locality="duncans",street="stuff",housenumber="12")

inmate = Inmate(serial_number="123",first_name="isaaac",last_name='something',middle_name="middle",alias='isaac',date_of_birth=datetime.date(1922,12,12),gender="male",distinctive_marks="well built",picture="avartar",language="akan",education="secondary",date_of_admission==datetime.date(2010,10,10),place_of_conviction="accra",offence="muder",place_of_offence=datetime.date(2004,10,10),sentence_years=4,sentence_months=40,sentence_days=21,block_cell = "f/32")\
pa = PostalAddress(country="Ghana",region="Greater Accra",city="Osu",zipcode='0000',box_number='an 10887')
	'''	



from datetime import date

#postal address
class PostalAddress(Base):
	id = db.Column(db.Integer,primary_key=True)
	country = db.Column(db.String(100))
	region = db .Column(db.String(100))
	city = db.Column(db.String(100))
	zipcode = db.Column(db.String(100))
	box_number = db.Column(db.String(30))
	#inmate_id = db.Column(db.Integer,db.ForeignKey('inmate.id')))



ra = ResidentialAddress(country="Ghana",region="Greater Accra",area="Ringway",locality="duncans",street="stuff",housenumber="12")

pa = PostalAddress(country="Ghana",region="Greater Accra",city="Osu",zipcode='0000',box_number='an 10887')

db.session.add(ra)
db.session.add(pa)
db.session.commit()
def add_inmate(ra,pa):
	import datetime
	inmate = Inmate(serial_number="123",first_name="isaaac",last_name='something',middle_name="middle",alias='isaac',
		date_of_birth=datetime.date(1922,12,12),gender="male",distinctive_marks="well built",picture="avartar",
		language="akan",education="secondary",date_of_admission=datetime.date(2010,10,10),
		place_of_conviction="accra",offence="murder",
		place_of_birth_country="Ghana",
		place_of_birth_region="greater accra",
		place_of_birth_locality="OSU",
		sentence_years=4,sentence_months=40,sentence_days=21,block_cell = "f/32")
	inmate.residential_address =ra
	inmate.postal_address = pa
	db.session.add(inmate)
	db.session.commit()
	return inmate

  