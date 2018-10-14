'''
Copyright (C) 2018 Rafael Tavares
endssgamesstudio@bol.com.br

Created by Rafael Tavares

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Upbge Game Objects",
    "author": "RafaelTavares(EndSSGames)",
    "version": (0, 2),
    "blender": (2, 79, 6),
    "location": "View3D > Tools > Upbge Objects",
    "description": "adds several game objects for free use",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "UPBGE"}
	
import bpy
from math import *
import os
from . import __init__
from . import class_game_objects


	
	
	
	
	
	
	
def register():
    bpy.utils.register_module(__name__)
   
def unregister():
    bpy.utils.unregister_module(__name__)