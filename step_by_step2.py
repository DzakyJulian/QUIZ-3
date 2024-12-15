def format_integration_steps(rule):
    """
    Format integration steps for better readability.
    Args:
        rule: Integration rule (a dictionary or similar structure).
    Returns:
        A formatted string representing the integration steps.
    """
    if isinstance(rule, dict):
        integrand = rule.get("integrand", "Unknown")
        variable = rule.get("variable", "Unknown")
        substeps = rule.get("substeps", [])
        
        if "constant" in rule and "other" in rule:
            # Handle ConstantTimesRule
            return f"Integrate {rule['constant']} * {rule['other']} with respect to {variable}:\n  " \
                   f"{format_integration_steps(rule['substep'])}"
        elif "base" in rule and "exp" in rule:
            # Handle PowerRule
            return f"Apply power rule to {rule['base']}^{rule['exp']}:\n  " \
                   f"Result: {rule['base']}^{rule['exp'] + 1}/{rule['exp'] + 1}"
        elif "integrand" in rule and not substeps:
            # Handle ConstantRule or base cases
            return f"Integrate constant {integrand} with respect to {variable}:\n  Result: {integrand}*{variable}"
        elif substeps:
            # Handle general cases
            formatted_substeps = "\n  ".join(format_integration_steps(step) for step in substeps)
            return f"Integrate {integrand} with respect to {variable}:\n  {formatted_substeps}"
    return str(rule)

# Example input
rule = {
    "integrand": "3*x**2 + 2*x + 1",
    "variable": "x",
    "substeps": [
        {
            "integrand": "3*x**2",
            "variable": "x",
            "constant": 3,
            "other": "x**2",
            "substep": {
                "integrand": "x**2",
                "variable": "x",
                "base": "x",
                "exp": 2,
            }
        },
        {
            "integrand": "2*x",
            "variable": "x",
            "constant": 2,
            "other": "x",
            "substep": {
                "integrand": "x",
                "variable": "x",
                "base": "x",
                "exp": 1,
            }
        },
        {
            "integrand": "1",
            "variable": "x",
        }
    ]
}

# Formatting the example rule
print(format_integration_steps(rule))
