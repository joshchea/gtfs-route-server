# gtfs-route-server
Build Time Expanded Search Graphs Using GTFS Data

Contributors: Chetan Joshi, Portland OR
Requires: Python with standard modules and networkx
Tested with: GTFS data from psrc consolidated file and trimet
License: The MIT License (MIT)
License URI: https://opensource.org/licenses/MIT
Description: Generates a search graph as edge list that may be used to perform large scale timetable based route searches on GTFS data. Depends on NetworkX (http://networkx.github.io/documentation/networkx-1.9.1/index.html) for shortest path searches in addition to other standard python modules, the search graph in generated is generic so it can be used with any other graph search library if desired.
