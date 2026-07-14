#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

# pytest and pytest-json-ctrf are baked into the environment image;
# nothing is installed here at verify time.
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
exit_code=$?

if [ "$exit_code" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit 0