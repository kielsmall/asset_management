# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document


print("start")
class AssetTable(Document):
	count=0
	
	print "in class assettable"
	
	def validate(self):
			"""tab=AssetTable.my_serialno.append(self)"""
			"""print "tab=",tab"""
			print("in setup-method")
			print "before validate"
			print "steup----"
			print("in Validate function")
			privious_assign_details=frappe.get_list("Asset Table",fields=["serial_no","item_name"],filters={"serial_no":("=",self.serial_no)})
			if privious_assign_details:
					frappe.throw(_("Item {0} with serial no {1} already assigned to employee").format(self.item_name,self.serial_no))
			print "self.serial_no",self.serial_no
			print "assign_details=",privious_assign_details
			print("Middle")
     	 		
			"""print my_serialno.append(AssetTable(0))
			for n in range(100):
				x=AssetTable(Document)
				print my_serialno.append(x)
			for m in my_serialno:
				print m.serial_no"""
				
			for i in privious_assign_details:
				print "*****************"
				print i.serial_no
				if i.serial_no==self.serial_no:	
					print "matched"
					frappe.throw(_("Item {0} with serial no {1} already assigned to employee").format(self.item_name,self.serial_no))
				

		
	
my_serialno=[]
	
print("Finish")
