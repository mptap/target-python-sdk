# Copyright 2020 Adobe. All rights reserved.
# This file is licensed to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

"""Event Provider"""

def target_event(event_type, payload=None):
    """Creates Target event
    :param event_type: (str) Event type, required
    payload: (dict) Payload, optional
    """
    result = {}
    if not payload:
        payload = {}
    result.event_type = event_type
    for key in payload.keys():
        result.key = payload.get(key)
    return result

class EventProvider:
    """EventProvider"""

    def __init__(self, events=None):
        """
        :param events: (dict.<str, callable>) An object with event name keys and callback
            function values, optional
        """
        if not events:
            events = {}
        self.subscriptions = {}
        self.subscription_count = 0
        for event_name in events.keys():
            self.subscribe(event_name, events.get(event_name))

    def subscribe(self, event_name, callback_func):
        """Subscribe to events
        :param event_name: (str) Event name, required
        callback_func: (callable) Callback function, required
        :return: (str)
        """
        self.subscription_count += 1
        if not self.subscriptions.get(event_name):
            self.subscriptions[event_name] = {}

        self.subscriptions[event_name][self.subscription_count] = callback_func
        return "{}:{}".format(event_name, self.subscription_count)

    def unsubscribe(self, event_id):
        """Unsubscribe from events
        :param event_id: (str) Event Id, required
        """
        event_name, event_id = event_id.split(":")
        if self.subscriptions.get(event_name):
            self.subscriptions[event_name][event_id]=None

    def emit(self, event_name, payload=None):
        """Emits events
        :param event_name: (str) Event name, required
        payload: (dict) Payload, optional
        """
        if not payload:
            payload = {}
        subscribed = self.subscriptions.get(event_name) or []
        for subscriber in subscribed:
            subscriber(target_event(event_name, payload))
