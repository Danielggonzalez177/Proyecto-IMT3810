"""Stokes potential operators."""


def single_layer(
    space,
    points,
    parameters=None,
    assembler="dense",
    device_interface=None,
    precision=None,
    opt_layer=None,
):
    """Return a Stokes single-layer potential operator."""
    import bempp.api
    from bempp.api.assembly.assembler import PotentialAssembler
    from bempp.api.assembly.potential_operator import PotentialOperator
    from bempp.api.operators import OperatorDescriptor

    if precision is None:
        precision = bempp.api.DEFAULT_PRECISION

    operator_descriptor = OperatorDescriptor(
        "stokes_single_layer_potential",  # Identifier
        [],  # Options
        "stokes_single_layer",  # Kernel type
        "default_scalar",  # Assembly type
        precision,  # Precision
        False,  # Is complex
        None,  # Singular part
        1,  # Kernel dimension
        opt_layer,
    )

    return PotentialOperator(
        PotentialAssembler(
            space, points, operator_descriptor, device_interface, assembler, parameters
        )
    )
