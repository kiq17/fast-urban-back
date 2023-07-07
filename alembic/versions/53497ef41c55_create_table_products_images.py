"""create table products images

Revision ID: 53497ef41c55
Revises: 30791ebf57f2
Create Date: 2023-07-07 12:05:47.892504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53497ef41c55'
down_revision = '30791ebf57f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("products_images",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("image_url", sa.String, nullable=False),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))
    )
    pass


def downgrade() -> None:
    op.drop_table("products_images")
    pass
