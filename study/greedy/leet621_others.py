from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        task_occ_dict = Counter(tasks)
        
        max_occ = max(task_occ_dict.values())
        number_of_tasks_of_max_occ = sum((1 for task, occ in task_occ_dict.items() if occ == max_occ))
        
        # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
        # Fill each group with uniform iterleaving as even as possible

        # At last, execute for the last time of max_occ jobs
        interval_for_schedule = (max_occ - 1) * (n + 1) + number_of_tasks_of_max_occ

        # Minimal length is original length on best case.
        # Otherswise, it need some cooling intervals in the middle
        return max(len(tasks), interval_for_schedule)