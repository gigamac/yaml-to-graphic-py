def assignEntryAlias(entry):
    entrySplit = entry.split('-')
    newIndex = int(entrySplit[1])+1
    return "{}-{}".format(entrySplit[0],str(newIndex))

