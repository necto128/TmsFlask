"""empty message

Revision ID: 1f5dfeb13283
Revises: 
Create Date: 2023-07-28 17:59:10.858535

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1f5dfeb13283'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=100), nullable=False),
                    sa.Column('password', sa.String(length=16), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('idea',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('type', sa.String(length=100), nullable=False),
                    sa.Column('activity', sa.String(length=100), nullable=False),
                    sa.Column('accessibility', sa.Float(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('idea')
    op.drop_table('user')
    # ### end Alembic commands ###