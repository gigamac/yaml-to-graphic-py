class FlowChart:
    header = ''
    described = ''
    charts = []
    footer = ''
    def __init__(self, mermaid_flow_objects, orientation):
        self.header = '```mermaid'
        self.described = 'flowchart {}'.format(orientation)
        self.charts = mermaid_flow_objects.charts
        self.links = []
        self.footer = '```'
