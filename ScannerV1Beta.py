#!/usr/bin/env python
#
# Copyright (C) 2011-2012  Raoul Grosser
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
# Raoul Grosser <Raoul@pythonscanner.com>
#
from socket import * 

if __name__ == '__main__':
    target = raw_input('Enter host or ip to scan: ')
    targetIP = gethostbyname(target)
    print 'Starting scan on host ', targetIP

    #scan reserved ports
    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()

