import json
import os

transcript_path = r'C:\Users\HP\.gemini\antigravity\brain\369aa8a3-f317-4d9f-a5a7-2b4fdbcdaed2\.system_generated\logs\transcript_full.jsonl'
output_path = r'src\views\Home.vue'

home_content = None

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line.strip())
            if 'tool_calls' in data:
                for call in data['tool_calls']:
                    if call['function']['name'] == 'default_api:write_to_file':
                        args = json.loads(call['function']['arguments'])
                        if 'Home.vue' in args.get('TargetFile', ''):
                            home_content = args['CodeContent']
        except Exception as e:
            pass

if home_content:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(home_content)
    print("RESTORED HOME.VUE SUCCESSFULLY")
else:
    print("COULD NOT FIND HOME.VUE CONTENT")
