"""create orders table

Revision ID: 30791ebf57f2
Revises: fb079562bd26
Create Date: 2023-06-07 20:04:05.115052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30791ebf57f2'
down_revision = 'fb079562bd26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("orders",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))               
    )
    pass


def downgrade() -> None:
    op.drop_table("orders")
    pass
