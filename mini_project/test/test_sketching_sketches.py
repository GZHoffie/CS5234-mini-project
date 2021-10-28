from mini_project.algorithms.sketching_sketches import L2Estimator, L1Estimator
from mini_project.utils import check_error

TEST_FILE = "sample"

def test_l2_estimator():
    """
    Test function for l2 estimator.
    """
    estimator = L2Estimator(100, 100)
    error = check_error(estimator, TEST_FILE)
    print("multiplicative error:", error)


def test_l1_estimator():
    """
    Test function for l2 estimator.
    """
    estimator = L1Estimator(0.05, 100)
    error = check_error(estimator, TEST_FILE, 'l1')
    print("multiplicative error:", error)


if __name__ == "__main__":
    test_l2_estimator()