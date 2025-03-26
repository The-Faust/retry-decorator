from RetryDecorator import retry

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

@retry(n_retry=2, tts=0.1)
def func_to_retry(raise_error: bool = True):
    if raise_error:
        print("error is raised")
        
        raise Exception("test exception")
    
    print("error not raised")

    return True


def main():
    try:
        func_to_retry()

    except Exception as e:
        print(e)

    func_to_retry(False)

    return


if __name__ == "__main__":
    main()
    
