from pyarrow import csv
from pyarrow.dataset import dataset
from pyarrow import fs

def main():
    ds = dataset("../../datasets/ursa-labs-taxi-data", partitioning=["month"])
    
    rows = 0
    for batch in ds.to_batches(batch_size=1000):
        rows += batch.num_rows
    print(rows)


if __name__=="__main__":
    main()