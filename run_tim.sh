#!/bin/bash

INPUT="$1"

cd /Users/agent-a/openclaw/tim_tools || exit 1

python3 - <<PY
from core.tim_runner import run
result = run("""$INPUT""")
print(result["response_text"])
PY
