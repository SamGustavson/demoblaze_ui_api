from os import environ

import pytest
from selenium.webdriver import ChromeOptions, DesiredCapabilities
from webdriver_setup import get_webdriver_for


@pytest.fixture(scope='session', autouse=True)
def session():
    return {}

@pytest.fixture(scope='session')
def driver(request):
    desired_caps = {}

    browser = {
        "build": "Demo Build",
        "name": "Test-Name",
        "platform": "MacOS Monterey",
        "browserName": "Chrome",
        "version": "104.0",
        "resolution": "1280x960"
    }

    desired_caps.update(browser)
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    tunnel_id = environ.get('TUNNEL', False)
    username = "senkevi44"
    access_key = "ZSZp4EKv4c49ttebpA8kwfTHeuez2B5HIJtrVp5MkNdlXCuG3O"


    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    caps = desired_caps


    # executor = RemoteConnection(selenium_endpoint)
    # browser = webdriver.Remote(
    #     command_executor=executor,
    #     desired_capabilities=caps
    # )

    chrome_options = ChromeOptions()
    chrome_options.add_argument("start-maximized")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True

    browser = get_webdriver_for("chrome",
                               desired_capabilities=capabilities,
                               options=chrome_options)
    yield browser

    def fin():
        # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        # if request.node.rep_call.failed:
        #     # browser.execute_script("lambda-status=failed")
        #     # browser.clear()
        #     browser.close()
        # else:
        #     # browser.execute_script("lambda-status=passed")
        browser.quit()

    request.addfinalizer(fin)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
