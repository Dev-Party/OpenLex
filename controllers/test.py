# -*- coding: utf-8 -*-
# try something like
sexo_dic=[('','Todos'),('F','Femenino'), ('M','Masculino'), ('J','P.Jurídica')]
def contactSearch(self,url):
    #  Build drop-down list for districts
    form = FORM(LABEL(T('Sexo:')),
        SELECT(_name='sexo', _id='sexo',
                    _style='width:100px;',
                    value=request.get_vars.sexo,
                    *[k[1] for k in sexo_dic]),' ',
        LABEL(T('Ingrese:')),INPUT(_name='searchText',_value=request.get_vars.searchText,
           _style='width:70%;',
           _id='searchText'),
        INPUT(_type='submit',_value=T('Search')),
        INPUT(_type='submit',_value=T('Clear'),

        _onclick="jQuery('#district').val('');jQuery('#searchText').val('');"),
        _id='contactSearch',
        _method='GET',
        _action=url,
        )

    return form

@auth.requires_login()
def index():
    #  Get filters
    sex = request.get_vars.sexo
    searchText = request.get_vars.searchText

    #  Build query
    queries=[db.persona.created_by==auth.user.id]
    if searchText and searchText.strip() != '':
        queries.append(db.persona.apellido.contains(searchText))
    if sex:
        id_sex=[k[1] for k in sexo_dic].index(sex)
        cod_sex=[k[1] for k in sexo_dic][id_sex]
        if id_sex:
            queries.append(db.persona.sexo==cod_sex)
    if len(queries) > 0:
        query = reduce(lambda a,b:(a&b),queries)
        #constraints={'contact':query}

    grid = SQLFORM.grid(query,
                        user_signature=True,
                        maxtextlength=50,
                        search_widget=contactSearch)
    return locals()
