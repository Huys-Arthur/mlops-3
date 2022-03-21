# Simple unit test for checking that all wanted columns are in our raw data
import pandas as pd

def unittest_output(df: pd.DataFrame):
    assert df['Survived'].isin([0,1]).all()

def main():
    # Read data
    predictions = pd.read_csv('/data/output/final_predictions.csv')

    # Test data
    unittest_output(predictions)
    
    # Success
    print('All output unit tests passed!')
    
if __name__ == '__main__':
    main()
