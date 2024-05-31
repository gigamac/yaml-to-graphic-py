import re
from file_functions.tryNext import tryNext
from match_functions.identify_line import identify_line
from pipeline.give_objects_aliases import give_objects_aliases
from yaml_objects.classStage import Stage


class Stages: 
    current_line = ''
    stages = []

    def __init__(self,iter_lines):
        def get_stage_name(thisLine, matching_rule):
            parsedLine = re.search(matching_rule, thisLine)
            if len(parsedLine.groups()) > 0:
                return parsedLine.group(1)
            else:
                print('error in stage line possible end of list', thisLine)
        
        def link_stages(self):
            prev_stage = ''
            for stage in self.stages:
                if prev_stage != '':
                    stage.link = ('{} ~~~ {}').format(prev_stage.stage_link_name, stage.stage_link_name)            
                prev_stage = stage
                    
            return self

        current_line = tryNext(iter_lines)
        stages_regex = ['^  - (.*)','^ *$', '^ *#*.*$']
        matching_rule = identify_line(stages_regex, current_line)
        print('matching_rule is: ',matching_rule)
        while (matching_rule == '^  - (.*)'):
            self.stages.append(Stage(get_stage_name(current_line, matching_rule),[]))
            current_line = tryNext(iter_lines)
            matching_rule = identify_line(stages_regex, current_line)
        
        self.current_line = current_line
        give_objects_aliases(self.stages,'stage-0')
        link_stages(self)
