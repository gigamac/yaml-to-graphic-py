def tryNext(myIterator):
    try:
        return next(myIterator)
    except:
        return 'eof'
