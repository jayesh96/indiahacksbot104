
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username='4a18750e-dcaa-46ab-8f1f-77f22e8885d9',
  password='UBIYKIyZJztG',
  version='2017-05-26'
)

# Replace with the context obtained from the initial request

def check_intent(msg):
	context = {
		'conversation_id': '1b7b67c0-90ed-45dc-8508-9488bc483d5b'
	}

	workspace_id = '2fa8fe14-c4da-4759-8e12-aa6e067b9322'

	response = conversation.message(
  	workspace_id=workspace_id,
  	message_input={'text': msg},
  	context=context
	)

	print(json.dumps(response, indent=2))

	text=(response['output']['text'][0])
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	print text
	return text