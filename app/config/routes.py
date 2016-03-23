
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users/new'] = 'Users#new'
routes['GET']['/travels'] = 'Travels#index'
routes['GET']['/travels/add'] = 'Travels#add_plan'
routes['POST']['/travels/new'] = 'Travels#new'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/destination/<int:id>'] = 'Travels#destination'
routes['GET']['/travels/join/<int:id>'] = 'Travels#join'





"""

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
