# -*- coding: utf-8 -*-
import kivy

#Program coded by: Ian McDowell

#gives python access to all needed kivy features
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
import math

#making the window maximized on start
Config.set('graphics', 'window_state', 'maximized')
#allowing input and mouse but disabling multitouch
Config.set("input", "mouse", "mouse, disable_multitouch")

#checks if a certain input is a number
def IsNum(lis):
	for x in lis:
		try:
			float(str(x))
			a = True
		except:
			a = False
			break
	return a

#checks if an input field is blank
def IsBlank(lis):
	a = True
	for x in lis:
		if len(x) == 0:
			a = False
			break
	return a

#  ~(-*-)~

class QuadraticsLayout(FloatLayout):

		def calculate(self, entry1, entry2, entry3, abcform, quadform, standform, standconform, vert, foc, yint, aos, dire, rel, rellb):
			#Loads inputs
			str_float1 = entry1.text
			str_float2 = entry2.text
			str_float3 = entry3.text

			#Makes sure inputs are valid and shows an appropriate popup error message if the inputs are invalid
			if IsBlank([str_float1]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Please input a number for A.'), 
							size_hint = (.35, .35))
				popup.open()
			elif str_float1 == "0":
				popup = Popup(title = 'Input Error',
						content = Label(text='A cannot be 0.\nPlease input a new number for A.'), 
						size_hint = (.35, .35))
				popup.open()
			elif IsNum([str_float1]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for A.'), 
							size_hint = (.35, .35))
				popup.open()
			elif str_float1 == "NaN":
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for A.'), 
							size_hint = (.35, .35))
				popup.open()
			elif IsBlank([str_float2]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Please input a number for B.'), 
							size_hint = (.35, .35))
				popup.open()
			elif IsNum([str_float2]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for B.'), 
							size_hint = (.35, .35))	
				popup.open()
			elif str_float2 == "NaN":
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for B.'), 
							size_hint = (.35, .35))
				popup.open()
			elif IsBlank([str_float3]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Please input a number for C.'), 
							size_hint = (.35, .35))
				popup.open()
			elif IsNum([str_float3]) == False:
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for C.'), 
							size_hint = (.35, .35))	
				popup.open()
			elif str_float3 == "NaN":
				popup = Popup(title = 'Input Error',
							content = Label(text='Inputs must be numbers.\nPlease input a number for C.'), 
							size_hint = (.35, .35))
				popup.open()
			else:
			#Converts inputs into numbers
				A = float(str_float1)
				B = float(str_float2)
				C = float(str_float3)
			#Calculates needed values
				D = (B / (2 * A)) #x-coordinate of vertex
				E = (A * (D) ** 2 + (B * (D)) + (C)) #y-coordinate of vertex
				P = ((1 / A) / 4) #half distance from focus to directrix 
			#Standard Form
				try:
					abcform.text = "Y = " + str(A) + "X² + " + str(B) + "X + " + str(C)
				except Exception:
					abcform.text = "Error"		
			#Quadratic Form
				if ((B ** 2) - (4 * A * C)) < 0:
					if isinstance(math.sqrt((-1 * ((B ** 2) - (4 * A * C)))), int):
						try:
							quadform.text = "     " + "-" + str(B) + " " + "±" + str(math.sqrt(-1 * ((B ** 2) - (4 * A * C)))) + "i" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A)
						except Exception:
							quadform.text = "Error"
					else:
						try:
							quadform.text = "     " + "-" + str(B) + " " + "±" + "√(" + str((-1 * ((B ** 2) - (4 * A * C)))) + ")" + "i" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A)
						except Exception:
							quadform.text = "Error"
				else:
					if isinstance(math.sqrt(((B ** 2) - (4 * A * C))), int):
						try:
							quadform.text = "     " + "-" + str(B) + " " + "±" + str( math.sqrt((B ** 2) - (4 * A * C))) + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A)
						except Exception:
							quadform.text = "Error"	
					else:
						try:
							quadform.text = "     " + "-" + str(B) + " " + "±" + "√(" + str(((B ** 2) - (4 * A * C))) + ")" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A)
						except Exception:
							quadform.text = "Error"
			#Standard Form
				try:
					standform.text = "Y = " + str(A) + "(X + " + str(B / 2 * A) + ")" + "² + " + str(C - (B ** 2 / (4 * A )))
				except Exception:
					standform.display.text = "Error"
			#Standard Conic Form
				try:
					standconform.text = "(x - " + str(D) + ")² = 4*" + str(P) + "(y - " + str(E) + ")"
				except Exception:
					standconform.display.text = "Error"
			#Vertex
				try:
					vert.text = "(" + str(D) + "," + str(E) + ")"
				except Exception:
					vert.text = "Error"
			#Focus
				try:
					foc.text = "(" + str(D) + "," + str(E + P) + ")"
				except Exception:
					foc.text = "Error"
			#Y-Intercept
				try:
					yint.text = "(" + "0" + "," + str(C) + ")"
				except Exception:
					yint.text = "Error"
			#Axis of Symmetry
				try:
					aos.text = "X = " + str(D)
				except Exception:
					aos.text = "Error"
			#Directrix
				try:
					dire.text = "Y = " + str(E - P)
				except Exception:
					dire.text = "Error"
			#Relative Min/Max
				if A < 0:
					try:
						rel.text = "Y = " + str(E)
						rellb.text = "Relative Maximum"
					except Exception:
						rel.text = "Error"
				else:
					try:
						rel.text = "Y = " + str(E)
						rellb.text = "Relative Minimum"
					except Exception:
						rel.text = "Error"

#runs the program with kivy
class QuadraticsApp(App):

	def build(self):
		return QuadraticsLayout()

quadApp = QuadraticsApp()
quadApp.run()