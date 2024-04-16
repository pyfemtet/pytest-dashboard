import os
import datetime

from pytest import (
    Session,
    TestReport,
)


BR = '\n'
PATH = os.path.join(
    os.path.dirname(__file__),
    datetime.datetime.now().strftime('%Y%m%d-%H%M%S-report.txt'),
)
during_test = False


def pytest_collection_finish(session: Session):
    with open(PATH, 'w', encoding='utf-8', newline=BR) as f:
        f.write(f'[items]{BR}')
        f.writelines([f'{item.name}{BR}' for item in session.items])


def pytest_report_teststatus(report: TestReport, config):
    global during_test
    if during_test:
        with open(PATH, 'a', encoding='utf-8', newline=BR) as f:
            f.write(
                f'{report.when}{BR}'
                f'  {report.outcome}{BR}'
            )
    if report.when == 'teardown':
        during_test = False


def pytest_runtest_setup(item):
    global during_test
    during_test = True
    with open(PATH, 'a', encoding='utf-8', newline=BR) as f:
        f.write(f'[item]{BR}')
        f.write(
            f'name{BR}'
            f'  {item.name}{BR}'
        )


def pytest_runtest_teardown(item):
    # global during_test
    # during_test = False
    pass
