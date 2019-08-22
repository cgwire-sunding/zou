"""empty message

Revision ID: b45cb782bb9c
Revises: d8dcd5196d57
Create Date: 2019-08-21 16:49:56.479274

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'b45cb782bb9c'
down_revision = 'd8dcd5196d57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('schedule_item_entity_id_fkey', 'schedule_item', type_='foreignkey')
    op.create_foreign_key(None, 'schedule_item', 'entity', ['entity_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.create_foreign_key('schedule_item_entity_id_fkey', 'schedule_item', 'task_type', ['entity_id'], ['id'])
    # ### end Alembic commands ###
