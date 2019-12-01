import math

class NTC10kOhm:

    def ThermistorCal(self, value):
	"""
	Steinhart-Hart equation
	R1  T1
	22021  5
	10000  25
	4917  45
	"""
	A=0.9017477480e-3
	B=2.489190310e-4
	C=2.043213857e-7

	R=self.ResisCal(value)

	T=1.0/(A+B*math.log(R)+C*pow(math.log(R),3))-273

	return T

    def VoltageCal(self, value):
	V=value/1024.0*3.3
	return V

    def ResisCal(self, value):
	V=self.VoltageCal(value)
	if V>0.1 and V<3.2:
	    R=12000*(3.3-V)/V
	else:
	    R=1
	return R


