"""empty message

Revision ID: ad884bea3de8
Revises: 4dcec7de5747
Create Date: 2021-07-19 12:46:55.547796

"""
from alembic import op
import sqlalchemy as sa
import main.utils


# revision identifiers, used by Alembic.
revision = 'ad884bea3de8'
down_revision = '4dcec7de5747'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('camp_instance_registrations_spng_survey_camp_id_fkey', 'camp_instance_registrations', type_='foreignkey')
    op.drop_constraint('program_instance_registrations_spng_survey_program_id_fkey', 'program_instance_registrations', type_='foreignkey')
    op.drop_constraint('team_instance_registrations_spng_survey_team_id_fkey', 'team_instance_registrations', type_='foreignkey')
    op.create_table('spng_survey_camp_instances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spng_survey_program_instances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spng_survey_team_instances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('spng_survey_camps')
    op.drop_table('spng_survey_programs')
    op.drop_table('spng_survey_teams')
    op.add_column('camp_instance_registrations', sa.Column('spng_survey_camp_instance_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'camp_instance_registrations', 'spng_survey_camp_instances', ['spng_survey_camp_instance_id'], ['id'])
    op.drop_column('camp_instance_registrations', 'spng_survey_camp_id')
    op.add_column('program_instance_registrations', sa.Column('spng_survey_program_instance_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'program_instance_registrations', 'spng_survey_program_instances', ['spng_survey_program_instance_id'], ['id'])
    op.drop_column('program_instance_registrations', 'spng_survey_program_id')
    op.add_column('team_instance_registrations', sa.Column('spng_survey_team_instance_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'team_instance_registrations', 'spng_survey_team_instances', ['spng_survey_team_instance_id'], ['id'])
    op.drop_column('team_instance_registrations', 'spng_survey_team_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team_instance_registrations', type_='foreignkey')
    op.drop_constraint(None, 'program_instance_registrations', type_='foreignkey')
    op.drop_constraint(None, 'camp_instance_registrations', type_='foreignkey')
    op.add_column('team_instance_registrations', sa.Column('spng_survey_team_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('team_instance_registrations_spng_survey_team_id_fkey', 'team_instance_registrations', 'spng_survey_teams', ['spng_survey_team_id'], ['id'])
    op.drop_column('team_instance_registrations', 'spng_survey_team_instance_id')
    op.add_column('program_instance_registrations', sa.Column('spng_survey_program_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('program_instance_registrations_spng_survey_program_id_fkey', 'program_instance_registrations', 'spng_survey_programs', ['spng_survey_program_id'], ['id'])
    op.drop_column('program_instance_registrations', 'spng_survey_program_instance_id')
    op.add_column('camp_instance_registrations', sa.Column('spng_survey_camp_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('camp_instance_registrations_spng_survey_camp_id_fkey', 'camp_instance_registrations', 'spng_survey_camps', ['spng_survey_camp_id'], ['id'])
    op.drop_column('camp_instance_registrations', 'spng_survey_camp_instance_id')
    op.create_table('spng_survey_teams',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], name='spng_survey_teams_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='spng_survey_teams_pkey')
    )
    op.create_table('spng_survey_programs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], name='spng_survey_programs_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='spng_survey_programs_pkey')
    )
    op.create_table('spng_survey_camps',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['spng_surveys.id'], name='spng_survey_camps_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='spng_survey_camps_pkey')
    )
    op.drop_table('spng_survey_team_instances')
    op.drop_table('spng_survey_program_instances')
    op.drop_table('spng_survey_camp_instances')
    # ### end Alembic commands ###
