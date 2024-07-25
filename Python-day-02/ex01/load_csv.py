import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """This function loads the data from a CSV file and displays its dimensions

    Args:
        path (str): path to your file

    Returns:
        pd.DataFrame | None : the dataset as pandas object \
or None if an error occ
    """
    try:
        assert isinstance(path, str), "The path to the data should be string"
        assert path.lower().endswith(".csv"), "The supported extension is csv"
        dt = pd.read_csv(path, header=0)
        print(f"Loading dataset of dimensions {dt.shape}")
        return dt
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except FileNotFoundError:
        print(f"File not found at {path}")
    except PermissionError:
        print(f"Error: Permission denied when trying to open file: {path}")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {path} is empty")
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file at {path}")
    except Exception as err:
        print(f"ExceptionError: {err}")
    return None
