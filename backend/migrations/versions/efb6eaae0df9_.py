"""empty message

Revision ID: efb6eaae0df9
Revises: 55b82bb0eb01
Create Date: 2020-05-28 22:46:30.009849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efb6eaae0df9'
down_revision = '55b82bb0eb01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmarker_assoc',
    sa.Column('bookmarker', sa.Integer(), nullable=True),
    sa.Column('bookmarked_article', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bookmarked_article'], ['article.id'], ),
    sa.ForeignKeyConstraint(['bookmarker'], ['userprofile.id'], )
    )
    op.create_table('tag_needReviewArticle_assoc',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('needReviewArticle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['needReviewArticle_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'needReviewArticle_id')
    )
    op.alter_column('users', 'isAdmin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'isAdmin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_table('tag_needReviewArticle_assoc')
    op.drop_table('bookmarker_assoc')
    # ### end Alembic commands ###
