
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
     driver=webdriver.Chrome()
     print("lunching chrome browser")
    elif browser == 'edge':
        driver=webdriver.Edge()
        print("lunching edge browser")
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#### pytest html report ######

# it is hook for addinf env info to html report
def pytest_configure(config):
    env=config.stash.setdefault(metadata_key, {})
    env["Project Name"] = "nop commerce"
    env["Module Name"] = "Customers"
    env["Tester"] = "Shahnaz"

    # config.metadata['Project Name']= 'nop commerce'
    # config.metadata['Module Name']= 'Customers'
    # config.metadata['Tester']= 'Shahnaz'

# it is hook for delete/modify env info to html report
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)