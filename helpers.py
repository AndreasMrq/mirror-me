def get_api_for(website):
    '''Searches the secrets.txt for the string given as website and returns the value
    after  ":".'''
    fstream=open("secrets.txt",'r')
    settings=fstream.read()
    settings=settings.replace("\n",":").split(":")
    print(settings)
    return settings[settings.index(website)+1]
