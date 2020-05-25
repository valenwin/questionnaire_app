"""empty message

Revision ID: 4e10ec8dc24f
Revises: f46d40f29750
Create Date: 2020-05-25 18:27:36.715222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e10ec8dc24f'
down_revision = 'f46d40f29750'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'answer', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.drop_column('answer', 'user_id')
    # ### end Alembic commands ###
