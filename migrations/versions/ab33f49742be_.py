"""empty message

Revision ID: ab33f49742be
Revises: 05ff6b8545d7
Create Date: 2024-12-09 23:06:09.159269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab33f49742be'
down_revision = '05ff6b8545d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_last_name_key', type_='unique')
        batch_op.drop_constraint('user_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_name_key', ['name'])
        batch_op.create_unique_constraint('user_last_name_key', ['last_name'])

    # ### end Alembic commands ###
