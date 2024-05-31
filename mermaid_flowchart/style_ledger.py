from match_functions.identify_line import identify_line


class style_processor:
    link_count = 0
    style_rules = []

    def __init__(self):
        def rules():
            rules = []
            rules.append(style_rule('dependency','.* -- dependency -->.*','append', 'linkStyle {} stroke: #3498db,stroke-width:4px,color:blue;') )
            rules.append(style_rule('need','.* -- need -->.*','append', 'linkStyle {} stroke: #cb4335,stroke-width:4px,color:red;') )
            rules.append(style_rule('need_optional','.* -. need .->.*','append', 'linkStyle {} stroke:  #229954,stroke-width:4px,color:green;') )
            rules.append(style_rule('need_artifact','.* == need ==>.*','append', 'linkStyle {} stroke:  #cb4335,stroke-width:8px,color:red;') )
            rules.append(style_rule('stage_link','.*~~~.*','', '') )
            return rules

        self.link_count = 0
        self.style_rules.extend(rules())

    def add_link_ct(self):
        self.link_count = self.link_count + 1

    def process_line_for_rule(self,line):
        def apply_rule_to_line(matching_rule, rules_regex):
            rule_index = rules_regex.index(matching_rule)
            print(rule_index)
            if self.style_rules[rule_index].append_or_inline == 'append':
                self.style_rules[rule_index].matched_lines.append(str(self.link_count))
            
            self.link_count = self.link_count + 1
        
        rules_regex =list (rule.match_expression for rule in self.style_rules)
        matching_rule = identify_line(rules_regex,line)
        if matching_rule != '':
            apply_rule_to_line(matching_rule, rules_regex)
        print(matching_rule)

    def append_styles(self):
        appends = []
        for rule in self.style_rules:
            if len(rule.matched_lines) > 0:
                appends.append(rule.formatting.format(','.join(rule.matched_lines)))
                print(appends)

        return appends
    
class style_rule:
    name = ''
    match_expression = ''
    append_or_inline = ''
    formatting = ''
    matched_lines = []
    def __init__(self,name, match_expression, append_or_inline, formatting):
        self.name = name
        self.match_expression = match_expression
        self.formatting = formatting
        self.append_or_inline = append_or_inline
        self.matched_lines = []
