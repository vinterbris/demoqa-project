import project

valid_credentials = {
    "userName": project.config.login,
    "password": project.config.password,
}
invalid_credentials = {"userName": project.config.login, "password": 'ps'}
