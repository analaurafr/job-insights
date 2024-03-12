from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = set(
            job["industry"] for job in self.jobs_list if job.get("industry")
        )
        return list(unique_industries)


processInstance = ProcessIndustries()
processInstance.read("tests/mocks/jobs_with_industries.csv")

unique_industries = processInstance.get_unique_industries()
print(unique_industries)
