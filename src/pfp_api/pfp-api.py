#from asyncore import read
import json
import sys
import warnings
import time
import logging
import json
import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper

# load()
# from .load_for_real import load
from .load import  read
from .stages import bit_stomach ,can_smasher,think_pudding,mod_collector,esteemer

warnings.filterwarnings("ignore")
# TODO: process command line args if using graph_from_file()
# Read graph and convert to dataframe
start_time = time.time()
graph_read = read(sys.argv[1])
bs_graph = bit_stomach(graph_read)
cs_graph = can_smasher(bs_graph)
tp_graph = think_pudding(cs_graph)
mc_graph = mod_collector(tp_graph)
es_graph = esteemer(mc_graph)


print(es_graph.serialize(format='json-ld', indent=4))
