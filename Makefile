install:
	poetry install

install_poetry:
	curl -sSL https://install.python-poetry.org | python -
	poetry install

tests: install tests_only tests_pre_commit

tests_pre_commit:
	poetry run pre-commit run --all-files

run_tests: tests

tests_only:
	poetry run pytest --cov=./ --cov-report=xml --cov-report=html -vv

build_sync:
	poetry run unasync supabase_functions tests

rename_project: rename_package_dir rename_package

rename_package_dir:
	mv supabase_functions supafunc

rename_package:
	sed -i 's/supabase_functions/supafunc/g' pyproject.toml tests/_async/clients.py tests/_sync/clients.py tests/_async/test_function_client.py tests/_sync/test_function_client.py
