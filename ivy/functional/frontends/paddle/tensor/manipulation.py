# global
import ivy
from ivy.functional.frontends.paddle.func_wrapper import (
    to_ivy_arrays_and_back,
)
from ivy.func_wrapper import (
    with_unsupported_dtypes,
    with_supported_dtypes,
)


@to_ivy_arrays_and_back
def reshape(x, shape):
    return ivy.reshape(x, shape)


@with_unsupported_dtypes({"2.5.0 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def abs(x, name=None):
    return ivy.abs(x)


absolute = abs


@to_ivy_arrays_and_back
def stack(x, axis=0, name=None):
    return ivy.stack(x, axis=axis)


@with_unsupported_dtypes({"2.5.0 and below": ("int8", "int16")}, "paddle")
@to_ivy_arrays_and_back
def concat(x, axis, name=None):
    return ivy.concat(x, axis=axis)


@with_unsupported_dtypes(
    {"2.5.0 and below": ("int8", "uint8", "int16", "float16")},
    "paddle",
)
@to_ivy_arrays_and_back
def tile(x, repeat_times, name=None):
    return ivy.tile(x, repeats=repeat_times)


@with_unsupported_dtypes(
    {"2.5.0 and below": ("int16", "complex64", "complex128")},
    "paddle",
)
@to_ivy_arrays_and_back
def split(x, num_or_sections, axis=0, name=None):
    return ivy.split(x, num_or_size_splits=num_or_sections, axis=axis)


@with_unsupported_dtypes(
    {"2.5.0 and below": ("float16", "bfloat16", "int8", "int16")},
    "paddle",
)
@to_ivy_arrays_and_back
def squeeze(x, axis=None, name=None):
    return ivy.squeeze(x, axis=axis)


@with_supported_dtypes(
    {"2.5.0 and below": ("bool", "float32", "float64", "int32", "int64")},
    "paddle",
)
@to_ivy_arrays_and_back
def expand(x, shape, name=None):
    return ivy.expand(x, shape)


@with_supported_dtypes(
    {
        "2.5.0 and below": (
            "bool",
            "float16",
            "float32",
            "float64",
            "int32",
            "int64",
            "uint8",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def cast(x, dtype):
    return ivy.astype(x, dtype)


@with_supported_dtypes(
    {"2.5.0 and below": ("bool", "float32", "float64", "int32", "int64")},
    "paddle",
)
@to_ivy_arrays_and_back
def broadcast_to(x, shape, name=None):
    return ivy.broadcast_to(x, shape)

@to_ivy_arrays_and_back
def reshape_(x, shape):
    return ivy.reshape_(x, shape)

@with_unsupported_dtypes(
    {"2.5.0 and below": ("float32", "bfloat16"), "paddle")
    return ivy.reshape_(x, shape)
