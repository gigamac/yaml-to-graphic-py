# from functions.AssignEntryAlias import assignEntryAlias
# from classes.utilityClasses.classAlias import Alias, StageAlias
from mermaid_flowchart.orientations import Orient
# from functions.writeMermaidFlow.create_job_subGraph import create_job_subGraph
from mermaid_flowchart.classSubgraph import StageSubgraph


def parse_stages_to_charts(pipelineObject):
    # def add_stage_jobs_report_objects(entries, stage_alias):
    #     body = []
    #     for entry in entries:
    #         body.append(create_job_subGraph(entry,stage_alias, Orient.top2bottom))
        
    #     return body

    stage_start = 'stage-0'
    stage_subgraphs = []

    for stage in pipelineObject.stages:
        # running alias and subgraph together for now - will remove alias when all is well
        stage_subgraph = StageSubgraph(stage, Orient.top2bottom)
        stage_subgraph.add_jobs_to_body(pipelineObject.jobs)
        # stage_jobs = add_stage_jobs_report_objects(stage.body, stage.alias)
        # stage_subgraph.body = stage_jobs
        stage_subgraphs.append(stage_subgraph)

    return stage_subgraphs

