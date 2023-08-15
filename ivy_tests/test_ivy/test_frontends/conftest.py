import pytest
from ivy import DefaultDevice
from ivy_tests.test_ivy.helpers import globals as test_globals

@pytest.fixture(autouse=True)
def setup_teardown_fixture(request, on_device, backend_fw, frontend, compile_graph, implicit):
    """
    A pytest fixture for setting up and tearing down the testing environment.
    
    Args:
        request: The pytest request object.
        on_device: The target device for the test.
        backend_fw: Backend framework object.
        frontend: Ivy frontend for testing.
        compile_graph: Compilation flag.
        implicit: Implicit flag.
    """
    # Check if the test function has test_data attribute
    if hasattr(request.function, "test_data"):
        try:
            # Set up Ivy testing environment based on test_data
            test_globals.setup_frontend_test(
                request.function.test_data, frontend, backend_fw.backend, on_device
            )
        except Exception as e:
            test_globals.teardown_frontend_test()
            raise RuntimeError(f"Setting up test for {request.function} failed.") from e
        with backend_fw.use, DefaultDevice(on_device):
            yield
        test_globals.teardown_frontend_test()
    else:
        with backend_fw.use, DefaultDevice(on_device):
            yield

def with_test_data(test_data):
    """
    A decorator to attach test_data to a test function.
    
    Args:
        test_data: Test data to be attached to the test function.
    """
    def decorator(test_func):
        test_func.test_data = test_data
        return test_func
    return decorator
