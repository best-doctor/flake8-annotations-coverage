import ast
from typing import Generator, Tuple

from flake8_annotations_coverage.ast_helpers import has_type_annotations
from flake8_annotations_coverage import __version__ as version


class AnnotationsCoverageChecker:
    name = 'flake8-annotations-coverage'
    version = version
    default_min_coverage_percents = 75
    min_coverage_percents = None

    _error_message = 'TAE001 too few type annotations ({}%)'

    def __init__(self, tree, filename: str):
        self.filename = filename
        self.tree = tree

    @classmethod
    def add_options(cls, parser) -> None:
        parser.add_option(
            '--min-coverage-percents',
            type=int,
            parse_from_config=True,
            default=cls.default_min_coverage_percents,
        )

    @classmethod
    def parse_options(cls, options) -> None:
        cls.min_coverage_percents = int(options.min_coverage_percents)

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        func_defs = [f for f in ast.walk(self.tree) if isinstance(f, ast.FunctionDef)]
        defs_annotations_info = [has_type_annotations(f) for f in func_defs]
        if not defs_annotations_info:
            return
        annotations_coverage = int(
            len(list(filter(None, defs_annotations_info)))
            / len(defs_annotations_info)
            * 100,
        )
        if self.min_coverage_percents and annotations_coverage < self.min_coverage_percents:
            yield 0, 0, self._error_message.format(annotations_coverage), type(self)
