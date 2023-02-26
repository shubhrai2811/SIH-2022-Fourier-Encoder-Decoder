#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mat.h"

#define charmask 0b11111111

unsigned short noc, nor;
unsigned char* mat;
char* ret;
int * perm;

void char2short(unsigned char* pchar, unsigned short* pshort)
{
  *pshort = (pchar[0] << 8) | pchar[1];
}

void short2char(char* ret, int ctr, int a)//if a is int it just takes two bytes
{
  ret[ctr++] = (char)((a>>8)&charmask)+1;
  ret[ctr++] = (char)(a&charmask)+1;
}

void for_python(binmat_t mat)
{
  int noc = mat->coln;
  int nor = mat->rown;

  int ctr = 0;
  short2char(ret, ctr, noc);
  ctr+=2;
  short2char(ret, ctr, nor);
  ctr+=2;
  for(int i = 0;i<nor;i++)
    {
      for(int j = 0;j<noc;j++)
	if (mat_coeff(mat, i, j) == 1)
	  {
	    short2char(ret, ctr, j);
	    ctr+=2;
	  }

      short2char(ret, ctr, nor);//delimiter
      ctr+=2;
    }
  ret[ctr] = '\0';
}

void print_mat(binmat_t mat)
{
  int noc = mat->coln;
  int nor = mat->rown;

  for(int i = 0;i<nor;i++)
    {
      for(int j = 0;j<noc;j++)
	printf("%d", mat_coeff(mat, i, j));
      printf("\n");
    }
  
}

//str format
//first 4 bytes are two shorts giving the number of cols and rows
//from the each short encountered will be added to the current col
//until the number of rows is encountered. This will be done until
//all coloumns are populated
const char* str_to_mat(char* str)//each number should be a short
{
  ret = malloc(1024);//increase this as necessary
  int cur = 0;
  char2short(str, &noc);
  char2short(str+2, &nor);
  cur = 4;
  
  binmat_t mat = mat_ini(nor, noc);
  mat_set_to_zero(mat);

  int currcol = 0;
  short tmp;
  while(currcol<noc)
    {
      char2short(str+(cur), &tmp);
      cur+=2;
      
      if(tmp!=nor)
	mat_set_coeff_to_one(mat, tmp, currcol);
      else
	currcol++;
    }
  printf("Original Matrix - \n");
  print_mat(mat);

  perm = mat_rref(mat);
    if (perm == NULL) {
       printf("Inside - NUMM\n");
    
   }
  else
    {
      printf("Printing perm :- ");
      for(int i = 0;i<sizeof(perm)/sizeof(perm[0]);i++)
	printf("%d, ", perm[i]);
      printf("\n");
    }
    printf("Printing rrefd matrix - \n");
    print_mat(mat);

    for_python(mat);
    
    return ret;
}
