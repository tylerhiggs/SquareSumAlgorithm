

# Squares Sum Algorithm
## Tyler Higgs, June 2020



1. Sub Problem
    * $$x(i)$$ = find the smallest number of squared numbers which sum to $i$

\section{Relation}

\begin{itemize}
    \item $x(i) = 1 + \min \{x(i-j^2)\} \ \forall \  j \in \{1,...,\lfloor \sqrt{i} \rfloor \  \}$ 
\end{itemize}

\section{Topological Order}

\begin{itemize}
    \item $i$ always decreases
\end{itemize}

\section{Base}

\begin{itemize}
    \item $x(0) = 0$
\end{itemize}

\section{Original}

\begin{itemize}
    \item $x(n)$ gives the fewest number of square integers which sum to $n$
\end{itemize}

\section{Time}

\begin{itemize}
    \item $O(n)$ sub problems
    \item $O(\sqrt{n})$ work done per sub problem
    \item $O(n\sqrt{n})$ run-time
\end{itemize}

$$


\end{document}
