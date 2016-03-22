from flask.ext.wtf import Form #RecaptchaField
from wtforms import StringField,BooleanField,PasswordField,TextField,SelectField,FileField,TextAreaField
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, DataRequired,Email,EqualTo,regexp

'''class UserDetails(Form):
    group_id = SelectField(u'Group', coerce=int)

def edit_user(request, id):
    user = User.query.get(id)
    form = UserDetails(request.POST, obj=user)
    form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]




class UserForm(Form):
	user_name = StringField('Username',validators=[DataRequired()])
	password = StringField('Password',validators=[DataRequired()])
	admin = BooleanField('Is Admin ?',validators=[DataRequired()])


'''


class InmateForm(Form):
	serial_number = StringField('Serial Number',validators=[ DataRequired()] )
	first_name = StringField('First Name',validators=[ DataRequired()] )
	middle_name = StringField('Middle Name',validators=[DataRequired()] )
	last_name = StringField('Last Name',validators=[DataRequired()] )
	alias = StringField('Alias', validators =[DataRequired()])
	date_of_birth = DateField("Date of Birth",validators=[DataRequired()])
	gender = SelectField('Gender', choices=[('male','Male'),('female','Female')])
	distinctive_marks = TextAreaField('Distinctive Marks',validators=[DataRequired()])

	place_of_birth_country = StringField('Country Of Birth',validators=[DataRequired()])
	place_of_birth_region = StringField('Region of Birth',validators=[DataRequired()])
	place_of_birth_locality = StringField('Locality of Birth',validators=[DataRequired()])

	education = StringField('Education',validators=[DataRequired()])

	language = StringField('Language', validators=[DataRequired()])
	place_of_offence_country = StringField('Country of Offence',validators=[DataRequired()])
	place_of_offence_region = StringField('Region of Offence',validators=[DataRequired()])
	place_of_offence_locality = StringField('Locality of Offence',validators=[DataRequired()])

	offence = StringField("Offence",validators=[DataRequired()])
	place_of_conviction = StringField('Place of Conviction')
	date_of_admission = DateField('Date of Admission',validators = [DataRequired()])
	date_of_sentence = DateField('Date of Sentence',validators=[DataRequired()])

	sentence_years = StringField('Years of Sentence',validators=[DataRequired()])
	sentence_months = StringField('Months of Sentence',validators=[DataRequired()])
	sentence_days = StringField('Days of Sentence',validators=[DataRequired()])

	block_cell = StringField('Blocks /Cell',validators=[DataRequired()])

	picture = FileField('picture',)
	submit = SubmitField('Submit')


class PostalAddressForm(Form):
	serial_number = StringField('Serial Number',validators=[ DataRequired()] )
	country = StringField('Country',validators=[Required()])
	region = StringField('Region',validators=[Required()])
	city = StringField('City',validators=[Required()])
	zip_code = StringField('Zip Code')
	box_number = StringField('Box Number',validators=[Required])
	submit = SubmitField('Submit')



class ResidentalForm(Form):
	serial_number = StringField('Serial Number',validators=[ DataRequired()] )
	country = StringField('Country',validators=[Required()])
	region = StringField('Region', validators=[Required()])
	area = StringField('City',validators=[Required()])
	locality = StringField('Locality',validators=[Required()])
	submit = SubmitField('Submit')


class NextOfKinForm(Form):
	serial_number = StringField('Serial Number',validators=[ DataRequired()] )
	first_name = StringField('First Name',validators=[ DataRequired()] )
	middle_name = StringField('Middle Name',validators=[DataRequired()] )
	last_name = StringField('Last Name',validators=[DataRequired()] )
	alias = StringField('Relationship', validators =[DataRequired()])
	telephone = StringField('Telephone',validators=[DataRequired])
	
	#contact address
	residence_country = StringField('Country of Residence',validators=[Required()])
	residence_region = StringField('Region of Residence',validators=[Required()])
	residence_city = StringField('City of Residence',validators=[Required()])
	zip_code = StringField('Zip Code')

	postal_country = StringField('Postal Address Country',validators=[Required()])
	postal_region = StringField('Postal Address of Region',validators=[Required()])
	postal_city = StringField('Postal Address City',validators=[Required()])
	postal_box = StringField('Postal Office Box Number',validators=[Required()])
	postal_other = StringField('Postal Address other',validators=[Required()])	
	submit = SubmitField('Submit')



class PenalRecordForm(Form):
	serial_number = StringField('Serail Number',validators=[DataRequired()])
	place_of_conviction = StringField('Place of Conviction',validators=[DataRequired()])
	date_of_conviction = DateField('Date of Conviction',validators=[DataRequired()])
	offence = StringField("Offence",validators=[DataRequired()])
	remission = StringField("Remission",validators=[DataRequired()])
	earliest_possible_discharge = DateField('Date of Admission',validators = [DataRequired()])
	lattest_possible_discharge = DateField('Date of Sentence',validators=[DataRequired()])
	submit = SubmitField('Submit')



class PreviousConviction(Form):
	serial_number = StringField('Serail Number',validators=[DataRequired()])
	offence = StringField("Offence",validators=[DataRequired()])
	sentence = StringField("Offence",validators=[DataRequired()])
	place_of_conviction = StringField('Place of Conviction',validators=[DataRequired()])
	date_of_conviction = DateField('Date of Conviction',validators=[DataRequired()])
	submit = SubmitField('Submit')


class DischargeForm(Form):
	serial_number = StringField('Serial Number', validators=[DataRequired()])
	items = TextAreaField('Items Accompanying Inmate',validators=[DataRequired()])
	reason_for_discharge = TextAreaField('Reason For Discharge',validators=[DataRequired()])
	submit = SubmitField('Submit')


class PropertyForm(Form):
	serial_number = StringField('Serial Number', validators=[DataRequired()])
	items = TextAreaField('Items' ,validators=[DataRequired()])
	submit = SubmitField('Submit')


class TransferForm(Form):
	serial_number = StringField('Serial Number', validators=[DataRequired()])
	date_of_transfer = DateField('Date of Transfer',validators=[DataRequired()])
	station_transferred_to = StringField("Station Transfered To",validators=[DataRequired()])
	reason_for_transfer = StringField("Reason For Transfer",validators=[DataRequired()])
	items_accompanying_inmate = TextAreaField('Items Accompanying Inmate',validators=[DataRequired()])
	submit = SubmitField('Submit')





