from configparser import ConfigParser as _ConfigParser
import os


class Config:
    """Get values from config"""

    __config_file = _ConfigParser()
    __config_file.read(os.path.join(os.path.dirname(__file__), 'config.ini'), encoding='utf-8-sig')

    token = __config_file.get("Bot", "token")

    http = __config_file.get("Server", "http")
    ws = __config_file.get("Server", "ws")
    host_name = __config_file.get("Server", "host_name")
    server_authkey = __config_file.get("Server", "server_authkey")

    avatars = __config_file.get("Paths", "avatars")
