#!/usr/bin/env python3

import optparse
import LocationStruct

def process_options():
    '''This specifies options how to run program.
    Multiple options can run. When run without any option, provide only name and IATA code of airport.'''
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("--cities", dest="cities", action="store_true", help="prints cities with airports")
    parser.add_option("--coords", dest="coordinates", action="store_true", help="prints coordinates")
    parser.add_option("--iata", dest="iata", action="store_true", help="prints IATA codes")
    parser.add_option("--names", dest="names", action="store_true", help='prints names for airports')
    parser.add_option('--full', dest='full', action="store_true", help='prints all details')
    opts, args = parser.parse_args()
    some_option_set = opts.names or opts.full or opts.iata or opts.coordinates or opts.cities
    if not some_option_set:
        opts.names = True
        opts.iata = True
    return opts, args

opts, args = process_options() 
airports = LocationStruct.Locations(opts)
airports.print_locations()