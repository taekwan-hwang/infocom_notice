#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infocom_notice.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    if 'runserver' in sys.argv:  #서버를 돌리는 경우에만 실행
        import threading
        import time
        threading.Thread(target=execute_from_command_line, args=(sys.argv,)).start()
        time.sleep(5)  # wait for loading app
        from apscheduler.schedulers.background import BackgroundScheduler
        from main.scheduled_task import send_new_msg_to_kakao
        import logging	
        # 이동시 이 밑으로 다 옮기면 됨
        logging.basicConfig(filename='./test.log', level=logging.INFO)
        # apscheduler에서 일어나는 모든 정보는 warning이 아니면 무시
        logging.getLogger("apscheduler").setLevel(logging.WARNING)
        sched = BackgroundScheduler()
        # interval 형식으로 작동하며, 마다 실행
        # 30초마다 scheduled_task.py의 updatedata함수 호출
        # hours = 2 이면 2시간 마다 실행됨
        sched.add_job(send_new_msg_to_kakao, 'interval', seconds=30)
        sched.start()
    else:
        execute_from_command_line(sys.argv)

