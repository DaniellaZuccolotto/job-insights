from src.pre_built.sorting import sort_by
from tests.sorting.mocks import sort_by_any_criteria


jobs = [
    {"max_salary": 1000, "min_salary": 1000, "date_posted": "2020-01-01"},
    {"max_salary": 2000, "min_salary": 2000, "date_posted": "2020-01-02"},
]


def test_sort_by_criteria():
    assert sort_by(jobs, "max_salary") == sort_by_any_criteria(
        jobs, "max_salary"
    )
    assert sort_by(jobs, "min_salary") == sort_by_any_criteria(
        jobs, "min_salary"
    )
    assert sort_by(jobs, "date_posted") == sort_by_any_criteria(
        jobs, "date_posted"
    )
