import re

# class Rules():
#     rules = []


# class Rule():
#     ruleType = ''
#     when = ''
#     body = []

#     def __init__(self, stage, body):
#         self.stage = stage
#         self.body = body

#     def addJob(self, job):
#         self.body.append(job)

# class RuleChange():
#     paths = []

#     def __init__(self, path):
#         self.paths.append(path)

# class RuleIf():
#     condition = ''
#     when = ''

#     def __init__(self, clause):
#         condition = clause


class Rules():
    rules = []


class Rule():
    ruleType = ''
    when = ''
    body = []

    def __init__(self, stage, body):
        self.stage = stage
        self.body = body

    def addJob(self, job):
        self.body.append(job)

class RuleChange():
    paths = []

    def __init__(self, path):
        self.paths.append(path)

class RuleIf():
    condition = ''
    statements = ''

    def __init__(self, current_line, file_lines):
        def parse_if_statement(current_line):
            result = ''
            if_regex = '^(\s{1,}- if: (.*))'
            if_groups = re.search(if_regex, current_line).group(0)
            print(current_line)
            for group in if_groups.group():
                print(group)
            return if_groups.group(1)

        condition = parse_if_statement(current_line)

        

