import json
import logging

import allure
import curlify
import requests
from allure_commons.types import AttachmentType

import project
from demoqa_tests.plugins.allure.report import step


def send_request(url, method, **kwargs):
    if method == 'get':
        with step(f'GET {url}'):
            response = requests.get(project.config.base_url + url, **kwargs)
            log(response)
    elif method == 'post':
        with step(f'POST {url}'):
            response = requests.post(project.config.base_url + url, **kwargs)
            log(response)
    elif method == 'delete':
        with step(f'DELETE {url}'):
            response = requests.delete(project.config.base_url + url, **kwargs)
            log(response)
    elif method == 'put':
        with step(f'PUT {url}'):
            response = requests.put(project.config.base_url + url, **kwargs)
            log(response)
    elif method == 'patch':
        with step(f'PATCH {url}'):
            response = requests.patch(project.config.base_url + url, **kwargs)
            log(response)
    return response


def log(response):
    curl = curlify.to_curl(response.request)
    logging.basicConfig(level=logging.INFO)
    logging.info(curl) # I don't get why it doesn't work
    print(curl)
    allure.attach(
        body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt'
    )
    allure.attach(
        body=response.request.method + " " + response.request.url,
        name="Request",
        attachment_type=AttachmentType.TEXT,
        extension="txt",
    )
    if response.text:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
