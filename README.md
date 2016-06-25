# PQ-NYCHA
Project-related drive for Progress Queens work regarding NYCHA FOIL documents.

The first module I'm uploading was designed to help read a CSV file of NYCHA
service repairs. The CSV file, which is being read by the module, was produced
by NYCHA to Progress Queens in response to a FOIL request for documents that
had been separately produced by NYCHA to the U.S. Attorney's Office. In total, 
NYCHA produced to Progress Queens approximately 1 GB of electronic documents. 
The size of the document production given to Progress Queens by NYCHA pales
in comparison with the approximately 400 million records that NYCHA has reportedly 
provided to the U.S. Attorney's Office. Despite attempts at follow-up about
the relatively small size of documents produced to Progress Queens, NYCHA 
has not explained this discrepancy. Furthermore, some of the files that NYCHA
produced were unreadable or contained unexplained information. (The subject CSV
file was too large to fully open in Excel, for example, forcing me to turn to
Python as a method to read and review the CSV file.) Despite these limitations,
this module provides some meaningful information about the service repair 
information contained in the CSV file.

This module evolved from my self-study of Python. After I studied enough to
write my first attempt at a module, I still had a lot of questions -- and
an unworkable module. At the suggestion of a friend, I attended a meet-up of
the Saturday Python Study Group, where I met Dillon Ko. Dillon immediately saw
that my approach to the module was incorrect, and he pointed me in a better
direction. After some more self-study, I was able to produce this working module.
Although unsophisticated, this module works, and I am proud of having been able 
to write a module that could read the CSV file and be shared with others, so 
that others could also read the CSV file.

Progress Queens believes in the democratization of data. All FOIA/FOIL records
received by Progress Queens are freely posted online, often before Progress
Queens reviews the documents. The sharing of public documents that are received
by Progress Queens is meant to further an open government. Progress Queens also
publishes this module, to make the CSV file accessible to the public, as well.
