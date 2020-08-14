class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(list)
        for k, v in prerequisites:
            course_graph[v].append(k)
        # print(course_graph)
        checked = [False] * numCourses
        path = [False] * numCourses
        
        for i in range(numCourses):
            if self.isCyclic(i, course_graph, path, checked):
                return False
        return True
        
    def isCyclic(self, course, course_graph, path, checked):
        if checked[course]:
            return False
        if path[course]:
            return True
        
        path[course] = True
        check = False
        
        for val in course_graph[course]:
            check = self.isCyclic(val, course_graph, path, checked)
            # print(check, val)
            if check:
                break
        path[course] = False
        checked[course] = True
        
        return check