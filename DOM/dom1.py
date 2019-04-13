from xml.dom.minidom import parse
import xml.dom.minidom

ArbolDOM=xml.dom.minidom.parse("ejemplo.xml")
catalogo=ArbolDOM.documentElement
libros=catalogo.getElementsByTagName("libro")
for libro in libros:
    if libro.hasAttribute("at"):
        print("Attribute at = ", libro.getAttribute("at"))
    titulo = libro.getElementsByTagName("titulo")[0]
    print ("Titulo: ", titulo.childNodes[0].data);
