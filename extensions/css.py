import jinja2
from jinja2 import nodes
from jinja2.ext import Extension
from flask import render_template


class ImportCSSExtension(Extension):
    tags = set(['import_css'])
    def __init__(self, environment):
        super(ImportCSSExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            fragment_cache_prefix='',
            fragment_cache=None
        )

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        node = self.call_method('_render_candlestick')
        return jinja2.nodes.CallBlock(node, [], [], [], lineno=lineno)

    def _render_candlestick(self, stock='', *args, **kwargs):
        return render_template('css.html')
