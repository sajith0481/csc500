# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col

# # Initialize Spark session
# spark = SparkSession.builder.appName("Example").getOrCreate()

# # Create a sample DataFrame
# data = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
# columns = ["id", "value"]
# df = spark.createDataFrame(data, columns)

# # User-defined function to calculate average with logging
# def calculate_average_with_logging(df, column_name):
#     """
#     Calculate the average of a column with logging at each step.

#     Parameters:
#     df (DataFrame): The DataFrame containing the data.
#     column_name (str): The name of the column to calculate the average for.

#     Returns:
#     float: The average value of the column.
#     """
#     total_sum = 0
#     count = 0

#     for row in df.select(column_name).collect():
#         total_sum += row[column_name]
#         count += 1
#         print(f"Adding {row[column_name]}, Total Sum: {total_sum}, Count: {count}")

#     if count == 0:
#         raise ValueError("Cannot calculate average of an empty DataFrame")

#     average = total_sum / count
#     print(f"Final Average: {average}")
#     return average

# # Example usage
# average_value = calculate_average_with_logging(df, "value")
# print(f"Average Value: {average_value}")

def factorial_with_logging(n: int) -> int:
    """
    Calculate the factorial of a number with logging at each step.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        print(f"Factorial of {n} is 1")
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
        print(f"Intermediate result after multiplying by {i}: {result}")
    print(f"Final result: Factorial of {n} is {result}")
    return result

# Example usage:
factorial_with_logging(5)
