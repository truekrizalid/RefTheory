def  f(x, c):
    m1 = np.sin(2*np.pi*x)
    m2 = np.exp(-c*x)
    return m1*m2
x = np.linspace(0, 4, 100)
sigma = 0.5
plt.plot(x, f(x, sigma), 'r', linewidth=2)
plt.xlabel(r'$\rm{time}  \  t$', fontsize=16)
plt.ylabel(r'$\rm{Amplitude} \ f(x)$', fontsize=16)
plt.title(r'$f(x) \ \rm{is \ damping  \ with} \ x$', fontsize=16)
plt.text(2.0, 0.5, r'$f(x) = \rm{sin}(2 \pi  x^2) e^{\sigma x}$', fontsize=20)
plt.savefig('latex.png', dpi=75)
plt.show()
