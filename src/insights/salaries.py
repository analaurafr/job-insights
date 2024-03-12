from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salaries = []
        for job in self.jobs_list:
            salary = job["max_salary"]
            if salary.strip().isdigit():
                max_salaries.append(int(salary))

        return max(max_salaries)

    def get_min_salary(self) -> int:
        min_salaries = []
        for job in self.jobs_list:
            salary = job["min_salary"]
            if salary.strip().isdigit():
                min_salaries.append(int(salary))

        return min(min_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        keys = ["min_salary", "max_salary"]

        try:
            salary = int(str(salary))
        except ValueError:
            raise ValueError()

        if not all(
            key in job and str(job[key]).isdigit() for key in keys
        ) or int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError()

        return int(job["min_salary"]) <= salary <= int(job["max_salary"])

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
