def lang_genoeg(lengte):
    'kijkt of iemand lang genoeg is voor een attractie'
    if lengte >= 120:
        return('je bent lang genoeg voor attractie')
    else:
        return('sorry je bent te klein')

print(lang_genoeg(130))