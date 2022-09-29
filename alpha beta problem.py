function minimax(node, depth, maximizingPlayer) is  
if depth ==0 or node is a terminal node then  
return static evaluation of node  
  
if MaximizingPlayer then      // for Maximizer Player  
maxEva= -infinity            
 for each child of node do  
 eva= minimax(child, depth-1, false)  
maxEva= max(maxEva,eva)        //gives Maximum of the values  
return maxEva  
  
else                         // for Minimizer player  
 minEva= +infinity   
 for each child of node do  
 eva= minimax(child, depth-1, true)  
 minEva= min(minEva, eva)         //gives minimum of the values  
 return minEva  
