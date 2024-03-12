from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            read_data = csv.DictReader(file, delimiter=",")
            for row in read_data:
                if row:
                    self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(job["job_type"] for job in self.jobs_list)
        return list(unique_job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[Dict]:
        filtered_jobs = []

        if not isinstance(filter_criteria, dict):
            raise TypeError

        for job in jobs:
            criteria_match = all(
                job.get(key) == value for key, value in filter_criteria.items()
            )
            if criteria_match:
                filtered_jobs.append(job)

        return filtered_jobs
