from langchain_core.tools import tool


@tool
def query_executor(query: str):
    """
    Executes a given SQL query on the "Rfam" database and handles both SELECT and non-SELECT operations.

    - For SELECT queries: Fetches and returns the result set with column names.
    - For non-SELECT queries (e.g., INSERT, UPDATE, DELETE): Commits the changes to the database.
    - Implements error handling to roll back transactions in case of failures.

    Args:
        query (str): The SQL query to be executed.

    Returns:
        dict:
            - For SELECT queries: A dictionary with the query, success message, and fetched results.
            - For non-SELECT queries: A dictionary with the query and success message.
            - For errors: A dictionary containing the error message.
    """
    try:
        d = DatabaseConnection("rfamro", "", "mysql-rfam-public.ebi.ac.uk", "4497", "mysql")
        query = query.replace('\\', '')
 
        result = d.execute_query(query=query, database_name="Rfam")
 
        if result.returns_rows:
            rows = result.fetchall()
            return {
                'query': query,
                'results': rows
            }
        else:
            return {
                'query': query,
                'message': 'Query executed successfully.'
            }
    except Exception as e:
        return {
            'query': query,
            'error': f"An error occurred: {str(e)}"
        }