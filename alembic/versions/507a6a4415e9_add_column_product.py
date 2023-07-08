"""add column product

Revision ID: 507a6a4415e9
Revises: 1786547e3392
Create Date: 2023-07-08 16:05:31.829244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '507a6a4415e9'
down_revision = '1786547e3392'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("products",
        sa.Column("categoria", sa.String)    
    )
    pass


def downgrade() -> None:
    op.drop_column("products", "categoria")
    pass
