import os
from os.path import join

from pydantic_settings import BaseSettings

BASE_DIR = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(BASE_DIR))
ENV_DIR = join(project_dir, '.env')


class DirConfigs(BaseSettings):
    ROOT_DIR: str = os.path.dirname(os.path.dirname(BASE_DIR))
    SRC_DIR: str = os.path.dirname(BASE_DIR)
    FILES_DIR: str = join(SRC_DIR, 'Для тестового')
    RESULT_FILE_DIR: str = join(SRC_DIR, 'result')
    RESULT_TIF: str = join(RESULT_FILE_DIR, 'result.tiff')


class Config(BaseSettings):
    DIR_CONFIG: DirConfigs = DirConfigs()


configs = Config()
