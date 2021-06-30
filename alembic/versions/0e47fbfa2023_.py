"""empty message

Revision ID: 0e47fbfa2023
Revises: 
Create Date: 2021-06-28 13:52:33.633132

"""
from alembic import op
import sqlalchemy as sa
import lib


# revision identifiers, used by Alembic.
revision = '0e47fbfa2023'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('camp_instance_registrations', sa.Column('spng_persona_id', sa.Integer(), nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('spng_survey_id', sa.Integer(), nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('spng_survey_result_id', sa.Integer(), nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('spng_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('camp_instance_registrations_se_survey_result_id_key', 'camp_instance_registrations', type_='unique')
    op.create_unique_constraint(None, 'camp_instance_registrations', ['spng_survey_result_id'])
    op.drop_column('camp_instance_registrations', 'se_survey_id')
    op.drop_column('camp_instance_registrations', 'se_user_id')
    op.drop_column('camp_instance_registrations', 'se_persona_id')
    op.drop_column('camp_instance_registrations', 'se_survey_result_id')
    op.add_column('camp_instances', sa.Column('spng_name_snake', sa.String(), nullable=True))
    op.add_column('camp_instances', sa.Column('spng_shared_question_id', sa.Integer(), nullable=True))
    op.drop_index('ix_camp_instances_se_name_snake', table_name='camp_instances')
    op.drop_index('ix_camp_instances_se_shared_question_id', table_name='camp_instances')
    op.create_index(op.f('ix_camp_instances_spng_name_snake'), 'camp_instances', ['spng_name_snake'], unique=False)
    op.create_index(op.f('ix_camp_instances_spng_shared_question_id'), 'camp_instances', ['spng_shared_question_id'], unique=False)
    op.drop_column('camp_instances', 'se_shared_question_id')
    op.drop_column('camp_instances', 'se_name_snake')
    op.add_column('players', sa.Column('spng_persona_id', sa.Integer(), nullable=True))
    op.drop_constraint('players_se_persona_id_key', 'players', type_='unique')
    op.create_unique_constraint(None, 'players', ['spng_persona_id'])
    op.drop_column('players', 'se_persona_id')
    op.add_column('program_instance_registrations', sa.Column('spng_persona_id', sa.Integer(), nullable=True))
    op.add_column('program_instance_registrations', sa.Column('spng_survey_id', sa.Integer(), nullable=True))
    op.add_column('program_instance_registrations', sa.Column('spng_survey_result_id', sa.Integer(), nullable=True))
    op.add_column('program_instance_registrations', sa.Column('spng_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('program_instance_registrations_se_survey_result_id_key', 'program_instance_registrations', type_='unique')
    op.create_unique_constraint(None, 'program_instance_registrations', ['spng_survey_result_id'])
    op.drop_column('program_instance_registrations', 'se_survey_id')
    op.drop_column('program_instance_registrations', 'se_user_id')
    op.drop_column('program_instance_registrations', 'se_persona_id')
    op.drop_column('program_instance_registrations', 'se_survey_result_id')
    op.add_column('program_instances', sa.Column('spng_name_snake', sa.String(), nullable=True))
    op.add_column('program_instances', sa.Column('spng_shared_question_id', sa.Integer(), nullable=True))
    op.drop_index('ix_program_instances_se_name_snake', table_name='program_instances')
    op.drop_index('ix_program_instances_se_shared_question_id', table_name='program_instances')
    op.create_index(op.f('ix_program_instances_spng_name_snake'), 'program_instances', ['spng_name_snake'], unique=False)
    op.create_index(op.f('ix_program_instances_spng_shared_question_id'), 'program_instances', ['spng_shared_question_id'], unique=False)
    op.drop_column('program_instances', 'se_shared_question_id')
    op.drop_column('program_instances', 'se_name_snake')
    op.add_column('team_instance_registrations', sa.Column('spng_persona_id', sa.Integer(), nullable=True))
    op.add_column('team_instance_registrations', sa.Column('spng_survey_id', sa.Integer(), nullable=True))
    op.add_column('team_instance_registrations', sa.Column('spng_survey_result_id', sa.Integer(), nullable=True))
    op.add_column('team_instance_registrations', sa.Column('spng_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('team_instance_registrations_se_survey_result_id_key', 'team_instance_registrations', type_='unique')
    op.create_unique_constraint(None, 'team_instance_registrations', ['spng_survey_result_id'])
    op.drop_column('team_instance_registrations', 'se_survey_id')
    op.drop_column('team_instance_registrations', 'se_user_id')
    op.drop_column('team_instance_registrations', 'se_persona_id')
    op.drop_column('team_instance_registrations', 'se_survey_result_id')
    op.add_column('team_instances', sa.Column('spng_name_snake', sa.String(), nullable=True))
    op.add_column('team_instances', sa.Column('spng_shared_question_id', sa.Integer(), nullable=True))
    op.drop_index('ix_team_instances_se_name_snake', table_name='team_instances')
    op.drop_index('ix_team_instances_se_shared_question_id', table_name='team_instances')
    op.create_index(op.f('ix_team_instances_spng_name_snake'), 'team_instances', ['spng_name_snake'], unique=False)
    op.create_index(op.f('ix_team_instances_spng_shared_question_id'), 'team_instances', ['spng_shared_question_id'], unique=False)
    op.drop_column('team_instances', 'se_shared_question_id')
    op.drop_column('team_instances', 'se_name_snake')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_instances', sa.Column('se_name_snake', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('team_instances', sa.Column('se_shared_question_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_team_instances_spng_shared_question_id'), table_name='team_instances')
    op.drop_index(op.f('ix_team_instances_spng_name_snake'), table_name='team_instances')
    op.create_index('ix_team_instances_se_shared_question_id', 'team_instances', ['se_shared_question_id'], unique=False)
    op.create_index('ix_team_instances_se_name_snake', 'team_instances', ['se_name_snake'], unique=False)
    op.drop_column('team_instances', 'spng_shared_question_id')
    op.drop_column('team_instances', 'spng_name_snake')
    op.add_column('team_instance_registrations', sa.Column('se_survey_result_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('se_persona_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('se_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('se_survey_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'team_instance_registrations', type_='unique')
    op.create_unique_constraint('team_instance_registrations_se_survey_result_id_key', 'team_instance_registrations', ['se_survey_result_id'])
    op.drop_column('team_instance_registrations', 'spng_user_id')
    op.drop_column('team_instance_registrations', 'spng_survey_result_id')
    op.drop_column('team_instance_registrations', 'spng_survey_id')
    op.drop_column('team_instance_registrations', 'spng_persona_id')
    op.add_column('program_instances', sa.Column('se_name_snake', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('program_instances', sa.Column('se_shared_question_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_program_instances_spng_shared_question_id'), table_name='program_instances')
    op.drop_index(op.f('ix_program_instances_spng_name_snake'), table_name='program_instances')
    op.create_index('ix_program_instances_se_shared_question_id', 'program_instances', ['se_shared_question_id'], unique=False)
    op.create_index('ix_program_instances_se_name_snake', 'program_instances', ['se_name_snake'], unique=False)
    op.drop_column('program_instances', 'spng_shared_question_id')
    op.drop_column('program_instances', 'spng_name_snake')
    op.add_column('program_instance_registrations', sa.Column('se_survey_result_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('se_persona_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('se_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('se_survey_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'program_instance_registrations', type_='unique')
    op.create_unique_constraint('program_instance_registrations_se_survey_result_id_key', 'program_instance_registrations', ['se_survey_result_id'])
    op.drop_column('program_instance_registrations', 'spng_user_id')
    op.drop_column('program_instance_registrations', 'spng_survey_result_id')
    op.drop_column('program_instance_registrations', 'spng_survey_id')
    op.drop_column('program_instance_registrations', 'spng_persona_id')
    op.add_column('players', sa.Column('se_persona_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'players', type_='unique')
    op.create_unique_constraint('players_se_persona_id_key', 'players', ['se_persona_id'])
    op.drop_column('players', 'spng_persona_id')
    op.add_column('camp_instances', sa.Column('se_name_snake', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('camp_instances', sa.Column('se_shared_question_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_camp_instances_spng_shared_question_id'), table_name='camp_instances')
    op.drop_index(op.f('ix_camp_instances_spng_name_snake'), table_name='camp_instances')
    op.create_index('ix_camp_instances_se_shared_question_id', 'camp_instances', ['se_shared_question_id'], unique=False)
    op.create_index('ix_camp_instances_se_name_snake', 'camp_instances', ['se_name_snake'], unique=False)
    op.drop_column('camp_instances', 'spng_shared_question_id')
    op.drop_column('camp_instances', 'spng_name_snake')
    op.add_column('camp_instance_registrations', sa.Column('se_survey_result_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('se_persona_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('se_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('se_survey_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'camp_instance_registrations', type_='unique')
    op.create_unique_constraint('camp_instance_registrations_se_survey_result_id_key', 'camp_instance_registrations', ['se_survey_result_id'])
    op.drop_column('camp_instance_registrations', 'spng_user_id')
    op.drop_column('camp_instance_registrations', 'spng_survey_result_id')
    op.drop_column('camp_instance_registrations', 'spng_survey_id')
    op.drop_column('camp_instance_registrations', 'spng_persona_id')
    # ### end Alembic commands ###