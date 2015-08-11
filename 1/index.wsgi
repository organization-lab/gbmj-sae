from bottle import Bottle, run, request, template

import mahjong
import sae

app = Bottle()

@app.route('/')
def hello():
    return "Guobiaomajiang - Organzation Laboratory"

@app.route('/hand')
def hand():
    return '''
        <form action="/handcal" method="post">
            Hand: <input name="hand" type="text" />
            <input value="Calculate" type="submit" />
        </form>
    '''

@app.route('/handcal', method='POST')
def do_hand():
    hand = request.forms.get('hand')
    print(hand) # check input
    return_list = mahjong.xiangtingshu_output(hand)
    if return_list:
        return template('mahjong.tpl', hand=hand, basket=return_list)
    else:
        return "<p>hand failed.</p>"

def check_hand(hand):
    return mahjong.xiangtingshu_output(hand)

application = sae.create_wsgi_app(app)