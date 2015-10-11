"""create streamer table

Revision ID: 4381fcb0cffe
Revises: 390b99746d52
Create Date: 2015-10-11 17:27:21.481137

"""

# revision identifiers, used by Alembic.
revision = '4381fcb0cffe'
down_revision = '390b99746d52'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('streamer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('cover', sa.Text(), nullable=True),
    sa.Column('channel', sa.String(length=64), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_streamer_user_id'), 'streamer', ['user_id'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_streamer_user_id'), table_name='streamer')
    op.drop_table('streamer')
    ### end Alembic commands ###
