#! -*- coding: utf-8 -*-


import os
import glob

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

    def del_user_data(self):
        data_files = glob.glob(os.path.join(self.channel_handler.ucache_path, '*.json'))
        if len(data_files) < 5:
            return
        for f_path in sorted(data_files, reverse=True)[5:]:
            File.force_delete(f_path)

    def set_user_data(self, event):
        return_code = 1314

        event_data = event.get_event_data()
        user_data = UserData.from_json(event_data)
        if not user_data.is_valid():
            logger.info('{0} got invalid user data: {1}'.format(self.real_name, event))
            return_code = 1313
            return return_code
        event_timestamp = event.get_event_timestamp()
        udata_path = settings.DEFAULT_USERDATA_PATH
        udata_name = os.path.basename(udata_path)
        ufile_name = '{0}_{1}'.format(event_timestamp, udata_name)
        ufile_path = os.path.join(self.channel_handler.ucache_path, ufile_name)
        File.write_content(event_data, ufile_path)

        self.del_user_data()

        data_files = glob.glob(os.path.join(self.channel_handler.ucache_path, '*.json'))
        sort_files = sorted(data_files, reverse=True)
        if not sort_files:
            return_code = 1313
            return return_code
        File.force_copy(sort_files[0], udata_path)

        return return_code

    def handle(self, event):
        logger.info('{0} handle event: {1}'.format(self.real_name, event))
        event_data = event.get_event_data()
        return_code = self.set_user_data(event)
        logger.debug('{0} update user data: {1}'.format(self.real_name, event_data))

        return return_code








