#2. Indique la palabra que aparece mayor cantidad de veces en el texto del `README.md` de numpy. 
#Copie y pegue el texto en una varible. 

from collections import Counter

readme = """NumPy is the fundamental package for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest and hypothesis. Tests can then be run after installation with:

python -c "import numpy, sys; sys.exit(numpy.test() is False)"
Code of Conduct
NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for guidance on how to interact with others in a way that makes our community thrive.

Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
help us stay on top of new and old issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
For more information about the ways you can contribute to NumPy, visit our website. If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invitation).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved."""

count = Counter()

#utilizo el método replace para poder sacar los saltos de línea en caso de que los haya y
#lower, para que me tome las palabras que son iguales aunque una esté escrita en mayúscula y la otra no.

text = readme.replace('\n','').lower().split(' ')
for word in text:
    count[word] += 1

#muestraa en pantalla la palabra que más veces se repite en el texto usitlizando most_common
print("La palabra que más veces aparece en el texto es: ", count.most_common(1)[0][0])