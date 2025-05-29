from DeepSlice import DSModel

species = 'mouse' #available species are 'mouse' and 'rat'
Model = DSModel(species)
#this cell should take about 1 second per image
folderpath = 'examples/example_brain/GLTa/'
Model.predict(folderpath, ensemble=True, section_numbers=True)