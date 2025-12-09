"""1. The Package I decided to use is BioPython. Bio Python is an open source package for bioinformatics.
It is useful in looking at DNA sequences in formats such as FASTA to parce together the data needed.
2. Advantages: EAsy way to handle biologica;l data, and its open source so it is free. Disadvantages are that it is some times slow
and it sometimes requires other biological tools like Bioconda."""
import Bio
from Bio import Entrez

from Bio import Entrez
from Bio import SeqIO
#need email to access NCBI
Entrez.email = "bryce.bosworth@hsc.utah.edu"
#
sequence = Entrez.efetch(db="nucleotide", id='17590', rettype='fasta', retmode='text')
seq_extract = SeqIO.read(sequence,'fasta')
c_elegans_seq = seq_extract.seq
print("The sequence of a c elegans gene is: ")
print(c_elegans_seq)
print("The length of a c elegans gene is: ")
print(len(c_elegans_seq))
print("The number of Adenine in a a c elegans gene is: ")
print(c_elegans_seq.count('A'))
print("The complement of a c elegans gene is: ")
print(c_elegans_seq.complement())
print("The transcription of a c elegans gene is: ")
print(c_elegans_seq.transcribe())
print("The protein sequence of a c elegans gene is: ")
print(c_elegans_seq.translate())


