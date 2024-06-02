
import re
from file_functions.tryNext import tryNext
from pipeline.Parsers import ParserFunction
from yaml_objects.classStages import Stages
from yaml_objects.job.classJob import Job


def pipeline_parser(pipeline_object):
    def default(pipeline_object, current_line):
        print(PATTERN_DEFAULT)
        print(current_line)
        return tryNext(pipeline_object.iter_lines)

    def include(pipeline_object, current_line):
        print(PATTERN_DEFAULT)
        print(current_line)
        return tryNext(pipeline_object.iter_lines)

    def stages(pipeline_object, current_line):
        print(PATTERN_STAGES)
        print(current_line)
        stages = Stages(pipeline_object.iter_lines)
        pipeline_object.stages = stages.stages
        pipeline_object.current_line = stages.current_line
        pipeline_object.links.extend(
            stage.link for stage in pipeline_object.stages)
        return pipeline_object.current_line

    def variables(pipeline_object, current_line):
        print('match unprocessed: rule: {}, line: {}'.format(
            PATTERN_VARIABLES, current_line))
        return tryNext(pipeline_object.iter_lines)

    def workflow(pipeline_object, current_line):
        print('match unprocessed: rule: {}, line: {}'.format(
            PATTERN_WORKFLOW, current_line))
        return tryNext(pipeline_object.iter_lines)

    def specs(pipeline_object, current_line):
        print('match unprocessed: rule: {}, line: {}'.format(
            PATTERN_SPEC, current_line))
        return tryNext(pipeline_object.iter_lines)

    def job(pipeline_object, current_line):
        print(('(^{} ({})').format('(^[a-z,\-,\_,0-9]{1,}):$', 'in other words jobs!'))
        print(current_line)
        job_name = re.search('(^[a-z,\-,\_,0-9]{1,}):$', current_line).group(1)
        job = Job(job_name).parse_job(pipeline_object.iter_lines).set_alias(len(pipeline_object.jobs))
        pipeline_object.jobs.append(job)
        return job.current_line

    def crlf(pipeline_object, current_line):
        print(('{} ({})').format(PATTERN_CRLF, 'blank line!'))
        print(current_line)
        return tryNext(pipeline_object.iter_lines)

    PATTERN_DEFAULT = '^default:$',
    PATTERN_INCLUDE = '^include:$',
    PATTERN_STAGES = '^stages:$',
    PATTERN_VARIABLES = '^variables:$',
    PATTERN_WORKFLOW = '^workflow:$',
    PATTERN_SPEC = '^spec:$',
    PATTERN_JOB = '(^[a-z,\-,\_,0-9]{1,}):$',
    PATTERN_CRLF = '^$',

    pipeline_parsers = [
        ParserFunction(PATTERN_DEFAULT, default),
        ParserFunction(PATTERN_INCLUDE, include),
        ParserFunction(PATTERN_STAGES, stages),
        ParserFunction(PATTERN_VARIABLES, variables),
        ParserFunction(PATTERN_WORKFLOW, workflow),
        ParserFunction(PATTERN_SPEC, specs),
        ParserFunction(PATTERN_JOB, job),
        ParserFunction(PATTERN_CRLF, crlf),

    ]
    return pipeline_parsers
