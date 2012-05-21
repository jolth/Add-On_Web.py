# -*- coding: UTF-8 -*-
"""
    Convierte una consulta a la base de datos en una 
    salida XML.
"""

__author__   = "Jorge A. Toro"
__version__  = "0.0.1"
__date__     = "21 may 2012"
__copyright  = "Copyright (c) 2012 Jorge A. Toro"
__license__  = "PSFL"


import xml.dom.minidom as XML


class dbToXML(object):
    def __init__(self, db, tables=(), cols=(), extend=None):
        """
            Realiza una consulta a la base de datos y
            la convierte en una fichero XML.

            sintax:
            dbToXML(inst_db, (codigo, name), (country, ))

            db = DB(None, {})
            dbToXML.dbToXML(db, ('pais',), ('codigo', 'descrip'))
            <0.0 (1): SELECT codigo, descrip FROM pais>

            Por el momento es recomendabla hacer una vista para 
            representar la tabla que queremos consultar.
        
        """
        self.db = db
        self.tables = ", ".join(tables)
        self.cols = ", ".join(cols)
        self.extendQuery = extend

        # Documento XML:
        self.xmldoc = XML.Document()
        # Etiqueta Raíz:
        self.root = self.xmldoc.createElement(self.tables) # Etiqueta raiz.
        self.xmldoc.appendChild(self.root) 

        self.table = db.query(self.__query())
    
        for row in self.table:
            self.toXML(row)


    def toXML(self, row):
        """
        """
        # Creamos la Etiqueta <content></content>
        content = self.xmldoc.createElement('content')
        self.root.appendChild(content)

        
        def g(k, v):
            element = self.xmldoc.createElement(k) 
            text = self.xmldoc.createTextNode(v)

            element.appendChild(text)
            content.appendChild(element)        

        [g(k, v) for k, v in row.items()[:]]
        

    def __query(self):
        """
            Por el momento el Query solo puede trabajar con
            Una sola tabla (en otras palabras no se pueden hacer
            JOIN).
        """
        return "SELECT " + self.cols + " FROM " + self.tables
