def pPow(bBase,eExp):

if eExp <= 0:

return 1

else:

return bBase * pPow(bBase,eExp-1)

