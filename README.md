# Safa-Backend
This is the backend repository to the application Safa.

In the root directory of the application create a file called config.ini

The file looks like:

    [NETWORK]

    IP_ADDRESS = <IP Address (I use my IPv4) address>

Then to run the backend locally, use the command:

    python3 manage.py runserver <IP Address>:8000

If you want to run this with the docker:

    To build the docker image:
    
        docker build -t safa_backend .
        
    To run docker container:
    
        docker run -p 8000:8000 -e HOST=<IP Address> safa_backend
        
        
Ask me for the dictionary .csv if needed. Only I have access to it, and the way to actually generate the data. The backend will break without it.
    
    
       

    
