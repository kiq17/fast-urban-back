"""create users table

Revision ID: f7a8d01782c8
Revises: 
Create Date: 2023-06-07 19:37:10.839551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7a8d01782c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("nome", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("senha",sa.String, nullable=False),
        sa.Column("created_at",sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")),
        sa.Column("update_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
