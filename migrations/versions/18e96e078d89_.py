"""empty message

Revision ID: 18e96e078d89
Revises: 
Create Date: 2020-06-27 07:50:11.445797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18e96e078d89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('hex', sa.String(length=20), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('color_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('for_everyone', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('member_by_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('list_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('expiration_date', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('member_by_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attached_user',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('card_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(length=1000), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('card_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pinned_tag',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('card_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pinned_tag')
    op.drop_table('comment')
    op.drop_table('attached_user')
    op.drop_table('card')
    op.drop_table('tag')
    op.drop_table('list')
    op.drop_table('table')
    op.drop_table('user')
    op.drop_table('color')
    # ### end Alembic commands ###
