import os, re, zipfile


def rename(sub, vid):
	try:
		os.rename(f'{p}\\{sub[0]}', re.findall(r'.*\.', vid[0])[0] + "srt")
	except:
		pass


def r(item):
	return (item, list(map(int,re.findall(r'\d{1,3}', re.findall(r'\d{1,3}\D\d{1,3}', item)[0]))))


p = os.getcwd()
vids = []

for item in os.listdir(p):
	if item.endswith('.zip'):
		file_name = os.path.abspath(item)
		with zipfile.ZipFile(file_name, 'r') as z:
			z.extractall(p)
		os.remove(file_name)
	elif not (item.endswith('.py') or item.endswith('.srt')):
		vids.append(item)

subtitles = [r(item) for item in os.listdir(p) if item.endswith('.srt')]

videos = [r(item) for item in vids]

for vid in videos:
	for sub in subtitles:
		if vid[1] == sub[1]:
			rename(sub, vid)
