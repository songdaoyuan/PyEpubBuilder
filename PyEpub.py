# -*- coding: utf-8 -*-
'''
要成功运行此程序 需要在程序目录下放置
coverpage.html
chapter1.html
...
chapterx.html
cover.jpg (可选，作品封面)
images (可选，作品插画)
'''
import os
import shutil
import zipfile

title = ''		#书名
creator = ''		#作者
description = ''		#作品描述

htmllist = ['coverpage.html', 'chapter1.html', 'chapter2.html', 'chapter3.html', 'chapter4.html', 'chapter5.html', 'chapter6.html', 'chapter7.html', 'chapter8.html', 'chapter9.html', 'chapter10.html']		#作品章节列表
if not os.path.exists(title):
	os.mkdir(title)

with open(title + '/mimetupe', 'w') as f:
	f.write('application/epub+zip')

if not os.path.exists(title + '/META-INF'):
	os.mkdir(title + '/META-INF')

with open(title + '/META-INF/container.xml', 'w') as f:
	f.write('''<?xml version="1.0" encoding="UTF-8" ?>
	<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
   		<rootfiles>
	    	<rootfile full-path="OPS/content.opf" media-type="application/oebps-package+xml"/> 
		</rootfiles>
	</container>
	''')

if not os.path.exists(title + '/OPS'):
	os.mkdir(title + '/OPS')

if not os.path.exists(title + '/OPS/css'):
	os.mkdir(title + '/OPS/css')

with open(title + '/OPS/css/main.css', 'w') as f:
	f.write('''@font-face {
	font-family:"cnepub";
	src:url(res:///opt/sony/ebook/FONT/tt0011m_.ttf), url(res:///tt0011m_.ttf);
	}
	body {
		padding: 0%;
		margin-top: 0%;
		margin-bottom: 0%;
		margin-left: 1%;
		margin-right: 1%;
		line-height:130%;
		text-align: justify;
		font-family:"cnepub", serif;
	}
	div {
		margin:0px;
		padding:0px;
		line-height:130%;
		text-align: justify;
		font-family:"cnepub", serif;
	}
	p {
		text-align: justify;
		text-indent: 2em;
		line-height:130%;
	}
	.cover {
		width:100%;
		padding:0px;
	}
	.center {
		text-align: center;
		margin-left: 0%;
		margin-right: 0%;
	}
	.left {
		text-align: center;
		margin-left: 0%;
		margin-right: 0%;
	}
	.right {
		text-align: right;
		margin-left: 0%;
		margin-right: 0%;
	}
	.quote {
		margin-top: 0%;
		margin-bottom: 0%;
		margin-left: 1em;
		margin-right: 1em;
		text-align: justify;
		font-family:"cnepub", serif;
	}
	h1 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:xx-large;
	}
	h2 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:x-large;
	}
	h3 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:large;
	}
	h4 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:medium;
	}
	h5 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:small;
	}
	h6 {
		line-height:130%;
		text-align: center;
		font-weight:bold;
		font-size:x-small;
	}
	''')

if not os.path.exists(title + '/OPS/images'):		#用于放置轻小说的插画和封面
	os.mkdir(title + '/OPS/images')

if os.path.isfile('cover.jpg'):
	shutil.copy('cover.jpg', title + '/OPS/images/cover.jpg')
	print('封面已添加！')

if os.path.isdir('images'):
	for dirpath, dirnames, filenames in os.walk(os.getcwd() + '/images'):
		for filepath in filenames:
			shutil.copy(os.path.join(dirpath, filepath), title + '/OPS/images/')
	print('插画已添加！')

opfcontent = '''<?xml version="1.0" encoding="UTF-8" ?>
<package version="2.0" unique-identifier="PrimaryID" xmlns="http://www.idpf.org/2007/opf">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
%(metadata)s
<dc:language>zh-CN</dc:language>
<meta name="cover" content="cover"/>
<dc:builder>PyEpubBuilder</dc:builder>
<dc:builder_version>0.0.0.1</dc:builder_version>
</metadata>
<manifest>
%(manifest)s
<item id="ncx" href="content.ncx" media-type="application/x-dtbncx+xml"/>
<item id="cover" href="images/cover.jpg" media-type="image/jpeg"/>
</manifest>
<spine toc="ncx">
%(ncx)s
</spine>
</package>
'''
dc = '<dc:%(name)s>%(value)s</dc:%(name)s>'
item = "<item id='%(id)s' href='%(url)s' media-type='application/xhtml+xml'/>"
itemref = "<itemref idref='%(id)s'/>"

metadata = '\n'.join([
        dc % {'name': 'title', 'value': title},
        dc % {'name': 'creator', 'value': creator},
        dc % {'name': 'description', 'value': description},
        ])

manifest = []
ncx = []

for htmlitem in htmllist:
	shutil.copy(htmlitem, title + '/OPS/' + htmlitem)
	manifest.append(item % {'id': htmlitem, 'url': htmlitem})
	ncx.append(itemref % {'id': htmlitem})

manifest='\n'.join(manifest)
ncx='\n'.join(ncx)

with open(title + '/OPS/content.opf', 'w', encoding = 'utf-8') as f:
	f.write(opfcontent %{'metadata': metadata, 'manifest': manifest, 'ncx': ncx,})

ncx ='''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx version="2005-1" xmlns="http://www.daisy.org/z3986/2005/ncx/">
<head>
  <meta name="dtb:uid" content=" "/>
  <meta name="dtb:depth" content="-1"/>
  <meta name="dtb:totalPageCount" content="0"/>
  <meta name="dtb:maxPageNumber" content="0"/>
</head>
 <docTitle><text>%(title)s</text></docTitle>
 <docAuthor><text>%(creator)s</text></docAuthor>
<navMap>
%(navpoints)s
</navMap>
</ncx>
'''

navpoint = '''<navPoint id='%s' class='level1' playOrder='%d'>
<navLabel> <text>%s</text> </navLabel>
<content src='%s'/></navPoint>''' #这两个不应该使用同一指代

navpoints = []
for i, htmlitem in enumerate(htmllist):
    navpoints.append(navpoint % (htmlitem, i+1, htmlitem, htmlitem))

with open(title + '/OPS/content.ncx', 'w', encoding = 'utf-8') as f:
	f.write(ncx % {
    	'title': title,
    	'creator': creator,
    	'navpoints': '\n'.join(navpoints)})

epubfile = zipfile.ZipFile(title + '.epub', 'w')
os.chdir(title)
for dirpath, dirnames, filenames in os.walk('.'):
    for filepath in filenames:
        epubfile.write(os.path.join(dirpath, filepath))
epubfile.close()
# shutil.rmtree('../' + title)
print("Done")