# flake8: noqa
import os
from pathlib import Path

from utils.enviroment import get_env_variable, parse_comma_sep_str_to_list

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-%%@2(a0*l1fvi6d!mcc^)t4(qoqq!bcvjkys&xqp%p&bfrshxw'  # noqa: E501

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('ALLOWED_HOST')
)
CSRF_TRUSTED_ORIGINS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('CSRF_TRUSTED_ORIGINS')
)
