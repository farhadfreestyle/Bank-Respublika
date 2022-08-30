"""empty message

Revision ID: 202c36f452f8
Revises: b7e5c1c44467
Create Date: 2022-06-18 01:04:52.867230

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '202c36f452f8'
down_revision = 'b7e5c1c44467'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('text', sa.String(length=200), nullable=True),
    sa.Column('bold', sa.String(length=200), nullable=True),
    sa.Column('alt', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('kampaniya')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kampaniya',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('image_url', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('text', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('bold', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('alt', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('campaign')
    # ### end Alembic commands ###
