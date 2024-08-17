import pydantic_settings

WEB_URL = 'https://demoqa.com'


class Config(pydantic_settings.BaseSettings):
    base_url: str = WEB_URL
    window_width: int = 1600
    window_height: int = 900
    timeout: float = 2.0
