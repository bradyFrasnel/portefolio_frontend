import json

transcript_path = r'C:\Users\HP\.gemini\antigravity\brain\369aa8a3-f317-4d9f-a5a7-2b4fdbcdaed2\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line.strip())
            if 'tool_calls' in data:
                for call in data['tool_calls']:
                    args_str = call['function'].get('arguments', '{}')
                    args = json.loads(args_str)
                    print(call['function']['name'], args.get('TargetFile', ''))
                    if 'Home.vue' in args.get('TargetFile', ''):
                        with open('src/views/Home.vue', 'w', encoding='utf-8') as out:
                            if 'CodeContent' in args:
                                out.write(args['CodeContent'])
                            elif 'ReplacementContent' in args:
                                # It was a replace, I can't just extract it directly if there are multiple.
                                print("IT WAS REPLACE", args.keys())
        except Exception as e:
            pass
