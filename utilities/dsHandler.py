class DsHandler():

    def read_dataset(ds):
        print(f"{ds}\n")
        tuples_list = []
        for key in ds:
            print(f"key: {key}, value: {ds[key]}\n")
            tuples_list.append((key, ds[key]))
        return tuples_list