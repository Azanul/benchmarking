from fastparquet import ParquetFile

def main():
    ds = ParquetFile("../../datasets/ursa-labs-taxi-data")

    rows = 0
    for batch in ds.iter_row_groups():
        rows += len(batch.index)
    print(rows)


if __name__=="__main__":
    main()