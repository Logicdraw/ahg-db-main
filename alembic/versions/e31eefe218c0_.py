"""empty message

Revision ID: e31eefe218c0
Revises: 6df81505bf5c
Create Date: 2021-05-29 14:30:53.756324

"""
from alembic import op
import sqlalchemy as sa
import lib


# revision identifiers, used by Alembic.
revision = 'e31eefe218c0'
down_revision = '6df81505bf5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('camp_instance_registrations', 'preferred_language')
    op.drop_column('camp_instance_registrations', 'invited_by_coach')
    op.drop_column('camp_instance_registrations', 'current_division_played')
    op.drop_column('camp_instance_registrations', 'current_minor_hockey_level')
    op.drop_column('program_instance_registrations', 'preferred_language')
    op.drop_column('program_instance_registrations', 'invited_by_coach')
    op.drop_column('program_instance_registrations', 'current_division_played')
    op.drop_column('program_instance_registrations', 'current_minor_hockey_level')
    op.drop_column('team_instance_registrations', 'preferred_language')
    op.drop_column('team_instance_registrations', 'invited_by_coach')
    op.drop_column('team_instance_registrations', 'current_division_played')
    op.drop_column('team_instance_registrations', 'current_minor_hockey_level')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_instance_registrations', sa.Column('current_minor_hockey_level', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('current_division_played', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('invited_by_coach', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('team_instance_registrations', sa.Column('preferred_language', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('current_minor_hockey_level', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('current_division_played', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('invited_by_coach', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('program_instance_registrations', sa.Column('preferred_language', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('current_minor_hockey_level', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('current_division_played', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('invited_by_coach', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('camp_instance_registrations', sa.Column('preferred_language', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
