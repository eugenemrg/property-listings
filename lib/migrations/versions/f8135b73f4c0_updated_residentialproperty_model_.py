"""Updated ResidentialProperty model removed price_per_sqf column

Revision ID: f8135b73f4c0
Revises: a47e8199cfe0
Create Date: 2023-09-06 16:43:37.128850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8135b73f4c0'
down_revision: Union[str, None] = 'a47e8199cfe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('residential_properties', 'price_per_sqf')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('residential_properties', sa.Column('price_per_sqf', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
