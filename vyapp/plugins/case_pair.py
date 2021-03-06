"""

"""

def install(area, setup={'background':'pink', 'foreground':'black'}, 
            MAX=1500, TIME=500):

    def cave(tag, args):
        area.after(TIME, cave, tag, args)
        index = area.case_pair(MAX, *args)

        if not index: 
            area.tag_remove(tag, '1.0', 'end')
        else:
            area.tag_update(tag, '1.0', 'end', 
                            ('insert', 'insert +1c'), (index, '%s +1c' % index))

    area.tag_config('_paren_', **setup)
    area.tag_config('_bracket_', **setup)
    area.tag_config('_brace_', **setup)
    cave('_paren_', ('(', ')'))
    cave('_bracket_', ('[', ']'))
    cave('_brace_', ('{', '}'))





















