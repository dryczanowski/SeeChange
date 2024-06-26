"""world_coordinates_header

Revision ID: a9c1d480a229
Revises: 887c36dbb427
Create Date: 2023-10-31 20:41:45.343665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c1d480a229'
down_revision = '887c36dbb427'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('world_coordinates', sa.Column('header_excerpt', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('world_coordinates', 'header_excerpt')
    # ### end Alembic commands ###
