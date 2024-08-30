import re
from file_functions.tryNext import tryNext
from match_functions.identify_line import identify_line

def process_unclassified_sub_line(iter_lines,current_line):
    unprocessed_regex = ['^  (.*)']
    matching_rule = identify_line(unprocessed_regex, current_line)
    print('matching_rule is: ',matching_rule)
    while (matching_rule == unprocessed_regex[0]):
        current_line = tryNext(iter_lines)
        matching_rule = identify_line(unprocessed_regex, current_line)
    return current_line
