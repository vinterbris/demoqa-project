import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demoqa.com'
    window_width: int = 1900
    window_height: int = 1080
    timeout: float = 2.0

    selenoid: bool = False
    browser_version: str = '127.0'
    selenoid_url: str = 'http://localhost:4444'
    selenoid_ui_url: str = 'http://localhost:8080'


config = Config(_env_file=dotenv.find_dotenv())

if __name__ == '__main__':
    """
    Run config.py to check config values on start. Used for debugging
    """
    print(config.__repr__())
