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
	  printf("Fail!\n");
	  return 0;
  }
  v4 = func2((__int64)v9, (__int64)s);
  if ( (v4 & 1) != 0 ) {
	  printf("Success!\n");
  } else {
	  printf("Fail!\n");
  }
  return 0;
}