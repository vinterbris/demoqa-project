import pydantic_settings
from dotenv import load_dotenv

from demoqa_ui_tests.utils import path

WEB_URL = 'https://demoqa.com'


class Config(pydantic_settings.BaseSettings):
    base_url: str = WEB_URL
    window_width: int = 1900
    window_height: int = 1080
    timeout: float = 2.0

    selenoid: bool = False
    browser_version: str = '127.0'
    selenoid_url: str = 'http://localhost:4444'
    selenoid_ui_url: str = 'http://localhost:8080'


config = Config(_env_file=path.relative_from_root('.env'))
