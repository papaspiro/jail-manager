from app import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())


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

	place_of_offence_country = db.Column(db.String(100))
	place_of_offence_region = db.Column(db.String(100))
	place_of_offence_locality = db.Column(db.String(100))
 

	#administrative data
	offence = db.Column(db.String(100))
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
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="property")


class Transfer(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(300))

	#relationship
	inmate = db.relationship('Inmate',foreign_keys=inmate_id,backref="transfers")
	





