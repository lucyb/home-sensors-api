export DEFAULT_PYTHON := if os_family() == "unix" { "python3.11" } else { "python" }
export VIRTUAL_ENV  := env_var_or_default("VIRTUAL_ENV", ".venv")
export PIP := BIN + if os_family() == "unix" { "/python -m pip" } else { "/python.exe -m pip" }
export BIN := VIRTUAL_ENV + if os_family() == "unix" { "/bin" } else { "/Scripts" }

default:
    @"{{ just_executable() }}" --list

clean:
    rm -rf .venv

virtualenv:
    #!/usr/bin/env bash
    set -euo pipefail

    # allow users to specify python version in .env
    PYTHON_VERSION=${PYTHON_VERSION:-$DEFAULT_PYTHON}

    # create venv and upgrade pip
    test -d $VIRTUAL_ENV || { $PYTHON_VERSION -m venv $VIRTUAL_ENV && $PIP install --upgrade pip; }

    # ensure we have pip-tools so we can run pip-compile
    test -e $BIN/pip-compile || $PIP install pip-tools

# update requirements.prod.txt if requirements.prod.in has changed
requirements-prod *args:
    #!/usr/bin/env bash
    set -euo pipefail

    # exit if src file is older than dst file (-nt = 'newer than', but we negate with || to avoid error exit code)
    test "${FORCE:-}" = "true" -o requirements.prod.in -nt requirements.prod.txt || exit 0
    $BIN/pip-compile --allow-unsafe --generate-hashes --output-file=requirements.prod.txt requirements.prod.in {{ args }}

# update requirements.dev.txt if requirements.dev.in has changed
requirements-dev *args: requirements-prod
    #!/usr/bin/env bash
    set -euo pipefail

    # exit if src file is older than dst file (-nt = 'newer than', but we negate with || to avoid error exit code)
    test "${FORCE:-}" = "true" -o requirements.dev.in -nt requirements.dev.txt || exit 0
    $BIN/pip-compile --allow-unsafe --generate-hashes --output-file=requirements.dev.txt requirements.dev.in {{ args }}

prodenv *args: requirements-prod
    #!/usr/bin/env bash
    set -euo pipefail

    # exit if .txt file has not changed since we installed them
    test requirements.prod.txt -nt $VIRTUAL_ENV/.prod || exit 0

    $PIP install -r requirements.prod.txt
    touch $VIRTUAL_ENV/.prod

devenv *args: prodenv
    #!/usr/bin/env bash
    set -euo pipefail

    # exit if .txt file has not changed since we installed them
    test requirements.dev.txt -nt $VIRTUAL_ENV/.dev || exit 0

    $PIP install -r requirements.dev.txt
    touch $VIRTUAL_ENV/.dev

run: prodenv
    python api.py

test *args: devenv
    pytest {{ args }}