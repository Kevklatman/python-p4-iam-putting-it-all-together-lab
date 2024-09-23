"""change model

Revision ID: 3d4a3f31c14f
Revises: 6cca2ea20de3
Create Date: 2024-09-22 19:13:21.258419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d4a3f31c14f'
down_revision = '6cca2ea20de3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_index('ix_recipes_user_id')
        batch_op.create_index(batch_op.f('ix_recipes_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipes_user_id'))
        batch_op.create_index('ix_recipes_user_id', ['user_id'], unique=False)

    # ### end Alembic commands ###
