from bottle import route, run, request, abort, static_file

from fsm import TocMachine
import os

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
machine = TocMachine(
    states=[
        'user',
        'eat',
        'search',
        'fastfood',
    	'fried',
    	'nonfried',
    	'food',
    	'expensive',
    	'cheap',
        'google',
	'demo'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'eat',
            'conditions': 'is_going_to_eat'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'fried',
            'conditions': 'is_going_to_fried'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'cheap',
            'conditions': 'is_going_to_cheap'
        }, 
        {
            'trigger': 'advance',
            'source': 'eat',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'google',
            'conditions': 'is_going_to_google'
        },
        {
            'trigger': 'advance',
            'source': 'eat',
            'dest': 'fastfood',
            'conditions': 'is_going_to_fastfood'
        },
        {
            'triiger':'advance',
            'source':'demo',
            'dest':'demo',
            'conditions':'is_going_to_demo'
        },
	{
	    'trigger': 'advance',
            'source': 'fastfood',
            'dest': 'fried',
            'conditions': 'is_going_to_fried'
	},
	{
	    'trigger': 'advance',
            'source': 'fastfood',
            'dest': 'nonfried',
            'conditions': 'is_going_to_nonfried'
	},
	{
	    'trigger': 'advance',
            'source': 'eat',
            'dest': 'food',
            'conditions': 'is_going_to_food'
	},
	{
	    'trigger': 'advance',
            'source': 'food',
            'dest': 'expensive',
            'conditions': 'is_going_to_expensive'
    	},
	{
	    'trigger': 'advance',
            'source': 'food',
            'dest': 'cheap',
            'conditions': 'is_going_to_cheap'
	},
	{
            'trigger': 'go_back',
            'source': [
                'google',
		'fried',
		'nonfried',
		'expensive',
		'cheap'
		    ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=os.environ['PORT'], debug=True, reloader=True)

