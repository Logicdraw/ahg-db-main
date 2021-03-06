"""empty message

Revision ID: ad268baab9dc
Revises: e7db03d97d90
Create Date: 2021-08-10 13:31:22.994422

"""
from alembic import op
import sqlalchemy as sa
import main.utils


# revision identifiers, used by Alembic.
revision = 'ad268baab9dc'
down_revision = 'e7db03d97d90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('mobile_phone', sa.String(), nullable=True))
    op.drop_index('ix_players_email', table_name='players')
    op.create_index(op.f('ix_players_email'), 'players', ['email'], unique=True)
    op.create_index(op.f('ix_players_mobile_phone'), 'players', ['mobile_phone'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_players_mobile_phone'), table_name='players')
    op.drop_index(op.f('ix_players_email'), table_name='players')
    op.create_index('ix_players_email', 'players', ['email'], unique=False)
    op.drop_column('players', 'mobile_phone')
    # ### end Alembic commands ###
