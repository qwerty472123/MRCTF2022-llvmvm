[QWORD* memory[0x21]] = memory[0x0];
[QWORD* memory[0x31]] = memory[0x8];
[unsigned int* memory[0x3d]] = 0x0;
L_0100: // from R_038b
memory[0x1bf] = BYTE [unsigned int* memory[0x3d]] < 0x10;
if (!memory[0x1bf]) goto L_0395; // R_0158
memory[0x1cf] = (char)[int* memory[0x21]] + (long)[unsigned int* memory[0x3d]];
memory[0x1c4] = (int)[unsigned int* memory[0x3d]] + (int)0x3;
memory[0x1c0] = (int)[BYTE* memory[0x1cf]] ^ (int)memory[0x1c4];
memory[0x1c4] = (int)[unsigned int* memory[0x3d]] % (int)0x8;
memory[0x1bb] = (int)memory[0x1c0] >> (int)memory[0x1c4];
memory[0x1d3] = (char)[int* memory[0x21]] + (long)[unsigned int* memory[0x3d]];
memory[0x1c8] = (int)[unsigned int* memory[0x3d]] + (int)0x3;
memory[0x1c4] = (int)[BYTE* memory[0x1d3]] ^ (int)memory[0x1c8];
memory[0x1c8] = (int)[unsigned int* memory[0x3d]] % (int)0x8;
memory[0x1c8] = (int)memory[0x1c4] << (int)((int)0x8 - (int)memory[0x1c8]);
memory[0x1bf] = (int)memory[0x1bb] | (int)memory[0x1c8];
memory[0x1d0] = (char)[int* memory[0x21]] + (long)[unsigned int* memory[0x3d]];
[BYTE* memory[0x1d0]] = memory[0x1bf];
memory[0x1bf] = (int)[unsigned int* memory[0x3d]] + (int)0x1;
[unsigned int* memory[0x3d]] = memory[0x1bf];
if (0x1) goto L_0100; // R_038b
L_0395: // from R_0158
memory[0x1c3] = (char)[int* memory[0x21]] + (long)0x0;
memory[0x1c3] = [unsigned int* ((unsigned int*)memory[0x1c3])];
a = memory[0x1c3];
memory[0x1c3] = (char)[int* memory[0x21]] + (long)0x4;
memory[0x1c3] = [unsigned int* ((unsigned int*)memory[0x1c3])];
b = memory[0x1c3];
memory[0x1c3] = (char)[int* memory[0x21]] + (long)0x8;
memory[0x1c3] = [unsigned int* ((unsigned int*)memory[0x1c3])];
c = memory[0x1c3];
memory[0x1c3] = (char)[int* memory[0x21]] + (long)0xc;
memory[0x1c3] = [unsigned int* ((unsigned int*)memory[0x1c3])];
d = memory[0x1c3];
[unsigned int* memory[0x109]] = 0x0;
L_04e8: // from R_0aaa
memory[0x1bf] = BYTE [unsigned int* memory[0x109]] < 0x4;
if (!memory[0x1bf]) goto L_0ab4; // R_0540
memory[0x1c3] = (int)b * (int)c;
memory[0x1bb] = (int)memory[0x1c3] & (int)0xdeadbfef;
memory[0x1c3] = (int)a << (int)0x3;
memory[0x1bf] = (int)memory[0x1bb] + (int)memory[0x1c3];
memory[0x1c3] = (int)d >> (int)0x1d;
memory[0x1bb] = (int)memory[0x1bf] + (int)memory[0x1c3];
a = memory[0x1bb];
memory[0x1c3] = (int)c * (int)d;
memory[0x1bb] = (int)memory[0x1c3] & (int)0xdefdbeef;
memory[0x1c3] = (int)b << (int)0x7;
memory[0x1bf] = (int)memory[0x1bb] + (int)memory[0x1c3];
memory[0x1c3] = (int)a >> (int)0x19;
memory[0x1bb] = (int)memory[0x1bf] + (int)memory[0x1c3];
b = memory[0x1bb];
memory[0x1c3] = (int)d * (int)a;
memory[0x1bb] = (int)memory[0x1c3] & (int)0xdfadbeef;
memory[0x1c3] = (int)c << (int)0x9;
memory[0x1bf] = (int)memory[0x1bb] + (int)memory[0x1c3];
memory[0x1c3] = (int)b >> (int)0x17;
memory[0x1bb] = (int)memory[0x1bf] + (int)memory[0x1c3];
c = memory[0x1bb];
memory[0x1c3] = (int)a * (int)b;
memory[0x1bb] = (int)memory[0x1c3] & (int)0xdeadbeff;
memory[0x1c3] = (int)d << (int)0x1;
memory[0x1bf] = (int)memory[0x1bb] + (int)memory[0x1c3];
memory[0x1c3] = (int)c >> (int)0x1f;
memory[0x1bb] = (int)memory[0x1bf] + (int)memory[0x1c3];
d = memory[0x1bb];
memory[0x1bf] = (int)d + (int)0xdeadbeef;
memory[0x1c3] = (int)0x4 * (int)[unsigned int* memory[0x109]];
memory[0x1cf] = 4 * memory[0x1c3] + 64 * 0x0 + memory[0xb5];
[unsigned int* memory[0x1cf]] = memory[0x1bf];
memory[0x1bf] = (int)c + (int)0xaa114514;
memory[0x1c3] = (int)0x4 * (int)[unsigned int* memory[0x109]];
memory[0x1c3] = ((int)memory[0x1c3] + (int)0x1);
memory[0x1cb] = 4 * memory[0x1c3] + 64 * 0x0 + memory[0xb5];
[unsigned int* memory[0x1cb]] = memory[0x1bf];
memory[0x1bf] = (int)a + (int)0xf1919810;
memory[0x1c3] = (int)0x4 * (int)[unsigned int* memory[0x109]];
memory[0x1c3] = ((int)memory[0x1c3] + (int)0x2);
memory[0x1cb] = 4 * memory[0x1c3] + 64 * 0x0 + memory[0xb5];
[unsigned int* memory[0x1cb]] = memory[0x1bf];
memory[0x1bf] = (int)b + (int)0x1abcdef1;
memory[0x1c3] = (int)0x4 * (int)[unsigned int* memory[0x109]];
memory[0x1c3] = ((int)memory[0x1c3] + (int)0x3);
memory[0x1cb] = 4 * memory[0x1c3] + 64 * 0x0 + memory[0xb5];
[unsigned int* memory[0x1cb]] = memory[0x1bf];
memory[0x1bf] = (int)[unsigned int* memory[0x109]] + (int)0x1;
[unsigned int* memory[0x109]] = memory[0x1bf];
if (0x1) goto L_04e8; // R_0aaa
L_0ab4: // from R_0540
[unsigned int* memory[0x115]] = 0x0;
L_0aef: // from R_1308
memory[0x1bf] = BYTE [unsigned int* memory[0x115]] < 0x20;
if (!memory[0x1bf]) goto L_1312; // R_0b47
memory[0x1cf] = (char)[int* memory[0x31]] + (long)[unsigned int* memory[0x115]];
[BYTE* memory[0x11e]] = [BYTE* memory[0x1cf]];
memory[0x1c0] = (int)[BYTE* memory[0x11e]] & (int)0xaa;
memory[0x1bb] = (int)memory[0x1c0] >> (int)0x1;
memory[0x1c4] = (int)[BYTE* memory[0x11e]] & (int)0x55;
memory[0x1c3] = (int)memory[0x1bb] | (int)((int)memory[0x1c4] << (int)0x1);
[BYTE* memory[0x11e]] = memory[0x1c3];
memory[0x1c0] = (int)[BYTE* memory[0x11e]] & (int)0xcc;
memory[0x1bb] = (int)memory[0x1c0] >> (int)0x2;
memory[0x1c4] = (int)[BYTE* memory[0x11e]] & (int)0x33;
memory[0x1c3] = (int)memory[0x1bb] | (int)((int)memory[0x1c4] << (int)0x2);
[BYTE* memory[0x11e]] = memory[0x1c3];
memory[0x1c0] = (int)[BYTE* memory[0x11e]] & (int)0xf0;
memory[0x1bb] = (int)memory[0x1c0] >> (int)0x4;
memory[0x1c4] = (int)[BYTE* memory[0x11e]] & (int)0xf;
memory[0x1c3] = (int)memory[0x1bb] | (int)((int)memory[0x1c4] << (int)0x4);
[BYTE* memory[0x11e]] = memory[0x1c3];
memory[0x1d0] = (char)[int* memory[0x31]] + (long)[unsigned int* memory[0x115]];
[BYTE* memory[0x1d0]] = [BYTE* memory[0x11e]];
[unsigned int* memory[0x12a]] = 0x0;
L_0e25: // from R_1086
memory[0x1bf] = BYTE [unsigned int* memory[0x12a]] < 0x20;
if (!memory[0x1bf]) goto L_1090; // R_0e7d
memory[0x1bf] = (int)[unsigned int* memory[0x12a]] % (int)0x10;
memory[0x1bb] = 4 * memory[0x1bf] + 64 * 0x0 + memory[0xb5];
memory[0x1c3] = [unsigned int* memory[0x1bb]];
memory[0x1bf] = (int)memory[0x1c3] >> (int)[unsigned int* memory[0x12a]];
memory[0x1c3] = (int)[unsigned int* memory[0x12a]] % (int)0x10;
memory[0x1cf] = 4 * memory[0x1c3] + 64 * 0x0 + memory[0xb5];
memory[0x1c7] = (int)0x20 - (int)[unsigned int* memory[0x12a]];
memory[0x1c3] = (int)[unsigned int* memory[0x1cf]] << (int)memory[0x1c7];
memory[0x1bb] = (int)memory[0x1bf] | (int)memory[0x1c3];
memory[0x1bf] = (int)memory[0x1bb] & (int)0xff;
memory[0x1d3] = (char)[int* memory[0x31]] + (long)[unsigned int* memory[0x12a]];
memory[0x1bb] = (int)[BYTE* memory[0x1d3]] ^ (int)memory[0x1bf];
[BYTE* memory[0x1d3]] = memory[0x1bb];
memory[0x1bf] = (int)[unsigned int* memory[0x12a]] + (int)0x1;
[unsigned int* memory[0x12a]] = memory[0x1bf];
if (0x1) goto L_0e25; // R_1086
L_1090: // from R_0e7d
function1((4 * 0x0 + 64 * 0x0 + memory[0xfd]), (4 * 0x0 + 64 * 0x0 + memory[0xb5]));
[unsigned int* memory[0x136]] = 0x0;
L_1136: // from R_128e
memory[0x1bf] = BYTE [unsigned int* memory[0x136]] < 0x10;
if (!memory[0x1bf]) goto L_1298; // R_118e
memory[0x1c7] = 4 * [unsigned int* memory[0x136]] + 64 * 0x0 + memory[0xfd];
memory[0x1cb] = 4 * [unsigned int* memory[0x136]] + 64 * 0x0 + memory[0xb5];
[unsigned int* memory[0x1cb]] = [unsigned int* memory[0x1c7]];
memory[0x1bf] = (int)[unsigned int* memory[0x136]] + (int)0x1;
[unsigned int* memory[0x136]] = memory[0x1bf];
if (0x1) goto L_1136; // R_128e
L_1298: // from R_118e
memory[0x1bf] = (int)[unsigned int* memory[0x115]] + (int)0x1;
[unsigned int* memory[0x115]] = memory[0x1bf];
if (0x1) goto L_0aef; // R_1308
L_1312: // from R_0b47
[unsigned int* memory[0x142]] = 0x0;
L_134d: // from R_19fd
memory[0x1bf] = BYTE [unsigned int* memory[0x142]] < 0x4;
if (!memory[0x1bf]) goto L_1a07; // R_13a5
memory[0x1c7] = (int)0x8 * (int)[unsigned int* memory[0x142]];
memory[0x1c3] = (char)[int* memory[0x31]] + (long)memory[0x1c7];
[BYTE* memory[0x14b]] = [BYTE* memory[0x1c3]];
[unsigned int* memory[0x157]] = 0x0;
L_144a: // from R_1983
memory[0x1bf] = BYTE [unsigned int* memory[0x157]] < 0x64;
if (!memory[0x1bf]) goto L_198d; // R_14a2
[unsigned int* memory[0x163]] = 0x0;
L_14ec: // from R_1909
memory[0x1bf] = BYTE [unsigned int* memory[0x163]] < 0x8;
if (!memory[0x1bf]) goto L_1913; // R_1544
memory[0x1cc] = (int)0x2 * (int)[unsigned int* memory[0x163]];
memory[0x1c8] = (char)[int* memory[0x21]] + (long)memory[0x1cc];
memory[0x1d0] = (int)0x2 * (int)[unsigned int* memory[0x163]];
memory[0x1d0] = ((int)memory[0x1d0] + (int)0x1);
memory[0x1d8] = (char)[int* memory[0x21]] + (long)memory[0x1d0];
memory[0x1c8] = (int)[BYTE* memory[0x1c8]] ^ (int)[BYTE* memory[0x1d8]];
memory[0x1c0] = (int)[BYTE* memory[0x14b]] + (int)memory[0x1c8];
[BYTE* memory[0x14b]] = memory[0x1c0];
memory[0x1bc] = (unsigned int*)[BYTE* memory[0x14b]];
memory[0x1bc] = [BYTE* Sbox[0x0][memory[0x1bc]]];
memory[0x1cc] = (int)0x8 * (int)[unsigned int* memory[0x142]];
memory[0x1d0] = (int)[unsigned int* memory[0x163]] + (int)0x1;
memory[0x1d0] = (int)memory[0x1cc] + (int)((int)memory[0x1d0] % (int)0x8);
memory[0x1d0] = (char)[int* memory[0x31]] + (long)memory[0x1d0];
memory[0x1c4] = (int)memory[0x1bc] + (int)[BYTE* memory[0x1d0]];
[BYTE* memory[0x14b]] = memory[0x1c4];
memory[0x1c0] = (int)[BYTE* memory[0x14b]] << (int)0x1;
memory[0x1c4] = (int)[BYTE* memory[0x14b]] >> (int)0x7;
memory[0x1bb] = (int)memory[0x1c0] | (int)memory[0x1c4];
[BYTE* memory[0x14b]] = memory[0x1bb];
memory[0x1c8] = (int)0x8 * (int)[unsigned int* memory[0x142]];
memory[0x1cc] = (int)[unsigned int* memory[0x163]] + (int)0x1;
memory[0x1cc] = (int)memory[0x1c8] + (int)((int)memory[0x1cc] % (int)0x8);
memory[0x1cc] = (char)[int* memory[0x31]] + (long)memory[0x1cc];
[BYTE* memory[0x1cc]] = [BYTE* memory[0x14b]];
memory[0x1bf] = (int)[unsigned int* memory[0x163]] + (int)0x1;
[unsigned int* memory[0x163]] = memory[0x1bf];
if (0x1) goto L_14ec; // R_1909
L_1913: // from R_1544
memory[0x1bf] = (int)[unsigned int* memory[0x157]] + (int)0x1;
[unsigned int* memory[0x157]] = memory[0x1bf];
if (0x1) goto L_144a; // R_1983
L_198d: // from R_14a2
memory[0x1bf] = (int)[unsigned int* memory[0x142]] + (int)0x1;
[unsigned int* memory[0x142]] = memory[0x1bf];
if (0x1) goto L_134d; // R_19fd
L_1a07: // from R_13a5
[QWORD* memory[0x173]] = ((unsigned int*)[int* memory[0x31]]);
[unsigned int* memory[0x17f]] = 0x0;
L_1a61: // from R_1e5c
memory[0x1bf] = BYTE [unsigned int* memory[0x17f]] < 0x8;
if (!memory[0x1bf]) goto L_1e66; // R_1ab9
[QWORD* memory[0x18f]] = 0x0;
[unsigned int* memory[0x19b]] = 0x0;
L_1b1c: // from R_1d12
memory[0x1bf] = BYTE [unsigned int* memory[0x19b]] < 0x20;
if (!memory[0x1bf]) goto L_1d1c; // R_1b74
memory[0x1cf] = 4 * [unsigned int* memory[0x17f]] + [unsigned int* memory[0x173]];
memory[0x1c3] = (int)[unsigned int* memory[0x1cf]] >> (int)[unsigned int* memory[0x19b]];
[unsigned int* memory[0x1a7]] = ((int)memory[0x1c3] & (int)0x1);
memory[0x1c7] = weights[ 256 * 0x0 + 8 * [unsigned int* memory[0x19b]] ];
memory[0x1bb] = ..[unsigned int* memory[0x1c7]];
memory[0x1cf] = (QWORD)memory[0x1bb] * (QWORD)[unsigned int* memory[0x1a7]];
memory[0x1c3] = (char*)(..[unsigned int* memory[0x18f]]) + (QWORD)memory[0x1cf];
[QWORD* memory[0x18f]] = memory[0x1c3];
memory[0x1cb] = (int)(..[unsigned int* memory[0x18f]]) % (QWORD)mod/*97A95E7981*/;
[QWORD* memory[0x18f]] = memory[0x1cb];
memory[0x1bf] = (int)[unsigned int* memory[0x19b]] + (int)0x1;
[unsigned int* memory[0x19b]] = memory[0x1bf];
if (0x1) goto L_1b1c; // R_1d12
L_1d1c: // from R_1b74
memory[0x1cf] = sums[ 64 * 0x0  + 8 * [unsigned int* memory[0x17f]]];
memory[0x1cb] = (..[unsigned int* memory[0x18f]]) !=  (..[unsigned int* memory[0x1cf]]);
if (!memory[0x1cb]) goto L_1dec; // R_1da5
memory[0x11] = 0x0 & 1;
if (0x1) goto L_1e9e; // R_1de2
L_1dec: // from R_1da5
memory[0x1bf] = (int)[unsigned int* memory[0x17f]] + (int)0x1;
[unsigned int* memory[0x17f]] = memory[0x1bf];
if (0x1) goto L_1a61; // R_1e5c
L_1e66: // from R_1ab9
memory[0x11] = 0x1 & 1;
L_1e9e: // from R_1de2
return (memory[0x11] & 1);
