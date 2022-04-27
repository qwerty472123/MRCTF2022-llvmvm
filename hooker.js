// frida ./llvmvm -l hooker.js --no-pause
// 11111111111111111111111111111111
let f = new File('record.txt', 'w');

function print_dump(addr, size){
	if (size instanceof NativePointer) {
		size = size.toInt32();
	}
    let buf = Memory.readByteArray(addr, size)
    console.log("[dump] " + addr.toString() + "  "+ "length: " + size.toString() + "\n[data]")
    console.log(hexdump(buf, {
      offset: 0,
      length: size,
          header: false,
          ansi: false
    }));
    console.log("")
	return Array.from(new Uint8Array(buf)).map(x => x.toString(16).padStart(2, '0')).join('');
}

Interceptor.replace(Module.findExportByName(null, "__isoc99_scanf"), new NativeCallback((format, v) => {
  console.log(format.readCString());
  v.writeByteArray(Array.from('MRCTF{s@1Sa2O_w1tH_bE5t_1lVmvM!}\x00').map(v => v.charCodeAt(0)));
  return 0;
}, 'int', ['pointer', 'pointer']));

Interceptor.attach(ptr('0x401150'), {
    onEnter: function (args, state) {
        f.write('E' + print_dump(args[1], 16 * 4) + '\n');
		f.flush();
		this.arg0 = args[0];
    },
    onLeave: function (retval, state) {
		f.write('L' + print_dump(this.arg0, 16 * 4) + '\n');
		f.flush();
    }
});
