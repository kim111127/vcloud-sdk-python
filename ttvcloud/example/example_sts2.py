# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.policy import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    statement = Statement.new_allow_statement(['iam:*'], [])
    inline_policy = Policy([statement])

    # 60 * 60(设定有效期一小时)
    resp = vod_service.sign_sts2(inline_policy, 60 * 60)
    print(resp)
