""" The link to the project:
https://hub.labs.coursera.org/connect/sharedweipwpyi?forceRefresh=false&path=%2Fnotebooks
%2FC1M6L1_Putting_It_All_Together.ipynb&isLabVersioning=file-prep
"""


def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.event_type == "login":
            machines[event.machine].add(event.user)
        elif event.event_type == "logout":
            machines[event.machine].discard(event.user)  # use discard to avoid KeyError
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if users:
            user_list = ", ".join(users)
            print(f"{machine}: {user_list}")


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.event_type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)
generate_report(users)
