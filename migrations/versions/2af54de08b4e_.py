"""empty message

Revision ID: 2af54de08b4e
Revises: 
Create Date: 2023-08-15 14:45:11.374713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2af54de08b4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('isVisited', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('link', 'isVisited')
    # ### end Alembic commands ###
