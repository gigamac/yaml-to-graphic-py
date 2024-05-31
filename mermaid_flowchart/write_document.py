from mermaid_flowchart.style_ledger import style_processor
def write_document(mermaid_flowchart,orientation):
    apply_styles = style_processor()
    documents = []
    documents.append('{}\n'.format(mermaid_flowchart.header))
    documents.append('{}\n'.format(mermaid_flowchart.described))
    for chart in mermaid_flowchart.charts:
        document = []
        document.append('{}\n'.format(chart.title))
        document.append('{}\n'.format(chart.direction))
        if chart.body != []:
            for line in chart.body:
                apply_styles.process_line_for_rule(line)
                document.append('{}\n'.format(line))

        document.append('{}\n'.format(chart.end))
        if chart.link != '':
            apply_styles.process_line_for_rule(chart.link)
            document.append('{}\n'.format(chart.link))
        documents.extend(document)

    style_appends = apply_styles.append_styles()
    for style in style_appends:
        documents.append('{}\n'.format(style))

    documents.append('{}\n'.format(mermaid_flowchart.footer))
    return documents
