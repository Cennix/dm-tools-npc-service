# dm-tools-npc-service
A service for the DM tools written using python


# First Stage - NPC Overview

## Npc Detials
This should contain all the important information about an NPC.

A user should be to:
- Search for a specific NPC, by name
- Get list of all NPCs top level information

## Npc Relationship Mapper
This shows how 2 NPCs are related & the detials of that relationship.

A user should be able to:
- Get all NPCs related to a target NPC
- Get all NPCs & their relationships to one another



# SetUp

### Create a virtual environment to isolate our package dependencies locally
> python -m venv env
>
> env\Scripts\activate

### Install Django and Django REST framework into the virtual environment
> pip install django
>
> pip install djangorestframework
 
### Set up a new project with a single application
> django-admin startproject DmToolsBackend .  # Note the trailing '.' character to keep in current folder
>
> python manage.py migrate

Got to DmToolsBackend/settings.py & add 'rest_framework' to the INSTALLED_APPS list.

Add `path('api-auth/', include('rest_framework.urls')),` to the urlpatterns list in DmToolsBackend/api.py.


## New App
> django-admin startapp NpcManager

Create urls.py & serializers.py inside NpcManager/

Got to DmToolsBackend/settings.py & add 'NpcManager' to the INSTALLED_APPS list.

Add to urls.py aswell.
