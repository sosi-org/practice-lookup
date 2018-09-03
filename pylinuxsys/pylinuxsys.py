os.pipe()

pid=os.fork()
if pid==0:
    #child
else:
    #parent

os.execve(c, [...], env)
env=os.environ
os._exit(0)



# ZMQ
def init_connection(self,port):

        """Scheduler has the server side of the ZMQ"""
        self.zmq_context = get_zmqcontext()
        self.zmqsocket = self.zmq_context.socket(zmq.REP)

        adr = "tcp://*:%s" % port
        try:

            self.zmqsocket.bind( adr )

        except zmq.error.ZMQError as e:
            sys.stderr.write(repr(e))
            sys.stderr.write("ADDRESS/PORT IN USE: %s \n"%(adr,))
            traceback.print_exc()
            exit(1)


buff=self.zmqsocket.recv() or self.zmqsocket.send("")
        #self.zmqsocket.setsockopt(zmq.SNDTIMEO,1500) #man setsockopt
        #self.zmqsocket.setsockopt(zmq.RCVTIMEO,1500)
        # #"zmq.error.Again: Resource temporarily unavailable"


for idx, val in enumerate(ints):
