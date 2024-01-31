from prefect import flow,task


@task
def message_ret():
    msg = "Hello Shangeeth"
    return msg

@flow
def something():
    msg = 10    
    
    return msg


@flow
def first_function():
    msg = message_ret()
    msg2 = something()
    print(msg,msg2)


if __name__ == "__main__":
    first_function()



