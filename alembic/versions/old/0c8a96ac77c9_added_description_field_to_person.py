"""Added description field to person

Revision ID: 0c8a96ac77c9
Revises: 5f0b8e0c784c
Create Date: 2024-04-30 00:02:56.024615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8a96ac77c9'
down_revision = '5f0b8e0c784c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_content_people', sa.Column('description_ua', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_content_people', 'description_ua')
    # ### end Alembic commands ###
