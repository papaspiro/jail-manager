"""empty message

Revision ID: a88d4f7ada3
Revises: None
Create Date: 2016-03-31 03:17:41.333278

"""

# revision identifiers, used by Alembic.
revision = 'a88d4f7ada3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=130), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('inmate',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serial_number', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('alias', sa.String(length=60), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('distinctive_marks', sa.String(length=250), nullable=True),
    sa.Column('picture', sa.String(length=150), nullable=True),
    sa.Column('place_of_birth_country', sa.String(length=100), nullable=True),
    sa.Column('place_of_birth_region', sa.String(length=100), nullable=True),
    sa.Column('place_of_birth_locality', sa.String(length=100), nullable=True),
    sa.Column('language', sa.String(length=100), nullable=True),
    sa.Column('education', sa.String(length=100), nullable=True),
    sa.Column('place_of_offence_country', sa.String(length=100), nullable=True),
    sa.Column('place_of_offence_region', sa.String(length=100), nullable=True),
    sa.Column('place_of_offence_locality', sa.String(length=100), nullable=True),
    sa.Column('offence', sa.String(length=100), nullable=True),
    sa.Column('place_of_conviction', sa.String(), nullable=True),
    sa.Column('date_of_sentence', sa.Date(), nullable=True),
    sa.Column('sentence_years', sa.Integer(), nullable=True),
    sa.Column('sentence_months', sa.Integer(), nullable=True),
    sa.Column('sentence_days', sa.Integer(), nullable=True),
    sa.Column('date_of_admission', sa.Date(), nullable=True),
    sa.Column('block_cell', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('postal_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('region', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('zipcode', sa.String(length=100), nullable=True),
    sa.Column('box_number', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('residential_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('region', sa.String(length=60), nullable=True),
    sa.Column('area', sa.String(length=100), nullable=True),
    sa.Column('other_address_info', sa.String(length=30), nullable=True),
    sa.Column('locality', sa.String(length=100), nullable=True),
    sa.Column('street', sa.String(length=100), nullable=True),
    sa.Column('housenumber', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('pwdhash', sa.String(length=60), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discharge',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('date_of_discharge', sa.Date(), nullable=True),
    sa.Column('reason_for_discharge', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inmate_address_on_discharge',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('residential_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.ForeignKeyConstraint(['residential_address_id'], ['residential_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inmate_postal_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('postal_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.ForeignKeyConstraint(['postal_address_id'], ['postal_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inmate_residential_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('residential_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.ForeignKeyConstraint(['residential_address_id'], ['residential_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('next_of_kin',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('telephone', sa.String(length=30), nullable=True),
    sa.Column('relationship', sa.String(length=30), nullable=True),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('penal_record',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('date_of_conviction', sa.Date(), nullable=True),
    sa.Column('place_of_conviction', sa.String(length=100), nullable=True),
    sa.Column('remission', sa.String(length=100), nullable=True),
    sa.Column('offence', sa.String(length=200), nullable=True),
    sa.Column('earliest_possible_dishcharge', sa.Date(), nullable=True),
    sa.Column('lattest_possible_discharge', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('previous_conviction',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('date_of_conviction', sa.Date(), nullable=True),
    sa.Column('place_of_conviction', sa.String(), nullable=True),
    sa.Column('place_where_sentence_was_served', sa.String(length=100), nullable=True),
    sa.Column('sentence', sa.String(length=100), nullable=True),
    sa.Column('offence', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('property',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('items', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transfer',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inmate_id', sa.Integer(), nullable=True),
    sa.Column('date_of_transfer', sa.Date(), nullable=True),
    sa.Column('station_transferred_to', sa.String(length=100), nullable=True),
    sa.Column('reason_for_transfer', sa.String(length=200), nullable=True),
    sa.Column('items_accompanying_inmate', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['inmate_id'], ['inmate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('next_of_kin_postal_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('next_of_kin_id', sa.Integer(), nullable=True),
    sa.Column('postal_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['next_of_kin_id'], ['next_of_kin.id'], ),
    sa.ForeignKeyConstraint(['postal_address_id'], ['postal_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('next_of_kin_residential_address',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('next_of_kin_id', sa.Integer(), nullable=True),
    sa.Column('residential_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['next_of_kin_id'], ['next_of_kin.id'], ),
    sa.ForeignKeyConstraint(['residential_address_id'], ['residential_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('next_of_kin_residential_address')
    op.drop_table('next_of_kin_postal_address')
    op.drop_table('transfer')
    op.drop_table('property')
    op.drop_table('previous_conviction')
    op.drop_table('penal_record')
    op.drop_table('next_of_kin')
    op.drop_table('inmate_residential_address')
    op.drop_table('inmate_postal_address')
    op.drop_table('inmate_address_on_discharge')
    op.drop_table('discharge')
    op.drop_table('user')
    op.drop_table('residential_address')
    op.drop_table('postal_address')
    op.drop_table('inmate')
    op.drop_table('auth_user')
    ### end Alembic commands ###
