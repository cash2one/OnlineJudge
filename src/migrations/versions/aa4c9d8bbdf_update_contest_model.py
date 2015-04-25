"""update contest model

Revision ID: aa4c9d8bbdf
Revises: 532a3998fa9f
Create Date: 2015-04-19 13:46:43.182327

"""

# revision identifiers, used by Alembic.
revision = 'aa4c9d8bbdf'
down_revision = '532a3998fa9f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contest_user', 'login_name')
    op.drop_column('contest_user', 'password_hash')
    op.drop_index('ix_solution_contest_user_id', table_name='solution')
    op.drop_column('solution', 'contest_user_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution', sa.Column('contest_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_solution_contest_user_id', 'solution', ['contest_user_id'], unique=False)
    op.add_column('contest_user', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.add_column('contest_user', sa.Column('login_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    ### end Alembic commands ###