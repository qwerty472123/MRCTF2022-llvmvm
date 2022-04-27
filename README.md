# MRCTF2022-llvmvm writeup

首先的main的内容：

```cpp
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // edx
  char v4; // al
  int v5; // edx
  unsigned int i; // [rsp+Ch] [rbp-54h]
  char s[48]; // [rsp+10h] [rbp-50h] BYREF
  _DWORD v9[6]; // [rsp+40h] [rbp-20h] BYREF
  size_t v10; // [rsp+58h] [rbp-8h]

  v9[5] = 0;
  strcpy((char *)v9, "ezkeyforcipher!!");
  printf("Flag: ");
  __isoc99_scanf("%s", s);
  v10 = strlen(s);
  if (v10 != 32) {
	  printf("Fail!\\n");
	  return 0;
  }
  v4 = func2((__int64)v9, (__int64)s);
  if ( (v4 & 1) != 0 ) {
	  printf("Success!\\n");
  } else {
	  printf("Fail!\\n");
  }
  return 0;
}
```

在比赛时队友写的反汇编的脚本的基础上(加上部分patches，不过理论上还是会在特定情况下出bug)。 

瞎JB实现了一点块内数据流跟踪、控制流去扁平化、死代码消除、去垃圾跳转、跳转目标跟踪、活跃变量分析。

[parser_with_stack.py](./parser_with_stack.py)

得到了239行代码，基本可以看了:

[out2.c](./out2.c)

恢复的逻辑

[func2_logic.py](./func2_logic.py)

用frida Hook function1

[hooker.js](./hooker.js)

hook 结果

[record.txt](./record.txt)

折半搜索背包，求解即可。

后来把function1也给逆了。(分析程序 [parser_with_stack_func1.py](./parser_with_stack_func1.py))

[func1_logic.py](./func1_logic.py)

不需要hook结果的解题脚本

[solver.py](./solver.py)