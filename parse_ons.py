import pandas as pd

def format_csv(count_csv_name):
    count_csv = pd.read_csv(count_csv_name, index_col=0)
    count_csv = count_csv.rename(columns={"AREACD": "LAU118CD"})
    count_csv = count_csv.set_index("LAU118CD")
    return count_csv

def drop_counts(count_csv):
    count_csv = count_csv.drop("AREANM", axis=1)
    count_csv = count_csv.drop("Total", axis=1)
    return count_csv

def get_most_popular(count_csv, column_name):
    popular_names = [row[1].idxmax() for row in count_csv.iterrows()]
    count_csv[column_name] = popular_names
    return count_csv


if __name__=="__main__":
    counts = ['girl_count', 'boy_count']
    top_by_region = []
    for count in counts:
        filename = 'data/' + count + '.csv'
        count_csv = format_csv(filename)
        count_csv = drop_counts(count_csv)
        count_csv.fillna(0, inplace=True)
        count_csv = get_most_popular(count_csv, count)
        top_by_region.append(count_csv[count])
    top_by_region = pd.concat(top_by_region, axis=1)
    top_by_region.to_csv('data/top_by_region.csv', index="LAU118CD")
