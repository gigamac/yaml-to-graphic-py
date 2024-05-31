from pipeline.AssignEntryAlias import assignEntryAlias
def give_objects_aliases(namees, seed):
    alias = seed
    for namee in namees:
        alias = assignEntryAlias(alias)
        namee.alias = alias
        namee.stage_link_name = stage_link_name = '{}-{}'.format(alias, namee.stage)

    return namees
