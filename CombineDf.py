import pandas as pd
import pickle

def combine_dataframes(dataframes):
    combined_df = pd.concat(dataframes.values(), ignore_index=True)

    # Create the 'Platform' column with unique platform values for each Title
    combined_df['Platform'] = combined_df.groupby('Title')['Platform'].transform(lambda x: ', '.join(x.unique()))

    # Drop duplicate rows to keep unique combinations of Title and Platform
    combined_df = combined_df.drop_duplicates(subset=['Title', 'Platform']).reset_index(drop=True)

    return combined_df

if __name__ == "__main__":

    with open('result_dataframes.pkl', 'rb') as file:
        result_dataframes = pickle.load(file)

    combined_df = combine_dataframes(result_dataframes)
    print (combined_df)
    combined_df.to_csv('IGN.csv', index=False)
