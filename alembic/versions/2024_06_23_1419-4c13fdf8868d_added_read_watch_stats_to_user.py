"""Added read/watch stats to user

Revision ID: 4c13fdf8868d
Revises: d1f7b083c01e
Create Date: 2024-06-23 14:19:45.161510

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4c13fdf8868d"
down_revision = "d1f7b083c01e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "service_users",
        sa.Column(
            "anime_stats",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default="{}",
            nullable=False,
        ),
    )
    op.add_column(
        "service_users",
        sa.Column(
            "manga_stats",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default="{}",
            nullable=False,
        ),
    )
    op.add_column(
        "service_users",
        sa.Column(
            "novel_stats",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default="{}",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("service_users", "novel_stats")
    op.drop_column("service_users", "manga_stats")
    op.drop_column("service_users", "anime_stats")
    # ### end Alembic commands ###
