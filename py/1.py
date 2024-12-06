import re
import json

text = """
This is DIT | 2021 | DIT - Deggendorf Institute of Technology
Technische Hochschule Deggendorf
6.03K subscribers
Subscribe
762
Share
Download
Clip
Save
555K views  3 years ago
--
Visit the DIT online:

 …
...more
####################
15 Comments
Sort by
Add a comment...
@Abheshek5
2 years ago
This brings back Memories !!!!
2
Reply
@carolinekiai2631
4 months ago
18th July 2024, i got a letter of acceptance to study at your University. Am so happy and i can't wait to join in Oct. Thank you so much.
2
Reply
2 replies
@Shifan-Zi
2 years ago
is there programme for bsc optometry ?
1
Reply
·
2 replies
@elmehdielkhayati2742
3 years ago
Hello 
Please how can register in master management international
5
Reply
·
1 reply
@chiweolusamajah178
2 years ago
I love this.
I like to study it please can you help?
1
Reply
·
1 reply
@altaykaan
1 year ago
I dont want to say directly but i should warn incoming students. Firslty, location is not good, train connection is problematic. I think THD should have be in Plattling not in Deggendorf. Secondly, city is small so your parttime- minijob- werkstundet job opportunities are limited. Thirdly, so less students can able to finish mechanical or mechatronic departments.
Reply
·
1 reply
@shallow03
1 year ago
Your admission process is troubling. Admission requirements then Admission test.
I think there is no need for Admission test and unnecessary suffering.
2
Reply
"""

patterns = {
    "title": r"^(.*? \| .*?)$",
    "views_age": r"(\d+ views\s+\d+ \w+ ago)",
    "comments": r"^(@\w+)\n(\d+ weeks ago)\n(.*?)(?=Reply|$)",
}

data = {}

title_match = re.search(patterns["title"], text, re.MULTILINE)
data["title"] = title_match.group(1) if title_match else None


views_age_match = re.search(patterns["views_age"], text, re.MULTILINE)
if views_age_match:
    views, age = views_age_match.group(1).split(" views ")
    data["stats"] = {"views": int(views), "age": age.strip()}


comments = []
for match in re.finditer(patterns["comments"], text, re.MULTILINE | re.DOTALL):
    comments.append({
        "author": match.group(1),
        "time": match.group(2),
        "content": match.group(3).strip(),
    })
data["comments"] = comments

json_data = json.dumps(data, indent=4, ensure_ascii=False)

fileName = data['title']
#make sure the file name is valid
#replace all spaces with underscores

fileName = fileName.replace(" ", "_")
#re 
fileName = re.sub(r'[^\w\s_]', '', fileName)



# Save JSON string to a file
file_name = f"{fileName}.json"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(json_data)

print(f"JSON data has been saved to {file_name}")

