import graphene
from graphene import resolve_only_args, with_context
from graphene.contrib.django import DjangoObjectType
from django.contrib.auth.models import AnonymousUser

from graphene.contrib.django.debug import DjangoDebugMiddleware, DjangoDebug
import models


class User(DjangoObjectType):
    class Meta:
        model = models.User
        only_fields = ('id', 'name', 'talks', 'avatar')

    def resolve_talks(self, args, info):
        return self.talks.all()


class Talk(DjangoObjectType):
    class Meta:
        model = models.Talk


class Query(graphene.ObjectType):
    me = graphene.Field(User)
    # debug = graphene.Field(DjangoDebug, name='__debug')

    @with_context
    def resolve_me(self, args, context, info):
        if isinstance(context.user, AnonymousUser):
            return None
        return context.user


schema = graphene.Schema(name='MySchema')

# schema = graphene.Schema(name='MySchema', middlewares=[DjangoDebugMiddleware()])

schema.register(Talk)

schema.query = Query
