"""empty message

Revision ID: cd804a24c20a
Revises: 4c66b757c121
Create Date: 2025-05-22 11:26:17.243957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd804a24c20a'
down_revision = '4c66b757c121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('login_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('password', sa.VARCHAR(length=20), nullable=True),
    sa.Column('unit_code', sa.VARCHAR(length=20), nullable=False),
    sa.Column('unit_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('deleted', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login_name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('article',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('author_id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('update_by', sa.VARCHAR(length=36), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('create_by', sa.VARCHAR(length=36), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
