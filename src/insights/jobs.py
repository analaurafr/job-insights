from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            read_data = csv.DictReader(file, delimiter=",")
            for row in read_data:
                if row:
                    self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(job["job_type"] for job in self.jobs_list)
        return list(unique_job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


process = ProcessJobs()
process.read("data/jobs.csv")
unique_job_types = process.get_unique_job_types()
