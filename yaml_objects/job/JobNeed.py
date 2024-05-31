import re
from file_functions.tryNext import tryNext
from match_functions.identify_line import identify_line
from pipeline.Parsers import ParserFunction


class JobNeeds:
    job_needs = []
    current_line = ''
    PATTERN_JOB_SPEC = '^ {{{}}} {{0,}}- job: ([a-z,\-,0-9]*)'
    PATTERN_JOB = '^ {{{}}} {{1,}}- ([a-z,\-,0-9]*)[^:]{{0,1}}'
    PATTERN_JOB_ARTIFACT_TF = '^ {{{}}} {{1,}}artifacts: ([a-z]*)$'
    PATTERN_JOB_OPTIONAL_TF = '^ {{{}}} {{1,}}optional: ([a-z]*)$'
    pattern_job_needs_regex = []
    job_needs_parsers = []

    def job_spec(self,matching_rule, job_need, current_line):
        job_name = re.search(matching_rule,current_line).group(1)
        print(job_name)
        job_done = None
        if job_need.needed_job != '':
            self.job_needs.append(job_need)
            job_need = JobNeed(job_name)
        else:
            job_need.needed_job = job_name
        return job_need

    def job_artifact(self,matching_rule, job_need, current_line):
        job_need.artifact = re.search(matching_rule,current_line).group(1)
        job_done = None
        return job_need

    def job_optional(self,matching_rule, job_need, current_line):
        job_need.optional = re.search(matching_rule,current_line).group(1)
        job_done = None
        return job_need

    def load_parsers(self, indent):
        self.pattern_job_needs_regex = [
            self.PATTERN_JOB_SPEC.format(indent),
            self.PATTERN_JOB.format(indent),
            self.PATTERN_JOB_ARTIFACT_TF.format(indent),
            self.PATTERN_JOB_OPTIONAL_TF.format(indent)
            ]
        self.job_needs_parsers = [
            ParserFunction(self.PATTERN_JOB_SPEC.format(indent), self.job_spec),
            ParserFunction(self.PATTERN_JOB.format(indent), self.job_spec),
            ParserFunction(self.PATTERN_JOB_ARTIFACT_TF.format(indent), self.job_artifact),
            ParserFunction(self.PATTERN_JOB_OPTIONAL_TF.format(indent), self.job_optional)
        ]


    def add_job_needs(self,iter_lines):
        job_needs_patterns = self.job_needs_parsers
        parsing_regex_list = [getattr(job_needs_pattern, 'pattern') for job_needs_pattern in job_needs_patterns]
        current_line = tryNext(iter_lines)
        matching_rule = identify_line(parsing_regex_list, current_line)
        job_need = JobNeed('')
        parser_needs = []

        while matching_rule != '':
            print(re.search(matching_rule,current_line).group(1))
            rule_index = parsing_regex_list.index(matching_rule)
            print(rule_index)
            job_need = job_needs_patterns[rule_index].function(matching_rule, job_need, current_line)            
            current_line = tryNext(iter_lines)
            matching_rule = identify_line(parsing_regex_list, current_line)
        self.job_needs.append(job_need)
        self.current_line = current_line
        return self

    def __init__(self,iter_lines, current_line):
        self.current_line = current_line
        indent = len(re.search('^ *',self.current_line).group(0))
        self.job_needs = []
        self.load_parsers(indent)
        self.add_job_needs(iter_lines)
        print(self)

class JobNeed:
    needed_job = ''
    artifact = ''
    optional = ''

    def __init__(self, needed_job):
        self.needed_job = needed_job
        self.artifact = ''
        self.optional = ''
