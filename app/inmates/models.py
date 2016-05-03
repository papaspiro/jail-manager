from app import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())

'''
class User(Base):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(60))
	pwdhash = db.Column(db.String(60))
	admin = db.Column(db.Boolean)
	email  = db.Column(db.String(60))

	def __init__(self,username,password,admin):
		self.username = username
		self.pwdhash = generate_password_hash(password)
		self.admin = admin

	def isadmin(self):
		return self.admin

class Inmate(Base):

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

 
	#administrative data
	offence = db.Column(db.String(100))
	place_of_offence_country = db.Column(db.String(100))
	place_of_offence_region = db.Column(db.String(100))
	place_of_offence_locality = db.Column(db.String(100))

	place_of_conviction = db.Column(db.String())
	date_of_sentence = db.Column(db.Date())
	sentence_years = db.Column(db.Integer())
	sentence_months = db.Column(db.Integer())
	sentence_days = db.Column(db.Integer()) 

	date_of_admission = db.Column(db.Date())
	block_cell = db.Column(db.String(10))

	def __unicode__(self):
		return str( self.serial_number)

	



#postal address
class PostalAddress(Base):
	id = db.Column(db.Integer,primary_key=True)
	country = db.Column(db.String(100))
	region = db .Column(db.String(100))
	#locality = db .Column(db.String(100))
	#other_info = db .Column(db.String(100))
	city = db.Column(db.String(100))
	zipcode = db.Column(db.String(100))
	box_number = db.Column(db.String(30))
	#inmate_id = db.Column(db.Integer,db.ForeignKey('inmate.id')))


#bridge table
class InmatePostalAddress(Base):
	id = db.Column('id',db.Integer,primary_key=True)
	inmate_id = db.Column('inmate_id',db.Integer,db.ForeignKey('inmate.id'))
	postal_address_id = db.Column('postal_address_id',db.Integer,db.ForeignKey('postal_address.id'))
	
	#relationships
	inmate = db.relationship('Inmate',foreign_keys=inmate_id)
	address = db.relationship('PostalAddress',foreign_keys=postal_address_id) 



#Residential Address
class ResidentialAddress(Base):
	id = db.Column(db.Integer,primary_key=True)
	country = db.Column(db.String(60))
	region = db.Column(db.String(60))
	area = db.Column(db.String(100))
	other_address_info = db.Column(db.String(30))
	locality = db.Column(db.String(100))
	street = db.Column(db.String(100))
	housenumber = db.Column(db.String(30))
	


#bridge table 
class InmateResidentialAddress(Base):
	id = db.Column('id',db.Integer,primary_key=True)
	inmate_id = db.Column('inmate_id',db.Integer,db.ForeignKey('inmate.id'))
	residential_address_id = db.Column('residential_address_id',db.Integer,db.ForeignKey('residential_address.id'))


	#relationships
	inmate = db.relationship('Inmate',foreign_keys=inmate_id)
	address = db.relationship('ResidentialAddress',foreign_keys=residential_address_id) 



#bridge table 
class InmateAddressOnDischarge(Base):
	id = db.Column('id',db.Integer,primary_key=True)
	inmate_id = db.Column('inmate_id',db.Integer,db.ForeignKey('inmate.id'))
	residential_address_id = db.Column('residential_address_id',db.Integer,db.ForeignKey('residential_address.id'))

	#relationships
	inmate = db.relationship('Inmate',foreign_keys=inmate_id)
	address = db.relationship('ResidentialAddress',foreign_keys=residential_address_id) 




#the next of kin
class NextOfKin(Base):
	id = db.Column(db.Integer,primary_key=True )
	first_name = db.Column(db.String(100))
	middle_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	telephone = db.Column(db.String(30))
	relationship = db.Column(db.String(30))
	
	#foreignkey
	inmate_id = db.Column(db.ForeignKey('inmate.id'))		
	
	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="nextofkin")

	def __unicode__(self):
		u_rep = "%s of inmate %s"   %(str(self.relationship),str(self.inmate.serial_number))
		return  u_rep  #u_rep.encode("latin-1")

#bridge table 
class NextOfKinResidentialAddress(Base):
	id = db.Column('id',db.Integer,primary_key=True)
	next_of_kin_id = db.Column('next_of_kin_id',db.Integer,db.ForeignKey('next_of_kin.id'))
	residential_address_id = db.Column('residential_address_id',db.Integer,db.ForeignKey('residential_address.id'))

	#relationships
	nextofkin = db.relationship('NextOfKin',foreign_keys=next_of_kin_id)
	address = db.relationship('ResidentialAddress',foreign_keys=residential_address_id) 



#bridge table 
class NextOfKinPostalAddress(Base):
	id = db.Column('id',db.Integer,primary_key=True)
	next_of_kin_id = db.Column('next_of_kin_id',db.Integer,db.ForeignKey('next_of_kin.id'))
	postal_address_id = db.Column('postal_address_id',db.Integer,db.ForeignKey('postal_address.id'))

	#relationships
	nextofkin = db.relationship('NextOfKin',foreign_keys=next_of_kin_id)
	address = db.relationship('PostalAddress',foreign_keys=postal_address_id) 



class PenalRecord(Base):
	id = db.Column(db.Integer,primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey("inmate.id"))
	date_of_conviction = db.Column(db.Date())
	place_of_conviction = db.Column(db.String(100))
	remission = db.Column(db.String(100))
	offence = db.Column(db.String(200))
	country_of_offence = db.Column(db.String(200))
	region_of_offence = db.Column(db.String(200))
	locality_of_offence = db.Column(db.String(200))

	sentence = db.String(100)
	earliest_possible_dishcharge = db.Column(db.Date())
	lattest_possible_discharge = db.Column(db.Date())


	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="penal_record")



class PreviousConviction(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_conviction = db.Column(db.Date())
	place_of_conviction = db.Column(db.String())
	place_where_sentence_was_served = db.Column(db.String(100))
	sentence = db.Column(db.String(100))
	offence = db.Column(db.String(150))

	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="previous_conviction")


class Discharge(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_discharge = db.Column(db.Date())
	reason_for_discharge = db.Column(db.String(100))

	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="discharge")


class Property(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	items = db.Column(db.String(500))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="property")


class Transfer(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(300))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="transfers")
	


'''


class CorrectionalFacility(Base):
	 id = db.Column(db.Integer(),primary_key=True)
	 name = db.Column(db.String(90))
	 code = db.Column(db.String(4),unique=True)


class Inmate(Base):
	id = db.Column(db.Integer(),primary_key=True)
	serial_number = db.Column(db.String(24),unique=True,nullable=False)
	picture = db.Column(db.String(120))
	first_name = db.Column(db.String(120),nullable=False)
	middle_name = db.Column(db.String(12))
	last_name = db.Column(db.String(120),nullable=False)
	distinctive_marks = db.Column(db.String(250))


	date_of_birth = db.Column(db.Date())
	languages = db.Column(db.String(120))
	education = db.Column(db.String(120))

	complexion = db.Column(db.String(120),nullable=False)
	nationality = db.Column(db.String(120),nullable=False)
	tribe = db.Column(db.String(120),nullable=False)
	thumbprint = db.Column(db.String(),nullable=False)

	inmate_residential_address_id = db.Column(db.Integer(),db.ForeignKey('inmate_residential_address.id',user_alter=True,))
	#residential_address = db.relationship('InmateResidentialAddress',foreign_keys=inmate_residential_address_id)
	#postal_address = db.relationship('InmatePostalAddress',foreign_keys=inmate_residential_address_id )


	def __str__(self):
		return "inmate  %s %s %s"  %(self.last_name , self.first_name ,self.serial_number) 


class PenalRecord(Base):
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
	#place_id = db.Column(db.Integer(),db.ForeignKey('place.id'))
	correctional_facility_id = db.Column(db.Integer(),db.ForeignKey('correctional_facility.id'))


	#relationships

	#relations
	inmate = db.relationship(Inmate,backref='penal_records')
	##place_of_committal = db.relationship(CorrectionalFacility,backref = "penal_records")


class NextOfKin(Base):
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

class PreviousConviction(Base):
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


class Discharge(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	date_of_discharge = db.Column(db.Date())
	reason_for_discharge = db.Column(db.String(100))

	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="discharge")


class Property(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	items = db.Column(db.String(500))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="property")


class Transfer(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(300))

	#relationship
	inmate = db.relationship(Inmate,foreign_keys=inmate_id,backref="transfers")
	



#bridge tables
class NOKPostalAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	#postal_addresses_id = db.Column(db.Integer(),db.ForeignKey('postal_address.id'))
	next_of_kin_id = db.Column(db.Integer(),db.ForeignKey('next_of_kin.id'))	
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='0000')
	box_number = db.Column(db.String(120),nullable=False)

	#relationships
	next_of_kin = db.relationship(NextOfKin,backref="postal_address")


class NOKResidentialAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	
	#foreignkeys
	next_of_kin_id = db.Column(db.Integer(),db.ForeignKey('next_of_kin.id'))
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='')
	house_number = db.Column(db.String(20),nullable=False,default='NA')
	street  = db.Column(db.String(20),nullable=False,default='NA')

	#relationships
	#residential_address = db.relationship(ResidentialAddress,backref="nok_residential_address")
	next_of_kin = db.relationship(NextOfKin,backref="residential_address")



class InmatePostalAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='0000')
	box_number = db.Column(db.String(120),nullable=False)


	#relationship
	inmate_pa = db.relationship(Inmate,foreign_keys=inmate_id,backref='postal_address')

	#inline_models = [PostalAddress]


class InmateResidentialAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='0000')
	box_number = db.Column(db.String(120),nullable=False)

	#relationship
	#residential_address = db.relationship(ResidentialAddress,backref="inmate_residential_address")
	inmate_ra = db.relationship(Inmate,foreign_keys=inmate_id,backref='residential_address')




