"""empty message

Revision ID: 048e8f93dcf6
Revises: 0e47fbfa2023
Create Date: 2021-06-28 17:47:58.819768

"""
from alembic import op
import sqlalchemy as sa
import lib


# revision identifiers, used by Alembic.
revision = '048e8f93dcf6'
down_revision = '0e47fbfa2023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spng_survey_questions', sa.Column('exclude_non_set_answer_text_mapping_keys', sa.Boolean(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spng_survey_questions', 'exclude_non_set_answer_text_mapping_keys')
    # ### end Alembic commands ###