#coding=utf-8
import codecs
import  xml.dom.minidom

DPR = 1.5

#open xml document
dom = xml.dom.minidom.parse('dimens.xml')
root = dom.documentElement
nodes = root.getElementsByTagName("dimen")

for node in nodes:
	nodename = node.getAttribute('name')
	nodevalue = node.childNodes[0].nodeValue
	if nodevalue.endswith('dp'):
		num = nodevalue.replace('dp', '')
		node.childNodes[0].nodeValue = str(int(round(float(num)/DPR))) + 'dp'

newfile = codecs.open('new_dimens.xml', 'w', 'utf-8')
dom.writexml(newfile, encoding='utf-8')
