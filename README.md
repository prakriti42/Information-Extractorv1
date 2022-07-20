## Information Extractor V1 

This mini project consists of a python script written to extract texts as key value pairs based on the pixel positioning of the data in the image file.

### Libraries Used
* Opencv
* Numpy
* Json
* Pytessaract 

Input file : 

<img width="975" alt="Image" src="https://user-images.githubusercontent.com/65444364/180029491-12518ce2-4da7-446b-94a3-1432c2ae24c0.png">

Output json: 

<code> 
{"Master B/L#": " OOLU2665363730",
"House B/L#": " ", 
"Port of Loading": "HO CHI MINH ", 
"Port of UnLading": "Port of Unlading LOS ANGELES", 
"Something": " Mav 2. 2021",
"ABC": " May 23, 2021",
"TEST": "CMA CGM LEO",
"AALU": " OTUH7E1MA"}

</code>
