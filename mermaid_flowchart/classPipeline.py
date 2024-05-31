from mermaid_flowchart.flowchart_stages import parse_stages_to_charts

class Pipeline:
    name = ''
    variables = []
    stages = []
    includes = []
    jobs = []
    links = []
    jobsAsStr = ''
    def __init__(self):
        self = self

class MermaidFlowChartObjects():
    charts = []
    links = []

    def __init__(self):
        Pipeline.__init__(self)
    
    
 
    def build(self,pipeline_objects):
        self.charts.extend(parse_stages_to_charts(pipeline_objects))
        return self

    def __repr__(self):
        for job in self.jobs:
            jobStr = "["
            jobStr = jobStr +  "," + repr(job)
            print(repr(job))
            jobStr = jobStr + "]"
        
        self.jobsAsStr = jobStr

        return f'pipelineObject("name:{self.name}","stages:{self.stages}","includes:{self.includes}", "jobs:{self.jobsAsStr}")'


