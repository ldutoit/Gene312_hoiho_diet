#Just using python to reformat the database from https://github.com/ldutoit/YEP_diet/blob/master/create_classifier_primers_spec.md
#into a formt for the R package dada2.

dict_taxonomy = {}

i=0
with open("allrecordsncbi_accession.txt") as f:
	for line in f:
		i+=1
		if i%100000==0: print(i)
		taxo="Animalia;"+";".join(line.split()[1].split(";")[:-1])
		if len(line.split())>2:
			if " " in line.split()[2]:
				#only add species name
				species_name=line.split()[2].split(" ")[1]
				taxo=taxo+";"+species_name
			else:
				#add everything that is at the species_place
				taxo=taxo+";"+line.split()[2]
		#The genus is repeates so we removed
		dict_taxonomy[line.split()[0]]=taxo

output = open("taxo_reference_dada2_youngetal_alllevels.fa","w")
with open("ref-seqschorwithextra2.fa") as f:
	for line in f:
		if line.startswith(">"):
			code =  line.strip().split(">")[1].split()[0]
			taxo = dict_taxonomy[code]
			output.write(">"+taxo+";\n")
		else:
			output.write(line)
output.close()


#Note I removed all the Hemerocoetes homesecluster annotation and just called them NA at the s;ecies level