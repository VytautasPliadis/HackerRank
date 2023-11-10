import psycopg2

# Sample data
data = [("Author1", "Book1"),
        ("Author2", "Book2"),
        ("Author3", "Book3"),
        ("Author4", "Book4")]  # Intentional conflict with Author1

# Establish a connection to the PostgreSQL database using a context manager
with psycopg2.connect(
    dbname="test",
    user="postgres",
    password="mossom",
    host="localhost",
    port="5432"
) as conn:
    # Create a cursor object using a context manager
    with conn.cursor() as cursor:
        try:
            # Insert data into authors table with ON CONFLICT DO NOTHING
            cursor.executemany(
                "INSERT INTO authors (author_name) VALUES (%s) ON CONFLICT (author_name) DO NOTHING;",
                [(author_name,) for author_name, _ in data]
            )

            # Prepare data for books table insertion
            books_data = [(title, author_name) for author_name, title in data]

            # Insert data into books table using executemany()
            cursor.executemany(
                "INSERT INTO books (book_title, author_id) "
                "SELECT %s, author_id FROM authors WHERE author_name = %s;",
                books_data
            )

            print("Data inserted successfully.")

        except psycopg2.IntegrityError as e:
            # Handle integrity error (e.g., duplicate key violation) if needed
            print(f"Error occurred: {e}")







# import psycopg2
#
# # Establish a connection to the PostgreSQL database
# conn = psycopg2.connect(
#     dbname="test",
#     user="postgres",
#     password="mossom",
#     host="localhost",
#     port="5432"
# )
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# # Sample data
# data = [("Author1", "Book1"),
#         ("Author2", "Book2"),
#         ("Author3", "Book3"),
#         ("Author4", "Book4")]  # Intentional conflict with Author1
#
# # Insert data into authors table with ON CONFLICT IGNORE
# for author_name, _ in data:
#     try:
#         cursor.execute(
#             "INSERT INTO authors (author_name) VALUES (%s) ON CONFLICT (author_name) DO UPDATE SET author_name = excluded.author_name RETURNING author_id;",
#             (author_name,))
#         result = cursor.fetchone()  # Get the inserted row (or None if ON CONFLICT DO NOTHING triggered)
#         if result:
#             author_id = result[0]  # Get the inserted author_id
#         else:
#             # Handle the case where the row was not inserted due to conflict
#             print(f"Author '{author_name}' already exists in the authors table.")
#             continue  # Skip inserting into books table for this author_name
#     except psycopg2.IntegrityError:
#         # Handle integrity error (e.g., duplicate key violation) if needed
#         print(f"Error occurred while inserting author '{author_name}'.")
#
#     # Insert data into books table using the obtained author_id
#     cursor.execute("INSERT INTO books (book_title, author_id) VALUES (%s, %s)", (_, author_id))
#
# # Commit changes and close the connection
# conn.commit()
# conn.close()
#
#
# def clean_tbl_name(filename):
#     # rename csv, force lower case, no spaces, no dashes
#     clean_tbl_name = filename.lower().replace(" ", "").replace("-", "_").replace(r"/", "_").replace("\\", "_").replace(
#         "$", "").replace("%", "")
#
#     tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])
#
#     return tbl_name
#
#
# def clean_colname(dataframe):
#     # force column names to be lower case, no spaces, no dashes
#     dataframe.columns = [
#         x.lower().replace(" ", "_").replace("-", "_").replace(r"/", "_").replace("\\", "_").replace(".", "_").replace(
#             "$", "").replace("%", "") for x in dataframe.columns]
#
#     # processing data
#     replacements = {
#         'timedelta64[ns]': 'varchar',
#         'object': 'varchar',
#         'float64': 'float',
#         'int64': 'int',
#         'datetime64': 'timestamp'
#     }
#
#     col_str = ", ".join(
#         "{} {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements)))
#
#     return col_str, dataframe.columns