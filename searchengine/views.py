from django.shortcuts import redirect, HttpResponse
from . import secret

from ipware import get_client_ip
import ipaddress


INT_NET = ipaddress.IPv6Network(secret.NET) 
INT_NET4 = ipaddress.IPv4Network(secret.NET_IPV4)

INT_SEARCH_URL = secret.SEARCH
ALT_URL = secret.ALT 


def search(request):
    params = request.GET.get('q')
    cip, is_routable = get_client_ip(request)
    
    client_ip = ipaddress.ip_address(cip)

    if client_ip in INT_NET4 or client_ip in INT_NET:
        return redirect(f"{INT_SEARCH_URL}{params}")
    else:
        return redirect(f"{ALT_URL}{params}")
