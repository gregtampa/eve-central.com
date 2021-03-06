#    EVE-Central.com Codebase
#    Copyright (C) 2006-2012 StackFoundry LLC and Yann Ramin
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import Cheetah.Template


def template(file,session):
    t = None
    try:
        t = Cheetah.Template.Template(file = '/www/eve-central.com/web/templates/' + file)
    except:
        t = Cheetah.Template.Template(file = 'templates/' + file)

    try:
        t.isigb = session['isigb']
    except:
        t.isigb = False


    t.session = session
    return t
