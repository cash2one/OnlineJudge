"""empty message

Revision ID: 4c943b7423d3
Revises: 292cf7b6f13e
Create Date: 2015-03-22 11:34:32.586429

"""

# revision identifiers, used by Alembic.
revision = '4c943b7423d3'
down_revision = '292cf7b6f13e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem', sa.Column('is_special_judge', sa.Boolean(), server_default=sa.text(u'false'), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('problem', 'is_special_judge')
    ### end Alembic commands ###
