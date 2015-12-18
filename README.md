# gtfs-route-server
Build Time Expanded Search Graphs Using GTFS Data

<p class=MsoNormal>Contributors: Chetan Joshi, Portland OR<o:p></o:p></p>

<p class=MsoNormal>Requires: Python with standard modules and <span
class=SpellE>networkx</span><o:p></o:p></p>

<p class=MsoNormal>Tested with: GTFS data from <span class=SpellE>psrc</span>
consolidated file and <span class=SpellE>trimet</span><o:p></o:p></p>

<p class=MsoNormal>License: The MIT License (MIT)<o:p></o:p></p>

<p class=MsoNormal>License URI: https://opensource.org/licenses/MIT<o:p></o:p></p>

<p class=MsoNormal>Description: Generates a search graph as edge list that may
be used to perform large scale timetable based route searches on GTFS data.
Depends on <span class=SpellE>NetworkX</span>
(http://networkx.github.io/documentation/networkx-1.9.1/index.html) for
shortest path searches in addition to other standard python modules, the search
graph in generated is generic so it can be used with any other graph search
library if desired.</p>
