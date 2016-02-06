# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
__author__=u"María Andrea Vignau <mavignau@gmail.com>"
#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################



def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Bienvenido a pyDoctor")
    response.title = T("pyDoctor")
    content=T(u'Sistema para abogados y estudios jurídicos')
    modules=None
    features=None
    if auth.user:
        message=T("Bienvenido a pyDoctor, %s %s")%(auth.user.first_name,auth.user.last_name)
        modules=[{'url':URL('expedientes','index'),'img':'expedientes.png','alt':T('Administración de expedientes')},
                 {'url':URL('agenda','calendar'),'img':'calendario.png','alt':T('Calendario de vencimientos')},
                 {'url':URL('contactos','index'),'img':'personas.png','alt':T('Contactos')},
                 {'url':URL('other_tables','juzgados'),'img':'juzgados.png','alt':T('Oficinas judiciales')}
        ]
    else:
        message=T('¡Bienvenido! Pruébelo ya mismo.')
        features=[{'img':'feature-easy.png','alt':T('Intuitivo y muy fácil de usar, Ud. estára trabajando en sus expedientes inmediatamente. ')},
                 {'img':'feature-responsive.png','alt':T('Acceso total desde cualquier parte con conexión Internet. Podrá acceder desde todos sus dispositivos, computadoras o móviles')},
                 {'img':'feature-secure.png','alt':T('Tendrá sus datos en la seguridad absoluta de nuestros servidores. ¡Olvídese de las copias de seguridad!')},
                 {'img':'feature-fast.png','alt':T('Rápido de usar y veloz para empezar. Ahórrese el tiempo para instalar y configurar su software. Úselo ya mismo')}
        ]
    return dict(message=message,modules=modules,features=features)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())
