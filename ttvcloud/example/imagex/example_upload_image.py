# coding:utf-8
from __future__ import print_function

from ttvcloud.imagex.ImageXService import ImageXService

if __name__ == '__main__':
    imagex_service = ImageXService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # imagex_service.set_ak('ak')
    # imagex_service.set_sk('sk')

    service_id = 'your service id'
    file_paths = ['file path 1', 'file path 2']
    keys = ['file name 1', 'file name 2']

    resp = imagex_service.upload_image(service_id, file_paths, keys)
    print(resp)
