"""empty message

Revision ID: b7e5c1c44467
Revises: fb3eb3f20f7d
Create Date: 2022-06-18 01:03:35.260814

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7e5c1c44467'
down_revision = 'fb3eb3f20f7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ad', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('haqq', sa.String(length=40), nullable=True),
    sa.Column('muddet', sa.String(length=20), nullable=True),
    sa.Column('image_url', sa.String(length=1000), nullable=True),
    sa.Column('qaliq', sa.String(length=40), nullable=True),
    sa.Column('valyuta', sa.String(length=40), nullable=True),
    sa.Column('kredit', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('ad'),
    sa.UniqueConstraint('id')
    )
    op.drop_index('id', table_name='cards')
    op.drop_table('cards')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ad', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=1000), nullable=True),
    sa.Column('haqq', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('muddet', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=1000), nullable=True),
    sa.Column('qaliq', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('valyuta', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('kredit', mysql.VARCHAR(length=40), nullable=True),
    sa.PrimaryKeyConstraint('ad'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'cards', ['id'], unique=False)
    op.drop_table('card')
    # ### end Alembic commands ###