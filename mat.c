#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "mat.h"

//take a look at the MSB-LSB format???

binmat_t mat_ini (int rown, int coln)
{
  binmat_t A;

  A = (binmat_t) malloc (sizeof (struct matrix));
  A->coln = coln;
  A->rown = rown;  
  A->rwdcnt = (1 + (coln - 1) / BITS_PER_LONG);
  A->alloc_size = rown * A->rwdcnt * sizeof (unsigned long);
  A->elem = (unsigned long *)malloc(A->alloc_size);
  return A;
}

// assumes s has the proper allocated size
binmat_t mat_ini_from_string(int rown, int coln, const unsigned char * s)
{
  binmat_t A;

  A = (binmat_t) malloc (sizeof (struct matrix));
  A->coln = coln;
  A->rown = rown;  
  A->rwdcnt = (1 + (coln - 1) / BITS_PER_LONG);
  A->alloc_size = rown * A->rwdcnt * sizeof (unsigned long);
  A->elem = (unsigned long *) s;

  fflush(stdout);
  return A;
}

void mat_free(binmat_t A)
{
  free(A->elem);
  free(A);
}

binmat_t mat_copy(binmat_t A)//copying matrix (for the form [G|I].....)
{
  binmat_t X;
  int i;
  
  X=mat_ini(A->rown,A->coln);//initialize the matrix.
  for(i=0;i<((A->rwdcnt)*(A->rown));i++)
    X->elem[i]=A->elem[i];

  return(X);
}

binmat_t mat_rowxor(binmat_t A,int a, int b)
{
  int i;
  for(i=0;i<A->rwdcnt;i++)
    {
      A->elem[a*A->rwdcnt+i]^=A->elem[b*A->rwdcnt+i];
    }
  return A;
}

//the matrix is reduced from LSB...(from right)


int * mat_rref(binmat_t A)
{
  printf("INSIDE - rref\n");
  int i,j,failcnt,findrow,max=A->coln - 1;
  int *perm;
  fflush(stdout);
  perm = malloc(A->alloc_size);
  fflush(stdout);
  for(i=0;i<A->coln;i++)
    perm[i]=i;//initialize permutation.
  failcnt = 0;
  int ctr = 0;
  for(i=0;i<A->rown;i++,max--)
    {
      findrow=0;
      for(j=i;j<A->rown;j++)
        {
          if(mat_coeff(A,j,max))//(A->elem[(j*A->coln)+max])
            {
              //max--;
	      printf("checking %d row with %d row\n", i, j);
              if (i!=j)//not needed as ith row is 0 and jth row is 1.
		{
		  printf("xoring %d row with %d row\n", i, j);
		  A=mat_rowxor(A,i,j);//xor to the row.(swap)?
		}
              findrow=1;
              break;
            }//largest value found (end if)
          //              break;
        }
      
      if(!findrow)//if no row with a 1 found then swap last column and the column with no 1 down.
        {
          perm[A->coln - A->rown - 1 - failcnt] = max;
          failcnt++;
          if (!max)
            {
              return NULL;
            }
          i--;
        }
      else
        {
          perm[i+A->coln - A->rown] = max;
          for(j=i+1;j<A->rown;j++)//fill the column downwards with 0's
            {
              if(mat_coeff(A,j,(max)))//(A->elem[j*A->coln+max+1])
                A=mat_rowxor(A,j,i);//check the arg. order.
            }

          for(j=i-1;j>=0;j--)//fill the column with 0's upwards too.
            {
              if(mat_coeff(A,j,(max)))//(A->elem[j*A->coln+max+1])
                A=mat_rowxor(A,j,i);
            }
        }
    }//end for(i)

  return(perm);
}

void mat_vec_mul(unsigned long *cR, unsigned char *x, binmat_t A)
{
  int i,j;
  unsigned long *pt;

  memset(cR,0,A->rwdcnt*sizeof(long));
  pt = A->elem;
  for(i=0;i<A->rown;i++)//extract the first column in the form of char array.
    {
      if((x[i/8]>>(i%8))&1)
        for (j = 0; j < A->rwdcnt; ++j)
          cR[j] ^= *pt++;
      else
        pt += A->rwdcnt;
    }
}

binmat_t mat_mul(binmat_t A, binmat_t B)
{
  binmat_t C;
  int i,j,k;

  if (A->coln != B->rown)
    exit(0);

  C = mat_ini(A->rown, B->coln);
  memset(C->elem,0,C->alloc_size);
  for(i=0;i<A->rown;i++)
    for(j=0;j<B->coln;j++)
      for (k = 0; k < A->coln; ++k)
        if (mat_coeff(A,i,k) && mat_coeff(B,k,j))
          mat_change_coeff(C,i,j);

  return C;
}
