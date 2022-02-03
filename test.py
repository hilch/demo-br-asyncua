# hilch/demo-br-asyncua
# simple example how to get access to B&R control with asyncua (asyncio based OPC-UA stack)
# this program is published under the terms of GPL-3.0

# tested with Python 3.9.9 and B&R 'coffe machine' demo project in AS4.7 (ArSim)
# writing the variables needs
# writing the tags requires the activation of the OPC-UA server 
# and a configuration of the corresponding variables as writeable tags.


import asyncio
try:
    from asyncua import Client, ua
except ModuleNotFoundError:
    print("ModuleNotFoundError")
    print("solution: pip install asyncua")
    exit(0)


async def start():
    uaClient = Client(url="opc.tcp://127.0.0.1:4840")
    # anonymous access does not need a user/passwort set 
    #uaClient.set_user('mickey')
    #uaClient.set_password('4711') 
    connected = False
    try:
        await uaClient.connect()
        connected = True
        node1 = 'ns=0;i=2263'
        # read manufacturer's name
        print( await uaClient.get_node(node1).read_value() )
        # read current time
        node2 = 'ns=0;i=2258'
        print( await uaClient.get_node(node2).read_value() ) 
        # write (needs activation in AS project !)
        print("insert money")
        node3 = 'ns=6;s=::AsGlobalPV:gMainLogic.par.givenMoney'       
        dv = ua.DataValue( ua.Variant(Value = 3.0, VariantType= ua.VariantType.Float ), SourceTimestamp=None, ServerTimestamp =None)
        await uaClient.get_node(node3).write_value(dv)
        node4 = 'ns=6;s=::AsGlobalPV:gMainLogic.cmd.switchOnOff'       
        dv = ua.DataValue( ua.Variant(Value = True, VariantType= ua.VariantType.Boolean ), SourceTimestamp=None, ServerTimestamp =None)
        await uaClient.get_node(node4).write_value(dv)  
        print("start machine and boil the water") 
    except asyncio.exceptions.TimeoutError:
        print( ": OPC-UA Timeout !")            
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    finally:
        if connected:
            await uaClient.disconnect()   


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start())
