#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Copyright (c) 2022 Abid Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import requests as req, re
from bs4 import BeautifulSoup as par
import rich as rich

__import__('os').system('git pull')

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses = req.Session()
ses.headers.update(headers)

class Main(object):
	
	def __init__(self,coki):
		self.coki = {"cookie":coki}
	def logo(self):
		logo = """

 _____ _               _               
/  ___| |             | |              
\ `--.| |__   __ _  __| | _____      __
 `--. \ '_ \ / _` |/ _` |/ _ \ \ /\ / /
/\__/ / | | | (_| | (_| | (_) \ V  V / 
\____/|_| |_|\__,_|\__,_|\___/ \_/\_/  
                                                                      
    Tools enable a2f Facebook, \x1b[0;92mv1.0.0\x1b[0;97m
	Developer: SHADOW HACKER, Team: BLACK_HAT
		"""
		return logo
	def cek(self):
		try:
			r = par(
				ses.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		except req.exceptions.TooManyRedirects:
			r = par(
				req.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		try:
			lanjut = r.find(
				"a",string="Use Authentication App"
			).get(
				"href"
			)
		except:
			exit(" ! your account is already installed a2f ×")
		try:
			__r = ses.get(lanjut,cookies=self.coki).text
		except req.exceptions.TooManyRedirects:
			__r = req.get(lanjut,cookies=self.coki).text
		co = par(__r, 'html.parser')
		try:
			kode = self.get_kode(co)
			print("\n * Key authen:",kode,"\n * Enter the authentic key in the authentic app  2 faktor!\n")
		except:
			if "For security, please re-enter your password to continue." in __r:
				print(" * For security, please enter your Facebook password to continue.")
				sandi = input(" + Password facebook: ")
				lanjut = co.find(
					'form',{
						'method':'post'
					}
				)
				memek = {}
				lst = ["fb_dtsg","jazoest","save"]
				for x in lanjut:
					if x.get("name") in lst:
						memek.update(
							{
								x.get(
									"name"
								):x.get(
									"value"
								)
							}
						)
				memek.update(
					{
						"pass":sandi
					}
				)
				response = ses.post(
					lanjut.get(
						"action"
					),cookies=self.coki,data=memek
				).text
				if "The password you entered is not correct." in response:
					exit(" ! The password you entered is not correct.")
				else:
					try:
						kode = self.get_kode(response)
					except IndexError:
						exit(" × Facebook Caught checkpoint")
				print("\n * Key authen:",kode,"\n * Enter the authentic key in the authentic app 2 factor!\n")
			else:
				exit(" × Facebook Caught checkpoint")
		self.masuk(co)
	
	def spam(self,cokii):
		print(" ! To avoid the checkpoint tools will delete comments on the author's post as much as  14 spam.\n * The process is running please wait...\n")
		sp.Main(
			cokii
		).gasken(
			14,"Ravi Handsom:v"
		)

class Pasang(Main):
	
	def pasang(self,link,data_code):
		return ses.post(
			"https://mbasic.facebook.com"+str(
				link
			),data=data_code,cookies=self.coki
		).text
	def get_kode(self,res):
		kode = re.findall(
			'\<div\ class\=\".*?\"\>Or enter this code into your authentication app<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(
				res
			)
		)[0]
		return kode
	def kode_pemulihan(self,kontol):
		num = 0
		for x in kontol.find_all('span'):
			if(
				re.findall(
					'\d+\s\d+',str(
						x
					)
				)
			):
				num+=1
				if(num==1):
					print(f" \_> {x.text}")
				else:
					print(f" |_> {x.text}")
	def get_kode_pemulihan(self):
		waifu_wangy = {
			"Host":"mbasic.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type":"application/x-www-form-urlencoded",
			"origin":"https://www.facebook.com",
			"referer":"https://www.facebook.com",
			"upgrade-insecure-requests":"2",
			"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
		}
		ses.headers.update(waifu_wangy)
		__res = ses.get("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki).text
		kontol = par(__res, 'html.parser')
		if "Use the recovery code to log in if you lose your phone or can't receive the verification code via text message or authentication app." in __res:
			data = {}
			lst = ["fb_dtsg","jazoest","reset"]
			for x in kontol.find(
				'form',{
					'method':'post'
				}
			):
				if x.get('name') in lst:
					data.update(
						{x.get(
							'name'
						):x.get(
							'value'
						)
					}
				)
			data.update(
				{
					"":"Get Code"
				}
			)
			kontol = par(
				ses.post(
					"https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki,data=data
				).text, 'html.parser'
			)
			self.kode_pemulihan(kontol)
		else:
			self.kode_pemulihan(kontol)
	def masuk(self,co):
		data = {}
		masuk = input(" + input code authen: ")
		lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
		lanjut = co.find(
			'form',{
				'method':'post'
			}
		)
		for x in lanjut:
			if x.get('name') in lst:
				data.update(
					{x.get(
						'name'
					):x.get(
						'value'
					)
				}
			)	
		data.update(
			{
				'confirmButton':'Lanjutkan'
			}
		)
		res = par(
			ses.post(
				'https://mbasic.facebook.com'+str(
					lanjut.get(
						"action"
					)
				),cookies=self.coki,data=data
			).text, 'html.parser'
		)
		data.clear()
		lanjut = res.find(
			"form",{
				"id":"input_form"
			}
		)
		lst = ["fb_dtsg","jazoest"]
		for x in lanjut:
			if x.get("name") in lst:
				data.update(
					{x.get(
						"name"
					):x.get(
						"value"
					)
				}
			)
		data.update({
			"code":masuk,
			"submit_code_button":"Lanjutkan"
		})
		response = self.pasang(
			lanjut.get(
				"action"
			),data
		)
		if "checkpoint" in response:
			exit(" × Account ops exposed checkpoint")
		elif "Active Two-Factor Authentication " in response:
			print(" √ a2f Installed successfully ^^")
			print(" * Recovery code: ")
			self.get_Recovery_code()
		else:
			print(" ! Text:",response)
			exit(" × Something went wrong in the script, try reporting it to the developer. Copy text on! Send to wa 03425081910. ")

__import__('os').system('clear')

if __name__=="__main__":
	print(
		Pasang(
			""
		).logo(
		)
	)
	cokii = input(" + Get cookie: ")
	resss = req.get(
		"https://mbasic.facebook.com/profile.php",cookies={
			"cookie":cokii
		}
	).text
	if "mbasic_logout_button" in resss:
		nama = re.findall(
			'\<title\>(.*?)<\/title\>',str(
				resss
			)
		)[0]
		print(f' √ Cookies accept\n ^ Welcome {nama}\n')
		menuju = Pasang(cokii)
		menuju.spam(cokii)
		menuju.cek()
	else:
		exit(" × Cookies invalid")
