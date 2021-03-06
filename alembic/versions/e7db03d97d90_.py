"""empty message

Revision ID: e7db03d97d90
Revises: 086a428f2f85
Create Date: 2021-08-09 15:43:48.997597

"""
from alembic import op
import sqlalchemy as sa
import main.utils


# revision identifiers, used by Alembic.
revision = 'e7db03d97d90'
down_revision = '086a428f2f85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('email', sa.String(), nullable=True))
    op.create_index(op.f('ix_players_email'), 'players', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_players_email'), table_name='players')
    op.drop_column('players', 'email')
    # ### end Alembic commands ###
