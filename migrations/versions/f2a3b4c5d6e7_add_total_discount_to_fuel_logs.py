"""add total discount to fuel_logs

Revision ID: f2a3b4c5d6e7
Revises: d4e5f6a7b8c0
Create Date: 2026-08-14
"""
from alembic import op
import sqlalchemy as sa


revision = 'f2a3b4c5d6e7'
down_revision = 'd4e5f6a7b8c0'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'fuel_logs' not in inspector.get_table_names():
        return
    existing_cols = [col['name'] for col in inspector.get_columns('fuel_logs')]
    if 'discount_total' not in existing_cols:
        with op.batch_alter_table('fuel_logs', schema=None) as batch_op:
            batch_op.add_column(sa.Column('discount_total', sa.Float(), nullable=True))


def downgrade():
    with op.batch_alter_table('fuel_logs', schema=None) as batch_op:
        batch_op.drop_column('discount_total')
