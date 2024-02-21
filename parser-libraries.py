import os
import fnmatch
import hashlib
import json


for path,dirs,files in os.walk('.'):
    for file in files:
        if fnmatch.fnmatch(file,'*.jar'):
            fullname = os.path.join(path,file)
            newPath = fullname.replace(os.sep, '/').lstrip('./')
            sha1 = hashlib.sha1(open(fullname,'rb').read()).hexdigest()
            data = {
                "path": newPath,
                "sha1": sha1,
                "type": "library"
            }
            with open("libraries.json", "a") as f:
                f.write(f'{json.dumps(data, indent=4, skipkeys=True)},\n')
            print(newPath)
            print(sha1)
