from django.http import HttpResponse
from django import forms
from urlparse import urljoin
import json
import qiniu.conf
import qiniu.io
import qiniu.rs

class Qiniu_Setting(object):
    qiniu.conf.ACCESS_KEY = 'a5AuPB06Xs5dhS3zwl0wMLfXzp22n3dKm0u7gslf'
    qiniu.conf.SECRET_KEY = 'bbzvKSfRAmjWmovkXAXVvnFY3cEe549WBaMZOf1k'
    scope = 'laofei-test'
    policy = qiniu.rs.PutPolicy(scope)
    uptoken = policy.token()

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='lb')

def upload(data, dsc_key):
    ret, err = qiniu.io.put(Qiniu_Setting.uptoken, dsc_key, data)
    if err is not None:
        print err
        return None
    rep_link = 'http://laofei-test.qiniudn.com/dog.png'
    return urljoin(rep_link, ret['key'])

def upload_view(request):
    if request.method == 'POST':
        print request.POST
        print request.FILES
        file_obj = request.FILES['picfile']
        pictureLink = upload(file_obj.read(), file_obj.name)
        print pictureLink

        return HttpResponse(json.dumps({'pictureLink': pictureLink}), content_type='application/json')
    return HttpResponse('nothing to upload', content_type='text/plain')

