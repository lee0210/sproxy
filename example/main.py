import os
import django
import json
import socket

from sproxy.utils import read_request, write_request

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from data.models import Heartbeat

PORT = 20000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('',PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        data = read_request(conn)
        data = []
        for hb in Heartbeat.objects.all():
            data.append({
                'app_name': hb.app_name,
                'last_beat': hb.last_beat.isoformat(),
            })
        write_request(conn, json.dumps(data))

