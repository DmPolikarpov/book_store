"""first migration

Revision ID: 3ca1aded4ae0
Revises: 
Create Date: 2019-04-09 22:49:01.153451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ca1aded4ae0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book_feedback', 'book_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_role'), table_name='user')
    op.alter_column('book_feedback', 'book_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###