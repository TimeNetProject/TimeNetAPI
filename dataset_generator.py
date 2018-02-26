# libraries


available_datasets = ['mitbih', 'ptbdb', 'hapt']

parameters = {}


# setting the parameters
def set_parameters(
        path_to_database='./data/',
        database_name='mitbih',
):
    parameters['path_to_database'] = path_to_database
    parameters['database_name'] = database_name


if __name__ == '__main__':
    print("Project TimeNet - Dataset generator")

    set_parameters()

    # importing the required libraries
    if parameters['database_name'] == 'mitbih':
        import library.dataset_importers.importer_mitbih as database_importer
    elif parameters['database_name'] == 'ptbdb':
        import library.dataset_importers.importer_ptbdb as database_importer
    elif parameters['database_name'] == 'hapt':
        import library.dataset_importers.importer_hapt as database_importer


    flag_to_crawl = input("Have you created the TimeNet records already?\n\n")
    if str(flag_to_crawl) == '0' or str(flag_to_crawl) == 'no':
        # retrieving the data from cloud and storing it in the specified data folder:
        database_importer.download_the_original(parameters) #phase 1

    # applying the transforms and creating the final timenet package
    # transforming and saving the specified dataset
    database_importer.prepare_and_store_timenet_dataset(parameters) #phase 2




