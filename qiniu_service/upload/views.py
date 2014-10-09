from django.http import HttpResponse
from django import forms
from urlparse import urljoin
import json
import qiniu.conf
import qiniu.io
import qiniu.rs

class Qiniu_Setting(object):
    qiniu.conf.ACCESS_KEY = '0V3pdbcLhNOuUTs71Q-ynVTx3CM8DJZ0Va5Y9BiF'
    qiniu.conf.SECRET_KEY = 'RNB_fJHHlIEPT1W1gHarFf22VDBNj5qeo-34SS5N'
    scope = 'jiaoyin-picture'
    policy = qiniu.rs.PutPolicy(scope)
    uptoken = policy.token()

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='lb')

def upload(data, dsc_key):
    ret, err = qiniu.io.put(Qiniu_Setting.uptoken, dsc_key, data)
    if err is not None:
        print err
        return None
    rep_link = 'http://jiaoyin-picture.qiniudn.com/'
    return urljoin(rep_link, ret['key'])

def upload_view(request):
    if request.method == 'POST':
        file_obj = request.FILES['file']
        pictureLink = upload(file_obj.read(), file_obj.name)
        resp =  HttpResponse(json.dumps({'key': pictureLink, 'ret_code':0}), content_type='text/plain')#'application/json')

        return resp
    return HttpResponse('nothing to upload', content_type='text/plain')

