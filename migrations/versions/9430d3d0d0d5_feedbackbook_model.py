"""FeedbackBook model

Revision ID: 9430d3d0d0d5
Revises: 5768de65b1c4
Create Date: 2019-04-23 13:44:06.099553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9430d3d0d0d5'
down_revision = '5768de65b1c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book_feedback', sa.Column('created', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book_feedback', 'created')
    # ### end Alembic commands ###