
# Import Statements
import hypothesis.strategies as st
from ivy_tests.test_ivy.helpers import (
    dtype_and_values, get_dtypes, ints, test_frontend_function
)

# Test Function Definitions
# Kaiser Window Test
def test_tensorflow_kaiser_window(
    dtype_and_window_length,
    dtype_and_beta,
    dtype,
    frontend,
    test_flags,
    fn_tree,
    backend_fw,
    on_device,
):
    window_length_dtype, window_length = dtype_and_window_length
    beta_dtype, beta = dtype_and_beta
    test_frontend_function(
        input_dtypes=[window_length_dtype[0], beta_dtype[0]],
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        window_length=window_length,
        beta=beta,
        dtype=dtype,
    )

# IDCT Test
def test_tensorflow_idct(
    dtype_x_and_args,
    frontend,
    test_flags,
    fn_tree,
    backend_fw,
    on_device,
):
    input_dtype, x, type, n, axis, norm = dtype_x_and_args
    test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        input=x[0],
        type=type,
        n=n,
        axis=axis,
        norm=norm,
        atol=1e-01,
    )

# DCT Test
def test_tensorflow_dct(
    dtype_and_x,
    n,
    norm,
    type,
    frontend,
    test_flags,
    fn_tree,
    backend_fw,
    on_device,
):
    input_dtype, x = dtype_and_x
    if norm == "ortho" and type == 1:
        norm = None
    axis = -1
    test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        input=x[0],
        type=type,
        n=n,
        axis=axis,
        norm=norm,
    )

# Vorbis Window Test
def test_tensorflow_vorbis_window(
    dtype_and_x,
    test_flags,
    backend_fw,
    fn_tree,
    on_device,
    frontend
):
    input_dtype, x = dtype_and_x
    test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        atol=1e-02,
        window_length=int(x[0]),
    )

# Hypothesis Strategies
valid_idct = st.composite(lambda draw: (
    draw(dtype_and_values(
        available_dtypes=["float32", "float64"],
        max_value=65280,
        min_value=-65280,
        min_num_dims=1,
        min_dim_size=2,
        shared_dtype=True
    )),
    draw(st.sampled_from([-1, 0, 1])),  # type
    None,  # n
    -1,    # axis
    draw(st.sampled_from([None, "ortho"]))  # norm
))




