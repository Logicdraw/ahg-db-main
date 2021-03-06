"""empty message

Revision ID: 086a428f2f85
Revises: 5453c962223e
Create Date: 2021-08-09 14:25:25.314317

"""
from alembic import op
import sqlalchemy as sa
import main.utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '086a428f2f85'
down_revision = '5453c962223e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_instance_registration_invites', sa.Column('extra_question_answers', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team_instance_registration_invites', 'extra_question_answers')
    # ### end Alembic commands ###
