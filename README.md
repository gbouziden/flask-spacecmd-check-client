# flask-spacecmd-check-client
This is a remote function to check if a host is present in Spacewalk. It can be altered to delete or add hosts as well. 

To check, run curl:

curl server.address:5000/?hostname=< hostname >

You will need to run this in the same directory as your ~/.spacecmd/config file. 

Setting that up can be found here: https://github.com/spacewalkproject/spacewalk/wiki/spacecmd
