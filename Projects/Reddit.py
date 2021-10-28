import csv
import pandas
import json



def write_csv(data):
    with open('data.csv', 'w+') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        print(outf)
        return outf
            
x = """[
    {
        "pk": 22,
        "model": "auth.permission",
        "fields": {
            "codename": "add_logentry",
            "name": "Can add log entry",
            "content_type": 8
        }
    },
    {
        "pk": 23,
        "model": "auth.permission",
        "fields": {
            "codename": "change_logentry",
            "name": "Can change log entry",
            "content_type": 8
        }
    },
    {
        "pk": 24,
        "model": "auth.permission",
        "fields": {
            "codename": "delete_logentry",
            "name": "Can delete log entry",
            "content_type": 8
        }
    }
]"""
print(x)
write_csv(json.loads(x))



