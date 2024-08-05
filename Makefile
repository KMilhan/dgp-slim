lint:
	poetry shell
	black dgp
	ruff check . --fix --unsafe-fixes  # to enable re-wrapping comments and docstring
	mypy dgp
lint-check:
	poetry shell
	set -eu
	black --check dgp
	ruff check dgp
	mypy dgp

test:
	poetry shell
	pytest tests --cov-fail-under=80 --cov=aidata/ --cov-report=term-missing --cov-branch

compile-proto:
	poetry run python -m grpc_tools.protoc -I . --python_out . --mypy_out=.  ./dgp/proto/*.proto
