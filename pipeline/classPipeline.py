import re
from fileinput import filelineno
from file_functions.tryNext import tryNext
from match_functions.identify_line import identify_line
from pipeline.give_objects_aliases import give_objects_aliases
from pipeline.pipeline_parser import pipeline_parser
from yaml_objects.job.classJob import Job


class Pipeline:
    name = ''
    iter_lines = iter([])
    variables = []
    stages = []
    includes = []
    jobs = []
    links = []
    jobsAsStr = ''

    def __init__(self, name, input_file):
        def parse_file(self):
            parsing_functions = pipeline_parser(self)
            parsing_regex_list = [getattr(parsing_function, 'pattern')[0] for parsing_function in parsing_functions]
            current_line = tryNext(self.iter_lines)
            while current_line != 'eof':
                matching_rule = identify_line(parsing_regex_list, current_line)
                try:
                    rule_index = parsing_regex_list.index(matching_rule)
                    print('this is the matching rule parser patternL: {}'.format(
                        parsing_functions[rule_index].pattern))
                    current_line = parsing_functions[rule_index].function(
                        self, current_line)
                except ValueError as e:
                    print('Value Error')
                    print('others tbd')
                    print(current_line)
                    current_line = tryNext(self.iter_lines)

            return self

        self.name = name
        self.iter_lines = iter(input_file)
        self = parse_file(self)
        give_objects_aliases(self.jobs,'job-0')

    # def __repr__(self):
    #     for job in self.jobs:
    #         jobStr = "["
    #         jobStr = jobStr +  "," + repr(job)
    #         print(repr(job))
    #         jobStr = jobStr + "]"

    #     self.jobsAsStr = jobStr

    #     return f'pipelineObject("name:{self.name}","stages:{self.stages}","includes:{self.includes}", "jobs:{self.jobsAsStr}")'
