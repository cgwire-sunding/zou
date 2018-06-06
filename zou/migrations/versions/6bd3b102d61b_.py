"""empty message

Revision ID: 6bd3b102d61b
Revises: 0c90834fadd2
Create Date: 2018-06-06 14:49:11.420104

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '6bd3b102d61b'
down_revision = '3d5c93bafb9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.Column('task_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['task_type_id'], ['task_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id', 'task_id', name='subscription_task_uc'),
    sa.UniqueConstraint('person_id', 'task_type_id', 'entity_id', name='subscription_entity_uc')
    )
    op.create_index(op.f('ix_subscription_entity_id'), 'subscription', ['entity_id'], unique=False)
    op.create_index(op.f('ix_subscription_person_id'), 'subscription', ['person_id'], unique=False)
    op.create_index(op.f('ix_subscription_task_id'), 'subscription', ['task_id'], unique=False)
    op.create_index(op.f('ix_subscription_task_type_id'), 'subscription', ['task_type_id'], unique=False)
    op.drop_index('fki_search_filter_project_id_fkey', table_name='search_filter')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('fki_search_filter_project_id_fkey', 'search_filter', ['project_id'], unique=False)
    op.drop_index(op.f('ix_subscription_task_type_id'), table_name='subscription')
    op.drop_index(op.f('ix_subscription_task_id'), table_name='subscription')
    op.drop_index(op.f('ix_subscription_person_id'), table_name='subscription')
    op.drop_index(op.f('ix_subscription_entity_id'), table_name='subscription')
    op.drop_table('subscription')
    # ### end Alembic commands ###
