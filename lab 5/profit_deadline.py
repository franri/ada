
import operator

class Job:

    def __init__(self, name, profit, time, deadline):
        self.name = name
        self.profit = profit
        self.time = time
        self. deadline = deadline

    def  __repr__(self):
        # return 'J({}, {}, {})'.format(self.profit, self.time, self.deadline)
        return self.name

def process_DYNPROG_NOFUNCIONAAAAAA(u_jobs): # jobs sorted ascending by deadline. No importa el profit
    jobs = sorted(u_jobs, key= lambda j: (j[3], -j[1]))
    print(u_jobs)
    print(jobs)
    schedule = {} # key: time taken. Saves max profit with that time taken


    # schedule has list with:
    #   pos 0: profit
    #   pos 1: time taken
    #   pos 2: list of activities in execution order
    max_time_taken = 0
    schedule[0] = [0, 0, None]
    for i in range(len(jobs)):
        current_job = jobs[i]
        past_profit = -100 if max_time_taken==0 else schedule[max_time_taken][0]
        time_left_if_do_job = current_job[3] - current_job[2]
        while time_left_if_do_job not in schedule:
                time_left_if_do_job-=1
        p_t_j_cache_list = schedule[time_left_if_do_job]
        additional_profit = p_t_j_cache_list[0]
        new_profit = additional_profit + current_job[1]
        if new_profit > past_profit:
            if p_t_j_cache_list[2] is None:
                updated_job_list = []
            else:
                updated_job_list = p_t_j_cache_list[2][:]
            updated_job_list.append(current_job)
            new_time = current_job[2] + p_t_j_cache_list[1]
            node = [new_profit, new_time, updated_job_list]
            schedule[new_time] = node
            max_time_taken = new_time
        
        print(schedule)
    
    return schedule[max_time_taken]

def process(u_jobs):
    jobs = sorted(u_jobs, key= lambda j: (j[3], -j[1]))
    print(jobs)


   
   
if __name__ == "__main__":
        # m = [
        #     ["a", 20, 1, 4],
        #     ["b", 10, 1, 1],
        #     ["c", 40, 1, 1],
        #     ["d", 30, 1, 1]
        # ]

        m = [
            ["a", 100, 1, 2],
            ["b", 19, 1, 1],
            ["c", 27, 1, 2],
            ["d", 25, 1, 1],
            ["e", 15, 1, 3],
            ["e", 50, 2, 3]
        ]

        u_jobs = [Job(i, j, k, l) for i, j, k, l in m]

        print(process_DYNPROG_NOFUNCIONAAAAAA(m))


