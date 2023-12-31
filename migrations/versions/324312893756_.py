"""empty message

Revision ID: 324312893756
Revises: 7d5c203fdc6e
Create Date: 2023-08-15 15:34:19.778774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '324312893756'
down_revision = '7d5c203fdc6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('operatingSystem', sa.String(), nullable=True))
    op.add_column('link', sa.Column('device', sa.String(), nullable=True))
    op.drop_column('link', 'OperatingSystem')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('OperatingSystem', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('link', 'device')
    op.drop_column('link', 'operatingSystem')
    # ### end Alembic commands ###
