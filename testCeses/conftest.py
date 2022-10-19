from  selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching Chrome browser................")
    elif browser=="firefox":
        driver= webdriver.Firefox
        print("Lauching Firefox browser..............")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ###############
# It is hook for Adding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name '] = 'Customers'
    config._metadata['Tester'] = 'Dikshant'

# If is hook for delete/modify Enviroment info to HTML Report
@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
