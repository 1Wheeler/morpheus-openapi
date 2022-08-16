master_doc = 'index'

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.openapi','M2R2']

"""Patching m2r2"""
import m2r2

current_m2r2_setup = m2r2.setup

def patched_m2r2_setup(app):
    try:
        return current_m2r2_setup(app)
    except (AttributeError):
        app.add_source_suffix(".md", ".rst", "markdown")
        app.add_source_parser(m2r2.M2RParser)
    return dict(
        version=m2r2.__version__, parallel_read_safe=True, parallel_write_safe=True,
    )

m2r2.setup = patched_m2r2_setup

source_suffix = ['.rst', '.md']