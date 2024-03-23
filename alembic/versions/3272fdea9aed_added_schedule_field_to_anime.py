"""Added schedule field to anime

Revision ID: 3272fdea9aed
Revises: efab6f4f4ba9
Create Date: 2024-03-24 00:34:35.276039

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "3272fdea9aed"
down_revision = "efab6f4f4ba9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "service_content_anime",
        sa.Column(
            "schedule",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default="[]",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("service_content_anime", "schedule")
    # ### end Alembic commands ###
