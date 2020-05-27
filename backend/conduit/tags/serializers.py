# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump
import sys
from conduit.profile.serializers import ProfileSchema

class TagSchema(Schema):
    tagname = fields.Str()
    description = fields.Str()
    slug = fields.Str()
    icon = fields.Str()
    modSetting = fields.Int()
    tag = fields.Nested('self', exclude=('tag',), default=True, load_only=True)
    tagFollowers = fields.List(fields.Nested("ProfileSchema"))
    moderators = fields.List(fields.Nested("ProfileSchema"))

    @pre_load
    def make_Tag(self, data, **kwargs):
        return data['tag']

    @post_dump
    def dump_Tag(self, data, **kwargs):
        return {'tag': data}

class TagsSchema(TagSchema):

    @post_dump
    def dump_Tag(self, data, **kwargs):
        return data

    @post_dump(pass_many=True)
    def dump_Tags(self, data, many, **kwargs):
        return {'tags': data}

tag_schema = TagSchema()
tags_schemas = TagsSchema(many=True)
