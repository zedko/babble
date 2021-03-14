"""Constrains added

Revision ID: df77b5f096b8
Revises: 274784499962
Create Date: 2021-03-15 00:57:42.817503

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'df77b5f096b8'
down_revision = '274784499962'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message', 'importance',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('message', 'message',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('message', 'source',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('message', 'user_uuid',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.drop_constraint('user_slack_id_key', 'user', type_='unique')
    op.drop_constraint('user_telegram_id_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_telegram_id_key', 'user', ['telegram_id'])
    op.create_unique_constraint('user_slack_id_key', 'user', ['slack_id'])
    op.alter_column('message', 'user_uuid',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('message', 'source',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('message', 'message',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('message', 'importance',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
