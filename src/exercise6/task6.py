import json

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, 'input.txt')) as f:
    content = f.read().strip()

if not content:
    print("Empty file")
else:
    try:
        data = json.loads(content)
        if 'list1' not in data or 'list2' not in data:
            raise ValueError("Missing list1 or list2")

        l1 = data['list1']
        l2 = data['list2']

        merged = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i]['year'] <= l2[j]['year']:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        merged.extend(l1[i:])
        merged.extend(l2[j:])

        print(json.dumps({"list0": merged}, indent=2))
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"Invalid input: {e}")
