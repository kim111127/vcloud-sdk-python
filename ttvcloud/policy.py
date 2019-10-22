# coding:utf-8
import json


class Policy(object):
    def __init__(self, statements):
        self.statements = statements


class Statement(object):
    def __init__(self):
        self.effect = ''
        self.action = []
        self.resource = []
        self.condition = ''

    @staticmethod
    def new_allow_statement(actions, resources):
        s = Statement()
        s.effect = "Allow"
        s.action = actions
        s.resource = resources
        return s

    @staticmethod
    def new_deny_statement(actions, resources):
        s = Statement()
        s.effect = "Deny"
        s.action = actions
        s.resource = resources
        return s


class SecurityToken2(object):
    def __init__(self):
        self.access_key_id = ''
        self.secret_access_key = ''
        self.session_token = ''
        self.expired_time = ''

    def __str__(self):
        return json.dumps({
            'AccessKeyId': self.access_key_id,
            'SecretAccessKey': self.secret_access_key,
            'SessionToken': self.session_token,
            'ExpiredTime': self.expired_time
        })


class InnerToken(object):
    def __init__(self):
        self.lt_access_key_id = ''
        self.signed_secret_access_key = ''
        self.expired_time = 0
        self.policy = ''

    def __str__(self):
        return json.dumps({
            'LTAccessKeyId': self.lt_access_key_id,
            'SignedSecretAccessKey': self.signed_secret_access_key,
            'ExpiredTime': self.expired_time
        })
