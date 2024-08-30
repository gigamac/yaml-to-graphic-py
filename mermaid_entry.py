from mermaid_flowchart.FlowChart import FlowChart
from mermaid_flowchart.classPipeline import MermaidFlowChartObjects
from mermaid_flowchart.orientations import Orient
from mermaid_flowchart.write_document import write_document
import file_functions.openFile as openFile
import argparse
import sys

from pipeline.classPipeline import Pipeline

parser=argparse.ArgumentParser(description='creating a mermaid flowchart')
parser.add_argument('input_file')
args=parser.parse_args()

pipeline_objects = Pipeline('mermaid-pipeline',openFile.open_file(args.input_file))
mermaid_flow_objects = MermaidFlowChartObjects().build(pipeline_objects)
mermaid_flowchart = FlowChart(mermaid_flow_objects, Orient.top2bottom)
document = write_document(mermaid_flowchart, Orient.top2bottom)
# document = iter(document)
output_file_name = args.input_file.split('/')[-1].split('.')[0]

i = 1
f = open(output_file_name+'-'+str(i)+'.md', 'w')
f.writelines(document)
f.close
