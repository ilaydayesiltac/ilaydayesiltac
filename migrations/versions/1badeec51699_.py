"""empty message

Revision ID: 1badeec51699
Revises: ff7723919d90
Create Date: 2023-08-16 10:09:43.245223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1badeec51699'
down_revision = 'ff7723919d90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('original_url', sa.String(), nullable=True))
    op.drop_column('link', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('link', 'original_url')
    # ### end Alembic commands ###
