# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from api_app.models import Key_word
from .u_api import youtube_search


@shared_task
def search_and_update():
    if Key_word.objects.values_list():
        for id in Key_word.objects.values_list():
            t = Key_word.objects.get(id=id[0])
            search_result = youtube_search(t.key_word,t.create_time)
            if search_result:
                if t.videos == None:
                    t.videos = ", ".join(search_result)
                    t.save()
                else:
                    for result in search_result:
                        if result not in t.videos:
                            t.videos += f", {result}"
                            t.save()
    else:
        pass
