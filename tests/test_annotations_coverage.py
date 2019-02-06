from conftest import run_validator_for_test_file


def test_always_ok_for_empty_file():
    errors = run_validator_for_test_file('empty.py')
    assert not errors
    errors = run_validator_for_test_file('empty.py', min_coverage=100)
    assert not errors


def test_ok_for_fully_annotated_file():
    errors = run_validator_for_test_file('fully_annotated.py', min_coverage=100)
    assert not errors


def test_ok_for_args_only_annotated_file():
    errors = run_validator_for_test_file('arg_only_annotated.py', min_coverage=50)
    assert not errors
    errors = run_validator_for_test_file('arg_only_annotated.py', min_coverage=100)
    assert len(errors) == 1


def test_ok_for_kwonly_annotated_file():
    errors = run_validator_for_test_file('kwonly_arg_annotated.py', min_coverage=50)
    assert not errors
    errors = run_validator_for_test_file('kwonly_arg_annotated.py', min_coverage=100)
    assert len(errors) == 1
