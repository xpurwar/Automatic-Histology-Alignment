from DeepSlice import DSModel

species = 'mouse' #available species are 'mouse' and 'rat'
Model = DSModel(species)
#this cell should take about 1 second per image
folderpath = '/Users/dineshupadhyay/Transluscence/Automatic-Histology-Alignment-1/ExampleBrain'
Model.predict(folderpath, ensemble=True, section_numbers=True)
Model.propagate_angles()
Model.enforce_index_spacing()
Model.save_predictions(folderpath + 'MyResults')