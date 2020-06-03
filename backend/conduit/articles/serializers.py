# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump

from conduit.profile.serializers import ProfileSchema


class TagSchema(Schema):
    tagname = fields.Str()


class ArticleSchema(Schema):
    slug = fields.Str()
    title = fields.Str()
    description = fields.Str()
    createdAt = fields.DateTime()
    body = fields.Str()
    updatedAt = fields.DateTime(dump_only=True)
    author = fields.Nested(ProfileSchema)

    # for the envelope
    article = fields.Nested('self', exclude=('article',), default=True, load_only=True)
    tagList = fields.List(fields.Str())
    favoritesCount = fields.Int(dump_only=True)
    favorited = fields.Bool(dump_only=True)

    @pre_load
    def make_article(self, data, **kwargs):
        return data['article']

    @post_dump
    def dump_article(self, data, **kwargs):
        data['author'] = data['author']['profile']
        return {'article': data}

    class Meta:
        strict = True


class OrgArticleSchema(Schema):
    org_slug = fields.Str()
    slug = fields.Str(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    createdAt = fields.DateTime()
    body = fields.Str()
    updatedAt = fields.DateTime(dump_only=True)
    author = fields.Nested(ProfileSchema)
    
    # for the envelope
    article = fields.Nested('self', exclude=('article',), default=True, load_only=True)
    tagList = fields.List(fields.Str())
    favoritesCount = fields.Int(dump_only=True)
    favorited = fields.Bool(dump_only=True)
    needsReview = fields.Bool()


    @pre_load
    def make_article(self, data, **kwargs):
        print(data)
        return data['article']

    @post_dump
    def dump_article(self, data, **kwargs):
        data['author'] = data['author']['profile']
        return {'article': data}

    class Meta:
        strict = True


class PublishOrgArticle(Schema):
    slug = fields.Str()
    org_slug = fields.Str()
    article = fields.Nested('self', exclude=('article',), default=True, load_only=True)
 
    @pre_load
    def make_article(self, data, **kwargs):
        print(data)
        return data['article']

    @post_dump
    def dump_article(self, data, **kwargs):
        data['slug'] = data['slug']
        return {'article': data}


class OrgArticlesSchema(OrgArticleSchema):
    
    @post_dump
    def dump_article(self, data, **kwargs):
        data['author'] = data['author']['profile']
        return data

    @post_dump(pass_many=True)
    def dump_articles(self, data, many, **kwargs):
        return {'articles': data, 'articlesCount': len(data)}


class ArticleSchemas(ArticleSchema):

    @post_dump
    def dump_article(self, data, **kwargs):
        data['author'] = data['author']['profile']
        return data

    @post_dump(pass_many=True)
    def dump_articles(self, data, many, **kwargs):
        return {'articles': data, 'articlesCount': len(data)}


class CommentSchema(Schema):
    createdAt = fields.DateTime()
    body = fields.Str()
    updatedAt = fields.DateTime(dump_only=True)
    author = fields.Nested(ProfileSchema)
    id = fields.Int()

    # for the envelope
    comment = fields.Nested('self', exclude=('comment',), default=True, load_only=True)

    @pre_load
    def make_comment(self, data, **kwargs):
        return data['comment']

    @post_dump
    def dump_comment(self, data, **kwargs):
        data['author'] = data['author']['profile']

        return {'comment': data}

    class Meta:
        strict = True


class CommentsSchema(CommentSchema):

    @post_dump
    def dump_comment(self, data, **kwargs):
        data['author'] = data['author']['profile']
        return data

    @post_dump(pass_many=True)
    def make_comment(self, data, many, **kwargs):
        return {'comments': data}


article_schema = ArticleSchema()
org_article_schema = OrgArticleSchema()
publish_org_article = PublishOrgArticle()
org_articles_schema = OrgArticlesSchema(many=True)
articles_schema = ArticleSchemas(many=True)
comment_schema = CommentSchema()
comments_schema = CommentsSchema(many=True)
