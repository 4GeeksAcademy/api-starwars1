"""initial

Revision ID: 0a5de42999e7
Revises: a5cffa318ac2
Create Date: 2025-07-17 00:11:10.450131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a5de42999e7'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('username', sa.String(length=80), nullable=False))
        batch_op.drop_column('is_active')
        batch_op.drop_column('email')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('password', sa.VARCHAR(length=80), nullable=False))
        batch_op.add_column(
            sa.Column('email', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(
            sa.Column('is_active', sa.BOOLEAN(), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
