import re
from file_functions.tryNext import tryNext
from match_functions.identify_line import identify_line
from mermaid_flowchart.links import LinksTexted
from pipeline.Parsers import ParserFunction
from pipeline.ParsingAssist import ParsingAssist
from yaml_objects.job.JobNeed import JobNeeds


class Job:
    PATTERN_STAGE = '^ *stage: ([a-z,\-,0-9]{1,})$'
    PATTERN_EXTENDS = '^ *extends: \.([a-z,\-]{1,})$'
    PATTERN_NEEDS = '^ *needs: {0,}$'
    PATTERN_DEPENDENCIES = '^ *dependencies: {0,}$'
    PATTERN_ANY_OTHER_JOB_DATA = '^ {1,}.*'
    PATTERN_COMMENT = '^ {1,}#{1,}.*$'
    job_parsers = []
    stage = ''
    name = ''
    alias = ''
    extends = ''
    allowFailure = ''
    needs = []
    links = []
    uses_artifacts = []
    produces_artifacts = []
    dependencies = []
    variables = []
    rules = []
    conditions = []
    current_line = ''

    def pick_new_entries_for_a_list(self,target_list, new_list):
        return_new = []
        for entry in new_list:
            if len([x for x in target_list if x.needed_job == entry.needed_job]) == 0:
                return_new.append(entry)
        return return_new    

    def build_links(self,data, type):
        links = []
        match type:
            case 'dependencies':
                for dependency in data:
                    links.append(LinksTexted.from_to.format(dependency,'dependency',self.name))
            case 'needs':
                for need in data:
                    if need.artifact == 'true':
                        if need.optional == 'true':
                            link = LinksTexted.optional_from_to
                        else:
                            link = LinksTexted.thick
                    else:
                        if need.optional == 'true':
                            link = LinksTexted.optional_from_to
                        else:
                            link = LinksTexted.from_to
                    links.append(link.format(need.needed_job,'need',self.name))

        return links

    def add_stage(self, iter_lines):
        self.stage = re.search(self.PATTERN_STAGE,self.current_line).group(1)
        self.current_line = tryNext(iter_lines)

    def add_extends(self, iter_lines):
        self.extends = re.search(self.PATTERN_EXTENDS,self.current_line).group(1)
        self.current_line = tryNext(iter_lines)

    def add_dependencies(self, iter_lines):
        indent = len(re.search('^ *',self.current_line).group(0))
        PATTERN_DEPENDENCY = '^ {{{}}} {{1,}}- ([a-z,\-,0-9]*)'.format(indent)
        print(PATTERN_DEPENDENCY)

        self.current_line = tryNext(iter_lines)
        matching_rule = identify_line([PATTERN_DEPENDENCY], self.current_line)
        while matching_rule != '':
            self.dependencies.append(re.search(PATTERN_DEPENDENCY,self.current_line).group(1))
            self.current_line = tryNext(iter_lines)
            matching_rule = identify_line([PATTERN_DEPENDENCY], self.current_line)

        self.links.extend(self.build_links(self.dependencies, 'dependencies'))

    def add_job_needs(self, iter_lines):
        indent = len(re.search('^ *',self.current_line).group(0))
        job_needs = JobNeeds(iter_lines, self.current_line)
        self.current_line = job_needs.current_line
        unique_new_needs = self.pick_new_entries_for_a_list(self.needs,job_needs.job_needs)
        self.needs.extend(unique_new_needs)
        self.links.extend(self.build_links(unique_new_needs, 'needs'))
    
    def other_job_patterns(self,iter_lines):
        self.current_line = tryNext(iter_lines)

    def load_parsers(self):
            self.job_parsers = [
            ParserFunction(self.PATTERN_STAGE, self.add_stage),
            ParserFunction(self.PATTERN_EXTENDS, self.add_extends),
            ParserFunction(self.PATTERN_DEPENDENCIES, self.add_dependencies),
            ParserFunction(self.PATTERN_NEEDS, self.add_job_needs),
            ParserFunction(self.PATTERN_ANY_OTHER_JOB_DATA, self.other_job_patterns),
            ParserFunction(self.PATTERN_COMMENT, self.other_job_patterns),
        ]

    def __init__(self, name):
        self.load_parsers()
        self.name = name
        self.stage = ''
        self.alias = ''
        self.extends = ''
        self.allowFailure = ''
        self.needs = []
        self.links = []
        self.uses_artifacts = []
        self.produces_artifacts = []
        self.dependencies = []
        self.variables = []
        self.rules = []
        self.conditions = []

    def parse_job(self,iter_lines):

        regex_job = [getattr(job_parser, 'pattern') for job_parser in self.job_parsers]

        self.current_line = tryNext(iter_lines)
        matching_rule = identify_line(regex_job,self.current_line)
        while matching_rule != '':
            try:
                rule_index = regex_job.index(matching_rule)
                print('this is the matching rule parser patternL: {}'.format(
                    self.job_parsers[rule_index].pattern))
                self.job_parsers[rule_index].function(iter_lines)
            except ValueError as e:
                print('Value Error')
                print('others tbd')
                print(self.current_line)
                self.current_line = tryNext(iter_lines)
            matching_rule = identify_line(regex_job, self.current_line)
        return self
    
    def __repr__(self):
        return f'job("{self.stage}","{self.name}","{self.extends}", "{self.allowFailure}","{self.needs}","{self.uses_artifacts}","{self.produces_artifacts}","{self.dependencies}","{self.variables}","{self.rules}","{self.conditions}")'
