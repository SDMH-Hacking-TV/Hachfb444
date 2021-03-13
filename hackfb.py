import os, sys

print ("\033[1;34mLogin ID & Password My-Tools")

print ("\033[1;35mSDMH-Hacking-TV 081249281196 ")
print ("\033[1;32m Hacking Tools :V 1.1")
ID = 'SDMH'      

password = 'Hacking'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("ID : ")

	if uname == ID:

		pwd = raw_input("password : ")



		if pwd == password:

			print "Suksess Login To My-Tools..", 

			sys.exit()



		else:

			print "\033[1;32mWrong Password Please Put The Correct Password... [?]\033[00m"

			print "Log-in Success My-Tools...!!\n"

			restart()



	else:

		print "\033[1;32mWrong ID input Check ... [?]\033[00m"

		print "Log-in Success My-Tools...!!\n"

		restart()




bash TheTHCA.sh
