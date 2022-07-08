# -*- coding: utf-8 -*-
import dash

app = dash.Dash("enzus", suppress_callback_exceptions=True)
app.title = 'Analytics'
app.scripts.config.serve_locally = True

