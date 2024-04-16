import os
import sys
from subprocess import run
import argparse
import datetime


SAMPLE_DIRECTORY = os.path.join(
    os.path.dirname(__file__),
    '..',
    'sample-tests'
)


def run_pytest(debug=False):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--directory',
        help='test を含むディレクトリ',
        type=str
    )
    # parser.add_argument(
    #     "-c",
    #     "--csv-path",
    #     help="some optional argument",
    #     type=str
    # )

    args = parser.parse_args()

    if debug:
        directory = SAMPLE_DIRECTORY

    else:
        assert os.path.exists(args.directory)
        directory = args.directory

    result_path = os.path.join(directory, f'{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}-pytest-result.xml')

    # run pytest
    run([
        sys.executable,
        '-m',
        'pytest',
        f'--junit-xml={result_path}',  # [options]
        '--capture=no',
        directory,
    ])


def launch_pytest_dashboard():
    ...


# def _parse_junit():
#
#     result_path = os.path.join(SAMPLE_DIRECTORY, 'pytest-result.xml')
#
#
#     from junitparser import JUnitXml
#     # from lxml.etree import XMLParser, parse
#     #
#     # def parse_func(file_path):
#     #     xml_parser = XMLParser(huge_tree=True)
#     #     return parse(file_path, xml_parser)
#     #
#     # xml = JUnitXml.fromfile(result_path, parse_func)
#
#
#     xml = JUnitXml.fromfile(result_path)
#     # n_tests: int = xml.tests
#     # n_failures: int = xml.failures
#     # n_errors: int = xml.errors
#     # n_skipped: int = xml.skipped
#
#     for suite in xml:
#         # handle suites
#         print(suite)
#         for case in suite:
#             # handle cases
#             print(case)
#             # a:str = case.name
#             # a:bool = case.is_passed
#             # a:bool = case.is_skipped
#             # a:datetime.datetime = case.time
#
#     pass



if __name__ == '__main__':
    run_pytest(debug=True)
    # _parse_junit()