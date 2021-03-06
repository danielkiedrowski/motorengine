#!/usr/bin/env python
# -*- coding: utf-8 -*-

from motorengine.query.base import QueryOperator


class IContainsOperator(QueryOperator):
    '''
    Query operator used to return all documents which specified field contains a string equal to a passed value.

    It is not case sensitive.

    For more information on `$regex` go to https://docs.mongodb.org/manual/reference/operator/query/regex/

    Usage:

    .. testsetup:: icontains_query_operator

        from datetime import datetime

        import tornado.ioloop

        from motorengine import *

    .. testcode:: icontains_query_operator

        class User(Document):
            first_name = StringField()

        query = Q(first_name__icontains='NaR')

        query_result = query.to_query(User)

        print(query_result)

    The resulting query is:

    .. testoutput:: icontains_query_operator

        {'name': {'$regex': 'NaR', '$options': 'i'}}

    '''

    def to_query(self, field_name, value):
        return {
            field_name: {
                "$regex": r'%s' %value,
                "$options": 'i'
            }
        }
