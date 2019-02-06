import ast
import os

from flake8_annotations_coverage.annotations_coverage import AnnotationsCoverageChecker


def run_validator_for_test_file(filename, min_coverage=None):
    test_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_files',
        filename,
    )
    with open(test_file_path, 'r') as file_handler:
        raw_content = file_handler.read()
    tree = ast.parse(raw_content)
    if min_coverage:
        AnnotationsCoverageChecker.min_coverage_percents = min_coverage
    checker = AnnotationsCoverageChecker(tree=tree, filename=filename)

    return list(checker.run())
