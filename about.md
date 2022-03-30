By Ajit Devkota

#### This webpage is currently under construction. Come back soon.

PS: Check out the latex:


\begin{equation}
u_{n+1} = A\:u_n + B\:\dot{u}_{n} +C\:p_n + D\:p_{n+1}
\end{equation}

\begin{equation}
\dot{u}_{n+1} = A_1\:u_n + B_1\:\dot{u}_n + C_1\:p_n + D_1\:p_{n+1}
\end{equation}

where,

\begin{equation}
A = e^{-\xi\omega_nh}\left[\frac{\xi}{\sqrt{1-\xi^2}}\sin(\omega_dh) + \cos(\omega_dh) \right]
\end{equation}

\begin{equation}
B=e^{-\xi\omega_nh}\left[\frac{1}{\omega_d}\sin(\omega_dh) \right]
\end{equation}

\begin{equation}
C=\frac{1}{k}\left[\frac{2\xi}{\omega_nh} + e^{-\xi\omega_nh}\left(\left(\frac{1-2\xi^2}{\omega_dh} - \frac{\xi}{\sqrt{1-\xi^2}} \right)\sin(\omega_dh)-\left(1+\frac{2\xi}{\omega_n h} \right)\cos(\omega_dh)\right) \right]
\end{equation}

\begin{equation}
D=\frac{1}{k}\left[1-\frac{2\xi}{\omega_nh}+e^{-\xi\omega_nh}\left(\frac{2\xi^2-1}{\omega_dh}\sin(\omega_dh) + \frac{2\xi}{\omega_nh}\cos(\omega_dh) \right) \right]
\end{equation}

\begin{equation}
A_1=-e^{-\xi\omega_nh}\left[\frac{\omega_n}{\sqrt{1-\xi^2}}\sin(\omega_dh) \right]
\end{equation}

\begin{equation}
B_1=e^{-\xi\omega_nh}\left[\cos(\omega_dh)-\frac{\xi}{\sqrt{1-\xi^2}}\sin(\omega_dh) \right]
\end{equation}

[Back to homepage](index.md)
