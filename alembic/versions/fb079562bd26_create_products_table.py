"""create products table

Revision ID: fb079562bd26
Revises: f7a8d01782c8
Create Date: 2023-06-07 19:57:05.145079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb079562bd26'
down_revision = 'f7a8d01782c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("products", 
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("nome", sa.String, nullable=False),
        sa.Column("preco", sa.Float, nullable=False),
        sa.Column("quantidade", sa.Integer, nullable=False),
        sa.Column("a_venda", sa.Boolean, server_default="TRUE"),
        sa.Column("image_url", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")),
        sa.Column("update_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))                
    )
    pass


def downgrade() -> None:
    op.drop_table("products")
    pass
