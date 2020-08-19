"""empty message

Revision ID: e68de889c2d2
Revises: d13367dc8ed1
Create Date: 2020-08-19 21:33:53.199644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68de889c2d2'
down_revision = 'd13367dc8ed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attachment', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attachment', 'active')
    # ### end Alembic commands ###
