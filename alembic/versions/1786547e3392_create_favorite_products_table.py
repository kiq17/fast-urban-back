"""create favorite products table

Revision ID: 1786547e3392
Revises: 53497ef41c55
Create Date: 2023-07-07 15:26:51.180614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1786547e3392'
down_revision = '53497ef41c55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("favorite_products",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))               
    )
    pass


def downgrade() -> None:
    op.drop_table("favorite_products")
    pass
