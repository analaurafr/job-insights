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
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


process = ProcessSalaries()
process.read("data/jobs.csv")
max_salary = process.get_max_salary()
