"""Add Updated At To Notes

Revision ID: 65b795e35fdd
Revises: 5681c714ae4f
Create Date: 2020-03-18 14:24:21.483263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '65b795e35fdd'
down_revision = '5681c714ae4f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("notes", sa.Column("updated_at", sa.DateTime, onupdate=func.now()))


def downgrade():
    op.drop_column("notes", "updated_at")
