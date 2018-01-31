# Short_Scripts

This is a general repo for short tasks with some scripts being :-

	Download of generated qr_codes from google charts, with the download links provided as a text file.

	Custom pole numbering function in QGIS - arguments  being @rownumber variable, together with the pole numbering txt e.g CKRC.
    This script can also be customised and  used with qgis processing models to control numbering
    of customers ( so that numbering should not exceed 20).

Pole numbering usage (the following will work with QGIS 2.14, but code can also be used with any QGIS version):- 
	
	Copy the pole_numbering.py code into the QGIS function editor in Field Calculator by creating a file and giving it a name of your choice.
	Load it so that it executes and so that it executes without errors.
	In the expressions window of field calculator, go to Custom and double click on the function name.
	Enter the expression with the arguments @row_number and 'label_const'- remember to use single quotes as double quotes are used for field names or rather to call 
	previously defined fields. 

 		examples:- pole_numberer(@row_number, 'CKRC10') - for 10 metre poles and pole_numberer(@row_number, 'CKRC07') - for 7 metre poles
 



