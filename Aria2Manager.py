# -*- coding: utf-8 -*-
#
# <A PySide Gui for Aria2 Download Manager>
# Copyright (C) 2013  a.atalla <a.atalla@hacari.org>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

import os
import psutil
import signal
import subprocess
import xmlrpclib as rpc
import pprint as p

HOME_DIR = os.environ['HOME']
CONFIG_DIR= HOME_DIR+'/.barq'   # You can change the dir name as you want 

class Aria2Manager:
	
	def __init__(self):

		self._PID = self.get_PID()
		self.connection=rpc.ServerProxy('http://localhost:6800/rpc')
		if self.isRunning():
			print 'Aria2  is Running with PID = ',self._PID
			
	def get_PID(self):
		###
		# return the system PID for 'aria2c'  process
		###
		proc_list = psutil.get_process_list()
		for proc in proc_list:
			if proc.name == 'aria2c':
				return proc.pid
		return None
		
	def isRunning(self):
		if self.get_PID()==None:
			return False
		return True
		

	def startAria2(self):
		args = ['aria2c','-D','--enable-rpc','--continue=true']
		if os.path.exists(CONFIG_DIR+'/session.ini'):
			print CONFIG_DIR,'is exist'
			args.append('--input-file='+CONFIG_DIR+'/session.ini')
		else:
			if not os.path.exists(CONFIG_DIR):
				print 'create config folder'
				os.mkdir(CONFIG_DIR)
		args.append('--save-session='+CONFIG_DIR+'/session.ini')
		args.append('--save-session-interval=30')
		args.append('--always-resume=true')
		print (args)
		subprocess.call(args)
		self._PID = self.get_PID()
		
	
	def stopAria2(self):
		if self.isRunning():
			print 'Aria2 will shutdown ===> ',self._PID
			#self.connection.aria2.forceShutdown()
			os.system("killall aria2c")
			
			#proc = psutil.Process(self._PID)    Those 2 lines are a cleaner way to kill aria2c orocess
			#proc.send_signal(signal.SIGKILL)    but for unknown reason it doesnot save-session        
			
	def addUris(self,uris,params):
		'''
		Start new download by adding new uri/uris with options 
		uris: is a list (one or more ) uri for the downloaded file
		params: Dictionary of the download options such as (max-download-limit,max-connection-per-server,.....etc)
		'''
		self.connection.aria2.addUri(uris,params)
		
	def getGlobalStatus(self):
		return self.connection.aria2.getGlobalStat()
		
	def getAllGids(self):
		active  = self.connection.aria2.tellActive(['gid'])
		waiting = self.connection.aria2.tellWaiting(0,100,['gid'])
		stopped = self.connection.aria2.tellStopped(0,100,['gid'])
		allGids = [active,waiting,stopped]  # This is a list of 3 lists
		return allGids
	
	def getOptions(self,gid):
		return self.connection.aria2.getOption(gid)
		
	def changeGlobalOption(self,options):
		'''
		option is of type dictionary for example: {'max-overall-download-limit':'20K'}
		Avaliable globalOption in aria2:
		
		download-result
		log
		log-level
		max-concurrent-downloads
		max-download-result
		max-overall-download-limit
		max-overall-upload-limit
		save-cookies
		save-session
		server-stat-of
		'''
		self.connection.aria2.changeGlobalOption(options)
		
	def changeOption(self,gid,options):
		'''
		available options to be changed
		bt-max-peers
		bt-request-peer-speed-limit
		bt-remove-unselected-file
		force-save
		max-download-limit
		max-upload-limit
		'''
		self.connection.aria2.changeOption(gid,options)

	def  pauseAllDownloads(self):
		self.connection.aria2.forcePauseAll()
		
	def unpauseAllDownloads(self):
		self.connection.aria2.unpauseAll()
		
	def pauseSingleDownload(self,gid):
		self.connection.aria2.pause(gid)
		
	def unpauseSingleDownload(self,gid):
		self.connection.aria2.unpause(gid)
		
	def removeSingleDownload(self,gid):
		self.connection.aria2.remove(gid)
		
	def cleanDownloadList(self):
		self.connection.aria2.purgeDownloadResult()
		
	def getDownloadStatus(self,gid):
		data = self.connection.aria2.tellStatus(gid)
		gid = data.get('gid')
		filename = os.path.split(data.get('files')[0].get('path'))[1]
		status = data.get('status')
		size = data.get('totalLength')          # Total File Size
		dsize = data.get('completedLength')   # The Completed Size
		speed = data.get('downloadSpeed')
		return [gid, filename, status, size, dsize, speed]
	 
	def getDownloadDetail(self,gid,detail):
		status = self.connection.aria2.tellStatus(gid)
		detail_value = status.get(detail)
		return detail_value
		
	def getUrisDetails(self,gid):
		status  = self.connection.aria2.tellStatus(gid)
		p.pprint (status)
		return status.get('files')[0].get('uris')