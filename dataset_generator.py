# libraries






available_datasets = ['mitbih', 'ptbdb', 'hapt']

parameters = {}


# setting the parameters
def set_parameters(
        path_to_database='/mnt/Data/Database/TimeNetData/',
        database_name='hapt',
):
    parameters['path_to_database'] = path_to_database
    parameters['database_name'] = database_name


if __name__ == '__main__':
    print("Project TimeNet - Dataset generator")

    set_parameters()

    # importing the required libraries
    if parameters['database_name'] == 'mitbih':
        import library.dataset_importers.importer_mitbih as database_importer
    if parameters['database_name'] == 'hapt':
        import library.dataset_importers.importer_hapt as database_importer
     

    # retrieving the data from cloud and storing it in the specified data folder:
    database_importer.download_the_original(parameters) #phase 1

    # transforming and saving the specified dataset
    #database_importer.transform_and_store(parameters) #phase 2




