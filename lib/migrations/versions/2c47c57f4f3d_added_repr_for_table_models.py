"""Added repr for table models

Revision ID: 2c47c57f4f3d
Revises: f8135b73f4c0
Create Date: 2023-09-07 14:03:28.646794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c47c57f4f3d'
down_revision: Union[str, None] = 'f8135b73f4c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
