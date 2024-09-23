"""change model again

Revision ID: d21197c97241
Revises: 3d4a3f31c14f
Create Date: 2024-09-22 19:14:22.786824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21197c97241'
down_revision = '3d4a3f31c14f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               nullable=False)
        batch_op.drop_index('ix_recipes_user_id')
        batch_op.create_index(batch_op.f('ix_recipes_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipes_user_id'))
        batch_op.create_index('ix_recipes_user_id', ['user_id'], unique=False)
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
