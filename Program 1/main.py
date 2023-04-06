    FOR: R[1]=1 To 2
    FOR: R[2]=1 To 2
J   P[4]    100% FINE offset, PR[23]
J   P[5]    100% FINE offset, PR[23]
    CALL VACCM_ON
J   P[6]    100% FINE offset, PR[23]
J   P[1]    100% FINE offset, PR[22]
J   P[2]    100% FINE offset, PR[22]
    CALL VACCUM_OFF
J   P[3]    100% FINE offset, PR[22]
    PR[22,2]=PR[22,2]-71
    PR[23,2]=PR[23,2]-71
    ENDFOR
    PR[22,2]=0 
    PR[22,1]=PR[22,1]-161
    ENDFOR
    PR[22,1]=0
    PR[22,2]=0
    PR[23,2]=0