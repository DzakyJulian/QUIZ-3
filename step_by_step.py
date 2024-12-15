import sympy
from sympy import symbols, integrate
from sympy.integrals.manualintegrate import (
    integral_steps,
    parts_rule,
    add_rule,
    mul_rule,
    constant_rule,
    power_rule,
    exp_rule,
    trig_rule,
)

x = symbols('x')

def steps_explanation(step, level=0):
    """
    Penjelasan Langkah2 Integrasi secara Rekursif
    """
    # Inisialisasi variabel penjelasan
    explanation = ""

    """
    Generate explanations for integration steps.
    """
    if hasattr(step, "u") and hasattr(step, "dv"):  # PartsRule
        explanation = (
            f"Integration by Parts:\n"
            f"  u = {step.u}, dv = {step.dv}\n"
            f"  du = {step.u.diff(x)}, v = {integrate(step.dv, x)}\n"
        )
        explanation += steps_explanation(step.u_times_v)
        explanation += steps_explanation(step.remaining_integral)
        return explanation

    if hasattr(step, "substeps"):  # AddRule
        explanation = "Sum Rule:\n"
        for substep in step.substeps:
            explanation += steps_explanation(substep)
        return explanation

    if hasattr(step, "substep"):  # MulRule
        return steps_explanation(step.substep)

    if hasattr(step, "n"):  # PowerRule
        return f"Power Rule: x**{step.n} becomes x**({step.n + 1}) / ({step.n + 1})\n"

    if hasattr(step, "constant"):  # ConstantRule
        return f"Constant Rule: Move constant {step.constant} out of the integral.\n"

    if hasattr(step, "k"):  # ExpRule
        return f"Exponential Rule: exp({step.k} * x) becomes exp({step.k} * x) / {step.k}\n"

    return f"Unhandled step type: {type(step)}\n"