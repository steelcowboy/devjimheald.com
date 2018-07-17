from django.shortcuts import redirect, HttpResponse
from . import secret

from ipware import get_client_ip
import ipaddress


INT_NET = ipaddress.IPv6Network(secret.NET) 

INT_SEARCH_URL = secret.SEARCH
ALT_URL = secret.ALT 


def search(request):
    params = request.GET.get('q')
    cip, is_routable = get_client_ip(request)
    
    client_ip = ipaddress.ip_address(cip)

    # My internal network will certainly be IPv6, so this isn't it
    if type(client_ip) == ipaddress.IPv4Address:
        return redirect(f"{ALT_URL}{params}")
    else:
        if client_ip in FB_IP:
            return redirect(f"{INT_SEARCH_URL}{params}")
        else:
            return redirect(f"{ALT_URL}{params}")
