from mermaid_flowchart.orientations import Orient
from yaml_objects.job.classJob import Job

class Subgraph:
    direction = 'direction LR'
    alias = ''
    actual = ''
    title = 'subgraph One'
    link = ''
    body = []
    end = 'end'
    def __init__(self, title,body, orientation):
        self.title = 'subgraph {}'.format(title)
        self.direction = '  direction {}'.format(orientation)
        self.orientation = orientation
        self.body = body

class StageSubgraph(Subgraph):

    def  add_jobs_to_body(self,jobs):
        stage_jobs = list(filter(lambda job: (job.stage == self.actual), jobs))
        for job in stage_jobs:
            self.body.append(job.name)
        for job in stage_jobs:
            for link in job.links:
                self.body.append(link)

    def __init__(self, stage, orientation):
        super().__init__('{}-{}[{}]'.format(stage.alias, stage.name, stage.name), [], orientation)
        self.alias = stage.alias
        self.actual = stage.name
        self.link = stage.link
        self.body = []
