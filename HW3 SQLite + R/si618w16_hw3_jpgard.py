
import sqlite3

def get_data(infile):
	output = []
	infile = open(infile, 'rU')
	for line in infile.readlines()[1:]:
		data = line.split(',')
		year = data[63]
		make = data[46]
		model = data[47]
		VClass = data[62]
		cylinders = data[22]
		displ = data[23]
		trany = data[57]
		city08 = data[4]
		highway08 = data[34]
		comb08 = data[15]

		lineout = (year, make, model, VClass, cylinders, displ, trany, city08, highway08, comb08)

		if cylinders != 0 and cylinders != '' and cylinders != 'NA' and displ != 0 and displ != '' and displ != 'NA':
			output.append(lineout)

	return output


def write_data(data, outfile):
	conn = sqlite3.connect(outfile)
	c = conn.cursor()

	c.execute('''CREATE TABLE vehicles
             (year real, make text, model text, VClass text, cylinders real, displ real, trany text, city08 real, highway08 real, comb08 real)''')

	for item in data:
		query = 'INSERT INTO vehicles VALUES %s' % (str(item))
		c.execute(query)
		conn.commit()
	conn.close()

def main(infile, outfile):
	data = get_data(infile)
	write_data(data, outfile)


if __name__ == '__main__':
	infile = "vehicles.csv"
	outfile = "vehicles.db"
	main(infile, outfile)