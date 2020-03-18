"""Create Notes Table

Revision ID: 5681c714ae4f
Revises:
Create Date: 2020-03-18 11:13:03.835772

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '5681c714ae4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50)),
        sa.Column("description", sa.String(50)),
        sa.Column("created_at", sa.DateTime, default=func.now(), nullable=False),
    )


def downgrade():
    op.drop_table("notes")
