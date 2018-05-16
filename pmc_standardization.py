import sys
import os
import pandas
from datetime import datetime
import argparse
import xml.etree.ElementTree as ET
import json
import xmltodict


from PIL._util import isDirectory
DOCS_FOR_FOLDER=1000

parser=argparse.ArgumentParser()
parser.add_argument('-o', help='Output Directory')
parser.add_argument('-r', help='Remove All Before downloading, warning you have to be sure of remove al the PubMed Database')
args=parser.parse_args()

if __name__ == '__main__':
    import pmc_standardization
    try:
        dest=args.o
    except Exception as inst:
        print( "Error: reading the parameters.")
        sys.exit(1) 
    if dest==None:
        print( "Error: complete the destination path") 
        sys.exit(1)    
    if not os.path.exists(dest):
        print( "Error: the destination path does not exist.") 
        sys.exit(1) 
    pmc_standardization.Main(args)
    

def Main(args):
    dest=args.o
    #result_file = dest + "/index.csv"
    standardization_output = dest + "/standardization/"
    standardization_input = dest + "/retrieval/"
    
    if not os.path.exists(standardization_output):
        os.makedirs(standardization_output)
    
    '''if os.path.isfile(result_file):
        df = pandas.read_csv(result_file, header=0, index_col=0)
    else:
        print ("The update_histroy file is missing.")    
        sys.exit(1)
    '''     
    standardization(standardization_input,standardization_output)

                       
def standardization(standardization_input, standardization_output):
    #df_=df.loc[df['unzip'] == 'complete']
    work_dirs = [ f for f in os.listdir(standardization_input) if isDirectory(os.path.join(standardization_input, f))]
    for work_dir in work_dirs:
        work_dir_output = os.path.join(standardization_output, work_dir)
        if not os.path.exists(work_dir_output):
            os.makedirs(work_dir_output)
        update_folder = os.path.join(standardization_input, work_dir)
        folders = [ f for f in os.listdir(update_folder) if isDirectory(os.path.join(update_folder, f))]
        for sub_folder in folders:
            output_folder = os.path.join(work_dir_output, sub_folder)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            sub_folder = os.path.join(update_folder, sub_folder)    
            files = [f for f in os.listdir(sub_folder) if os.path.isfile(os.path.join(sub_folder, f))]
            for file_name in files:
                if(file_name.endswith(".xml")):
                    file_path = os.path.join(sub_folder, file_name)
                    with open(file_path,'r') as xml_file:
                        try:
                            file_name = file_name[:-4]
                            docXml = ET.parse(xml_file)
                            print ("Processing pmid:" + file_path)
                            root = docXml.getroot()
                            xml_string = ET.tostring(root, encoding='utf-8', method='xml')
                            o = xmltodict.parse(xml_string, encoding='utf-8')
                            jsonString = json.dumps(o, indent=4)
                            json_file=open(output_folder+"/"+file_name+".json",'w')
                            json_file.write(jsonString)
                            json_file.flush()
                            json_file.close()
                            txt = ET.tostring(root, encoding='utf-8', method='text')
                            txt_file=open(output_folder+"/"+file_name+".txt",'w')
                            txt_file.write(txt)
                            txt_file.flush()
                            txt_file.close()
                            '''
                            df.at[index,'name']=pmc_id
                            df.at[index,'date']=str(datetime.now().date())
                            df.at[index,'time']=str(datetime.now().time())
                            df.at[index,'standardization']="complete"
                            df.at[index,'txt_path']=file_path
                            df.at[index,'json_path']=file_path
                            df.to_csv(result_file)    
                            '''            
                        except Exception as inst:
                            print "Error Generando el JSON PMID " + file
                            print inst
                            x = inst.args
                            print x 
                
            
        