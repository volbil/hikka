"""Added history table

Revision ID: fd7ed0458b44
Revises: f7bcaacbff28
Create Date: 2024-02-07 23:23:16.929701

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fd7ed0458b44'
down_revision = 'f7bcaacbff28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_user_history',
    sa.Column('history_type', sa.String(length=64), nullable=False),
    sa.Column('target_id', sa.Uuid(), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=True),
    sa.Column('used_logs', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['service_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_user_history_history_type'), 'service_user_history', ['history_type'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_service_user_history_history_type'), table_name='service_user_history')
    op.drop_table('service_user_history')
    # ### end Alembic commands ###