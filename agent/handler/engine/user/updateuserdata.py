#! -*- coding: utf-8 -*-


from agent import settings
from agent.common.enhance import File
from agent.common.logger import Logger
from agent.models.event.event_type import EventType
from agent.models.userdata.user_data import UserData
from agent.handler.engine.baseengine import BaseEngineHandler

logger = Logger.get_logger(__name__)


class UpdateUserDataEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.UPDATEUSERDATA

    def get_user_data(self, o, n):
        user_data = n

        new_host_id, old_host_id = map(lambda k: k.get_host_id(), (n, o))
        new_cluster_id, old_cluster_id = map(lambda k: k.get_cluster_id(), (n, o))
        new_hostgroup_id, old_hostgroup_id = map(lambda k: k.get_hostgroup_id(), (n, o))

        user_data.set_host_id(new_host_id and new_host_id or old_host_id)
        user_data.set_cluster_id(new_cluster_id and new_cluster_id or old_cluster_id)
        user_data.set_hostgroup_id(new_hostgroup_id and new_hostgroup_id or old_hostgroup_id)

        return user_data

    def set_user_data(self, event):
        event_data = event.get_event_data()
        udata_path = settings.DEFAULT_USERDATA_PATH

        new_user_data = UserData.from_json(event_data)
        old_user_data = self.channel_handler.userdata_dao.get_user_data()

        user_data = self.get_user_data(old_user_data, new_user_data)
        File.write_content(user_data.to_json(), udata_path)

    def handle(self, event):
        logger.info('{0} handle event: {1}'.format(self.real_name, event))
        event_data = event.get_event_data()
        self.set_user_data(event)
        logger.debug('{0} update user data: {1}'.format(self.real_name, event_data))








