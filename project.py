from typing import Optional

import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demoqa.com'
    timeout: float = 2.0
    # browser_name: supported.BrowserName = 'chrome'
    headless: bool = False
    window_width: int = 1600
    window_height: int = 1000
    maximize_window: bool = False

    selenoid: bool = False
    browser_version: str = '127.0'
    selenoid_url: str = 'http://localhost:4444'
    selenoid_ui_url: str = 'http://localhost:8080'

    remote_url: Optional[str] = None
    remote_version: Optional[str] = None
    remote_platform: Optional[str] = None
    remote_enableVNC: bool = True
    remote_screenResolution: str = '1920x1080x24'
    remote_enableVideo: bool = True
    remote_enableLog: bool = True

    hold_browser_open: bool = False
    save_page_source_on_failure: bool = True


config = Config(_env_file=dotenv.find_dotenv())

if __name__ == '__main__':
    """
    Run python3 config.py to check config values on start. Used for debugging
    """
    print(config.__repr__())
