"""Add Fruits initial database schema

Revision ID: 4c3d13cab9c4
Revises: 
Create Date: 2024-06-24 08:24:19.637125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c3d13cab9c4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fruits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('flavor_variation', sa.Enum('CITRIC', 'SWEET', 'SOUR', 'BITTER', 'TANGY', name='flavorvariation'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fruits_id'), 'fruits', ['id'], unique=False)
    op.create_index(op.f('ix_fruits_name'), 'fruits', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fruits_name'), table_name='fruits')
    op.drop_index(op.f('ix_fruits_id'), table_name='fruits')
    op.drop_table('fruits')
    # ### end Alembic commands ###
