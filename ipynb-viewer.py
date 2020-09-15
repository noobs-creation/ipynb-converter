from nbconvert import HTMLExporter
from random import randint
import os
import sys
import nbformat
import tempfile
import webbrowser

tmpDir = tempfile.gettempdir()
ipynbDir = os.path.join(tmpDir, "ipynb-dir")
if not os.path.isdir(ipynbDir):
    os.mkdir(ipynbDir)


def create_html(fileName):
    while True:
        file_name = fileName.split(".")
        html_file = os.path.join(ipynbDir, file_name[0] + "-" + str(randint(45448, 58595859)) + ".html")
        if not os.path.exists(html_file):
            break
    nb = nbformat.read(fileName, as_version=4)
    html_exporter = HTMLExporter()
    # html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(nb)
    print(resources)
    with open(html_file, "w") as f:
        f.write(body)
        f.close()
    return html_file


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("""Usage: python ipynb-viewer.py [ipynb file]
            IPYNB (Jupyter Notebook) File Viewer
            Instantly view IPYNB (Jupyter Notebook) files directly on website.

            Additional arguments:
                -h, --help : shows this help message and quits""")
        else:
            nbfile = sys.argv[1]
            html_file = create_html(nbfile)
            w = webbrowser.open_new_tab(html_file)
    else:
        print("""Usage: python ipynb-viewer.py [ipynb file]
        IPYNB (Jupyter Notebook) File Viewer
        Instantly view IPYNB (Jupyter Notebook) files directly on website.

        Additional arguments:
            -h, --help : shows this help message and quits""")
