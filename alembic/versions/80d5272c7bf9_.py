"""empty message

Revision ID: 80d5272c7bf9
Revises: 5f8ee52b4320
Create Date: 2021-07-22 19:13:45.819913

"""
from alembic import op
import sqlalchemy as sa
import main.utils


# revision identifiers, used by Alembic.
revision = '80d5272c7bf9'
down_revision = '5f8ee52b4320'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_instance_jersey_socks_order_requests', sa.Column('rejected_reason', sa.String(), nullable=True))
    op.drop_column('team_instance_jersey_socks_order_requests', 'rejection_reason')
    op.add_column('team_instance_tracksuit_order_requests', sa.Column('rejected_reason', sa.String(), nullable=True))
    op.drop_column('team_instance_tracksuit_order_requests', 'rejection_reason')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_instance_tracksuit_order_requests', sa.Column('rejection_reason', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('team_instance_tracksuit_order_requests', 'rejected_reason')
    op.add_column('team_instance_jersey_socks_order_requests', sa.Column('rejection_reason', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('team_instance_jersey_socks_order_requests', 'rejected_reason')
    # ### end Alembic commands ###