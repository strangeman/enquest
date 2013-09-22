from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def scenario(request):
    return render_to_response('scenario.tmpl')

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def links(request):
    return render_to_response('links.tmpl')

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def gameplay(request):
    return render_to_response('gameplay.tmpl')