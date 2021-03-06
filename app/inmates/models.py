from app import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())



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
	alias  = db.Column(db.String(120))
	distinctive_marks = db.Column(db.String(250))


	date_of_birth = db.Column(db.Date())
	languages = db.Column(db.String(120))
	education = db.Column(db.String(120))

	complexion = db.Column(db.String(120),nullable=False)
	nationality = db.Column(db.String(120),nullable=False)
	tribe = db.Column(db.String(120))
	thumbprint = db.Column(db.String(120))

	#inmate_residential_address_id = db.Column(db.Integer(),db.ForeignKey('inmate_residential_address.id',user_alter=True,))
	#inmate_postal_address_id = db.Column(db.Integer(),db.ForeignKey('inmate_postal_address.id',user_alter=True,))

	#relationships
	#residential_address = db.relationship('InmateResidentialAddress',backref="serial_number",uselist=False)
	#postal_address = db.relationship('InmatePostalAddress',backref="serial_number",uselist=False )



	def __str__(self):
		return "inmate  %s  %s %s  alias %s"  %(self.last_name , self.first_name ,self.serial_number,self.alias) 

class InmatePostalAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='0000')
	box_number = db.Column(db.String(120),nullable=False)

	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	serial_number = db.relationship('Inmate',backref='postal_address')


class InmateResidentialAddress(Base):
	id = db.Column(db.Integer(),primary_key=True)
	country = db.Column(db.String(160),nullable=False)
	region = db.Column(db.String(160),nullable=False)
	locality = db.Column(db.String(160),nullable=False)
	postal_code = db.Column(db.String(10),nullable=False , default='0000')
	box_number = db.Column(db.String(120),nullable=False)

	#relationship
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))
	serial_number = db.relationship('Inmate',backref='residential_address',uselist=False)


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
	serial_number = db.relationship('Inmate',backref='penal_records')
	##place_of_committal = db.relationship(CorrectionalFacility,backref = "penal_records")

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
	serial_number = db.relationship(Inmate,backref="previous_conviction")
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
	serial_number = db.relationship(Inmate,foreign_keys=inmate_id,backref="property")


class Transfer(Base):
	id = db.Column(db.Integer(),primary_key=True)
	inmate_id = db.Column(db.Integer(), db.ForeignKey('inmate.id'))
	date_of_transfer = db.Column(db.Date())
	station_transferred_to = db.Column(db.String(100))
	reason_for_transfer = db.Column(db.String(200))
	items_accompanying_inmate = db.Column(db.String(300))

	#relationship
	serial_number = db.relationship(Inmate,foreign_keys=inmate_id,backref="transfers")
	
class NextOfKin(Base):
	id = db.Column(db.Integer(),primary_key=True)
	first_name = db.Column(db.String(120),nullable=False)
	middle_name = db.Column(db.String(120))
	last_name = db.Column(db.String(120) ,nullable=False)
	relation_to_inmate = db.Column(db.String(120),nullable=False )
	email = db.Column(db.String(120),nullable=False)

	#foreign keys
	inmate_id = db.Column(db.Integer(),db.ForeignKey('inmate.id'))

	#relations
	serial_number = db.relationship(Inmate,backref='next_of_kin')

	def __str__(self):
		return  " %s of %s" %(unicode(self.relation),unicode(self.inmate.serial_number))

	def get_inmate_by_id(id):
		pass

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
	next_of_kin = db.relationship(NextOfKin,backref="postal_address",uselist=False)

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
	next_of_kin = db.relationship(NextOfKin,backref="residential_address",uselist=False)




