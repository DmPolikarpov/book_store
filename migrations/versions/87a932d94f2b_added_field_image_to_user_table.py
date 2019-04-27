"""added field image to User table

Revision ID: 87a932d94f2b
Revises: 5768de65b1c4
Create Date: 2019-04-26 19:22:32.185584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87a932d94f2b'
down_revision = '5768de65b1c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image')
    # ### end Alembic commands ###