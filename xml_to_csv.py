import os , os.path
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member.find('bndbox')[3].text),
                     int(member.find('bndbox')[3].text),
                     int(member.find('bndbox')[3].text),
                     int(member.find('bndbox')[3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train','test']:
        for image_folder in next(os.walk(directory))[1]:
            image_path1 = os.path.join(os.getcwd(),'{}/'.format(directory))
            image_path2 = os.path.join(image_path1,'{}'.format(image_folder))
            xml_df = xml_to_csv(image_path2)
            xml_df.to_csv('data/{}_labels.csv'.format(directory),mode='a', header=False)
            print('Successfully converted xml to csv.')


main()