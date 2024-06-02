class Stage():
    name = ''
    alias = ''
    link = ''
    stage_link_name = ''
    body = []
    def __init__(self, stage, body):
        self.name = stage        
        self.body = body
