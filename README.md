PMC Standardization
========================


 

========================

1.- Clone this repository 

    $ git clone https://github.com/javicorvi/pmc_standardization.git
    
2.- Python 2.7 
	
	
3.- Third Party 
	
	pip install pandas
	pip install xmltodict
	pip install json

	
4.- Run the script
	
	To run the script just execute python pmc_standardization -o /home/myname/pmc_data 

5.- The container 
	
	If you just want to run the app without any kind of configuration you can do it 
	through the docker container is avaiblable in https://hub.docker.com/r/javidocker/pmc_standardization/ 

	To run the docker: 
	
	docker run --rm -u $UID  -v /home/yourname/pmc_data:/app/data pmc_standardization

	the path home/yourname/pmc_data will be the working directory in where the data will be downloaded.
