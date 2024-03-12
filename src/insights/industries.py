from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industries = set()
        for job in self.jobs_list:
            if job["industry"]:
                industries.add(job["industry"])
                return industries


process = ProcessIndustries()
process.read("data/jobs.csv")
unique_industries = process.get_unique_industries()
