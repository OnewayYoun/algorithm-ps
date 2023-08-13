from collections import defaultdict


def dfs(lst: list, tickets, routes, visited, answer):
    if len(tickets) + 1 == len(lst):
        answer.append(lst[:])
        return
    curr = lst[-1]
    for idx, val in enumerate(routes[curr]):
        if not visited[curr][idx]:
            visited[curr][idx] = True
            lst.append(routes[curr][idx])
            dfs(lst, tickets, routes, visited, answer)
            lst.pop()
            visited[curr][idx] = False


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0] != 'ICN', x[1]))
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    visited = {key: [False] * len(routes[key]) for key in routes}
    dfs(['ICN'], tickets, routes, visited, answer)
    return answer[0]


if __name__ == '__main__':
    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]  # ["ICN", "JFK", "HND", "IAD"]
    # tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    tickets = [["ICN", "JFK"], ["ICN", "IAD"], ["JFK", "ICN"]]
    print(solution(tickets))
