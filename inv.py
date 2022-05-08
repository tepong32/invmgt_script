import datetime

class Instance: 
	# name should be a 4-digit, numeric string (mmdd format): 0501 == May 01
	def __init__(self, name, at_price):
		self.name = name
		self.at_price = at_price
		# for getting the current year
		# see https://www.w3schools.com/python/python_datetime.asp for reference
		current_date = datetime.datetime.now()
		self.month = self.name[:2]
		self.date = self.name[2:]
		self.year = current_date.strftime("%Y")

		# separate computations of 11kg and 2.7kg (sk) tanks
		self.kg11_capital = float(self.at_price) * 11
		self.kg11_srp = float(self.kg11_capital) * 1.2
		self.sk_capital = float(self.at_price) * 2.7
		self.sk_srp = float(self.sk_capital) * 1.4
		
		# converting the class attibutes to strings so they can be concatinated into sentences/paragraphs
		return print("Date: " + str(self.year) + ", " + str(self.month) + "/" + str(self.date) +
			", at: " + str(self.at_price) +" per kg." +
			"\n11kg capital is at " + str(self.kg11_capital) + ". SRP is around " + str(self.kg11_srp) + " (20% markup)." +
			"\nSK capital is at " + str(self.sk_capital) + ". SRP is around " + str(self.sk_srp) +" (40% markup).")



when = input("Date (mmdd): ")
# converting inputs to integers for they will be used for computation 
price_per_kg = float(input("Price: "))
kg11_units = int(input("11kg Units (in pcs): ")) 
sk_units = int(input("SK Units (in pcs): "))
total_kgs = float(kg11_units*11) + float(sk_units)*2.7
total_paid = float(total_kgs)*price_per_kg

def get_instance_detail():
	print("Total price paid: " + str(total_paid))
	print("at " + str(total_kgs) +" KGs."
	x = Instance(str(when), str(price_per_kg))
	return x

get_instance_detail()


'''
	Next steps: find a way to have the instances recorded in a table line by line.
	They should be filter-able by date.
	Have monthly-based computations for profits/losses
	Should be able to have options to record other expenses other than capital.
	
'''
