import jinja2
from jinja2 import nodes
from jinja2.ext import Extension

class CandleStickExtension(Extension):
    tags = set(['candlestick'])
    def __init__(self, environment):
        super(CandleStickExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            fragment_cache_prefix='',
            fragment_cache=None
        )

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        try:
            args = [parser.parse_expression()]
        except jinja2.exceptions.TemplateSyntaxError:
            args = ['']
        node = self.call_method('_render_candlestick', args)
        return jinja2.nodes.CallBlock(node, [], [], [], lineno=lineno)

    def _render_candlestick(self, stock='', *args, **kwargs):
        from app import index, draw
        if args == '':
            response = index()
        else:
            response = draw(stock)
        return jinja2.Markup(response)
