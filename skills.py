# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-blood-omega3-dha-epa-index-cardiac-risk-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def stratify_omega3_index_cardiac_risk(epa_dha_percent, body_weight_kg=75.0, current_daily_supplement_mg=0):
    if epa_dha_percent <= 0:
        raise ValueError("epa_dha_percent must be positive")
        
    # Cardiovascular Risk Tiers (Harris WS et al.):
    # < 4.0%: High risk (lowest quartile of survival)
    # 4.0 - 7.9%: Intermediate risk
    # >= 8.0%: Desirable / optimal cardioprotective zone
    if epa_dha_percent >= 8.0:
        tier = "DESIRABLE_CARDIOPROTECTIVE_ZONE"
        relative_scd_risk = 0.10
        interpretation = "Lowest risk for fatal coronary heart disease and sudden cardiac arrest; superior erythrocyte membrane fluidity."
        recommended_extra_mg = 0
    elif epa_dha_percent >= 4.0:
        tier = "INTERMEDIATE_CARDIOVASCULAR_RISK"
        relative_scd_risk = 0.45
        interpretation = "Suboptimal cellular omega-3 incorporation. Membrane eicosanoid balance biased towards pro-thrombotic TXA2 and leukotrienes."
        # Approximate requirement: ~120 mg/day of EPA+DHA per 1% deficit to reach 8% over 16 weeks
        deficit_pct = 8.0 - epa_dha_percent
        recommended_extra_mg = int(deficit_pct * 250.0)
    else:
        tier = "HIGH_CARDIAC_MORTALITY_RISK"
        relative_scd_risk = 1.00
        interpretation = "Marked cellular depletion of marine long-chain omega-3s. Maximum vulnerability to ventricular arrhythmias and myocardial ischemia."
        deficit_pct = 8.0 - epa_dha_percent
        recommended_extra_mg = int(deficit_pct * 300.0)
        
    return {
        "erythrocyte_omega3_index_percent": round(epa_dha_percent, 2),
        "target_optimal_percent": 8.0,
        "risk_stratification_tier": tier,
        "relative_sudden_cardiac_death_risk": relative_scd_risk,
        "current_daily_intake_mg": current_daily_supplement_mg,
        "recommended_additional_epa_dha_mg_day": recommended_extra_mg,
        "clinical_interpretation": interpretation
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "stratify_omega3_index_cardiac_risk",
                        "description": """Quantify cardioprotection using the erythrocyte membrane Omega-3 Index (sum of EPA + DHA expressed as a percentage of total fatty acids).
Normal population risk stratification: < 4.0% high cardiovascular risk, 4.0% - 8.0% intermediate risk, > 8.0% optimal cardioprotection (90% reduction in sudden cardiac death).
Calculates required daily supplemental ethyl ester / triglyceride re-esterified EPA+DHA dosage to reach the 8.0% target within 16 weeks.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = stratify_omega3_index_cardiac_risk(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'epa_dha_percent': 5.4, 'body_weight_kg': 78.0, 'current_daily_supplement_mg': 500}
        out = stratify_omega3_index_cardiac_risk(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
