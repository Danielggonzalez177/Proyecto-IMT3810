"""Interfaces to Stokes operators."""
from bempp.api.operators.boundary import common as _common


def single_layer(
    domain,
    range_,
    dual_to_range,
    parameters=None,
    assembler="default_nonlocal",
    device_interface=None,
    precision=None,
    opt_layer=None,
):
    """Assemble the Stokes single-layer boundary operator."""
    return _common.create_operator(
        "stokes_single_layer_boundary",
        domain,
        range_,
        dual_to_range,
        parameters,
        assembler,
        [],
        "stokes_single_layer",
        "default_scalar",
        device_interface,
        precision,
        False,
        opt_layer,
    )
