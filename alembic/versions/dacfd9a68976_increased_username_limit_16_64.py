"""Increased username limit 16 -> 64

Revision ID: dacfd9a68976
Revises: 36b994f3335a
Create Date: 2023-11-18 01:12:36.703575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dacfd9a68976'
down_revision = '36b994f3335a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('service_users', 'username',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('service_users', 'username',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=16),
               nullable=True)
    # ### end Alembic commands ###
