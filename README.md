# genpark-personal-agent-blood-omega3-dha-epa-index-cardiac-risk-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Erythrocyte membrane Omega-3 Index (EPA+DHA %), target > 8.0%, sudden cardiac death relative risk stratifier.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `stratify_omega3_index_cardiac_risk`
- **Category**: `personal_agent`

### Method Documentation
Quantify cardioprotection using the erythrocyte membrane Omega-3 Index (sum of EPA + DHA expressed as a percentage of total fatty acids).
Normal population risk stratification: < 4.0% high cardiovascular risk, 4.0% - 8.0% intermediate risk, > 8.0% optimal cardioprotection (90% reduction in sudden cardiac death).
Calculates required daily supplemental ethyl ester / triglyceride re-esterified EPA+DHA dosage to reach the 8.0% target within 16 weeks.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "stratify_omega3_index_cardiac_risk",
    "arguments": {
    "epa_dha_percent": 5.4,
    "body_weight_kg": 78.0,
    "current_daily_supplement_mg": 500
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
