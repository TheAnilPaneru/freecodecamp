import pandas as pd

def demographic_data_analysis():
    # Load the dataset
    df = pd.read_csv('data.csv', header=None)
    # Assign column names based on the dataset description
    df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
                  'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
                  'hours-per-week', 'native-country', 'salary']
    
    # Ensure numeric columns are properly typed
    numeric_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Helper functions for calculations
    def race_count(df):
        return df['race'].value_counts()

    def average_age_of_men(df):
        return df[df['sex'] == 'Male']['age'].mean().round(1)

    def percentage_bachelors(df):
        return ((df['education'] == 'Bachelors').sum() / df.shape[0] * 100).round(1)

    def higher_education_rich(df):
        higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        return round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0] * 100), 1)

    def lower_education_rich(df):
        higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        lower_education = ~higher_education
        return round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0] * 100), 1)

    def min_work_hours(df):
        return df['hours-per-week'].min()

    def rich_percentage_min_hours(df):
        min_hours = min_work_hours(df)
        num_min_workers = df[df['hours-per-week'] == min_hours]
        return round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100), 1)

    def highest_earning_country(df):
        countries_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
        countries_total = df['native-country'].value_counts()
        highest_earning_country = (countries_earning / countries_total * 100).idxmax()
        highest_earning_country_percentage = round((countries_earning / countries_total * 100).max(), 1)
        return highest_earning_country, highest_earning_country_percentage

    def top_in_occupation(df):
        india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
        if not india_occupation.empty:
            return india_occupation.mode()[0]
        else:
            return None

    # Perform calculations
    result = {
        'race_count': race_count(df),
        'average_age_men': average_age_of_men(df),
        'percentage_bachelors': percentage_bachelors(df),
        'higher_education_rich': higher_education_rich(df),
        'lower_education_rich': lower_education_rich(df),
        'min_work_hours': min_work_hours(df),
        'rich_percentage': rich_percentage_min_hours(df),
        'highest_earning_country': highest_earning_country(df)[0],
        'highest_earning_country_percentage': highest_earning_country(df)[1],
        'top_IN_occupation': top_in_occupation(df)
    }

    return result

# Example to test the function
if __name__ == "__main__":
    print(demographic_data_analysis())


# Test the function and print the results
results = demographic_data_analysis()
for key, value in results.items():
    print(f"{key}: {value}")
