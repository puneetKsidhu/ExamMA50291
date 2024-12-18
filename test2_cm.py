###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

## Main
if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print(df)

    # Simulate 20 data points per group
    col_specs = {
        'height': {'distribution': 'normal', 'variance': 5},
        'weight': {'distribution': 'normal', 'variance': 3},
        'age': {'distribution': 'normal', 'variance': 2}
    }
    data = cm.simulate_data(df, n_points=20, col_specs=col_specs)
    print('\nSimulated data points:')
    print(data.head())

    # Try this first
    try:
        crr = cm.calculate_correlation(data)
        print(crr)
    except AttributeError as a:
        print(f"AttributeError: {a}")

    # Conclusion
    print("Is everything really working?")