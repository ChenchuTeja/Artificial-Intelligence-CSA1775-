%solve(goal,solution path)
%s(state,succesor-state)
dfs(N,[N]):-goal(N).
dfs(N,[N|Sol1]):- s(N,N1), dfs(N1,sol1).
s(a,b).s(a,c).s(c,d).s(b,d).s(d,e).s(e,f).s(f,g).s(g,h).s(h,i).s(i,j).goal(i).goal(j).

