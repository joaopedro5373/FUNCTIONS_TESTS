import os
def get_environment_variable(var_name:str)->str:
    return os.environ[var_name]