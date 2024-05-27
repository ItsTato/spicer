from re import findall
from flask import Flask
from os import path

class Spicer:
	def __init__(self,app:Flask) -> None:
		self.__app:Flask = app
	
	def patch(self,rendered:str) -> str:
		"""
		Patch up an already-rendered template using Spicer.

		:param rendered: The rendered template
		"""

		pattern:str = r"&<([^>]+)>"
		constants:list[str] = findall(pattern,rendered)

		for constant in constants:
			pass#continue working later

		return ""