import os
from os.path import join
from pydantic_settings import BaseSettings

BASE_DIR = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(BASE_DIR))
ENV_DIR = join(project_dir, '.env')


class DirConfigs(BaseSettings):
    ROOT_DIR: str = os.path.dirname(os.path.dirname(BASE_DIR))
    SRC_DIR: str = os.path.dirname(BASE_DIR)
    INPUT_FILE: str = join(SRC_DIR, 'accrual_report')
    OUTPUT_FILE: str = join(SRC_DIR, 'accrual_report.csv')


class Config(BaseSettings):
    DIR_CONFIG: DirConfigs = DirConfigs()


configs = Config()
