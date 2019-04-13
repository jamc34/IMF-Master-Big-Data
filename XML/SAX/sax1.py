import xml.sax
class ManejadorCatalogo (xml.sax.ContentHandler):
    def __init__(self):
            self.Datos=""
            self.titulo=""
            self.fecha=""
            self.autor=""

    def startElement(self,label,attr):
        self.Datos=label
        print('startElement:'+label);

    def endElement(self,label):
        print('endElement:'+label);


    def characters(self,label):
        print('characters:'+label);


parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=ManejadorCatalogo()
parser.setContentHandler(Handler)
parser.parse("ejemplo.xml")

