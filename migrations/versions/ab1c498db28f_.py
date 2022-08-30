"""empty message

Revision ID: ab1c498db28f
Revises: 202c36f452f8
Create Date: 2022-06-18 01:44:46.280619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab1c498db28f'
down_revision = '202c36f452f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('security_image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('security_image')
    # ### end Alembic commands ###
