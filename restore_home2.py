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
                    target = args.get('TargetFile', '')
                    if 'Home.vue' in target:
                        print(call['function']['name'])
                        if call['function']['name'] == 'default_api:write_to_file':
                            print(args.keys())
                            if 'CodeContent' in args:
                                with open('src/views/Home.vue', 'w', encoding='utf-8') as out:
                                    out.write(args['CodeContent'])
                                print("RESTORED HOME.VUE!")
                        elif call['function']['name'] == 'default_api:replace_file_content':
                            pass
        except Exception as e:
            pass
