import fastparquet, glob

filelist = glob.glob('./fastparquet_iterate_parquet/ursa-labs-taxi-data/*/data.parquet')
print(filelist)
fastparquet.writer.merge(filelist)