# Geofísica 2: Sismologia, sísmica, métodos elétricos e eletromagnéticos

[![Build Status](https://img.shields.io/travis/lagex/geofisica2/master.svg?style=flat-square)](https://travis-ci.org/lagex/geofisica2)
[![Built with Sphinx](https://img.shields.io/badge/built_with-sphinx-blue.svg?style=flat-square)](http://sphinx-doc.org/)
[![Powered by Bootstrap](https://img.shields.io/badge/powered_by-bootstrap-blue.svg?style=flat-square)](http://getbootstrap.com/)
[![Theme by Bootswatch](https://img.shields.io/badge/theme_by-bootswatch-blue.svg?style=flat-square)](http://bootswatch.com/)

Disciplina Geofísica 2 do curso de Geologia da UERJ.

Este repositório contem o código fonte para compilar o site da disciplina
([lagex.github.io/geofisica2](http://lagex.github.io/geofisica2/)).
O site é gerado pelo sistema [Sphinx](http://sphinx-doc.org/).
Ele converte os arquivos escritos em formato
[reStructuredText](sphinx-doc.org/rest.html)
(os arquivos `.rst`)
para HTML usando o nosso template.

## Requisitos

Para compilar o site, você vai precisar das seguintes bibliotecas:

* sphinx >= 1.2.3
* sphinx-bootstrap-theme == 0.4.5

Instale ambos usando o `pip`:

    pip install sphinx sphinx_bootstrap_theme==0.4.5

## Compilando o site

Use o `Makefile` para compilar o HTML do site.
Rode:

    make

para compilar os arquivos fonte (os `.rst`) para HTML.
O resultado é colocado na pasta `_build/html`.

Para ver o site que você acabou de compilar, rode:

    make serve

O comando `make serve` iniciará um servidor local.
Abra um navegador e vá para [http://127.0.0.1:8003](http://127.0.0.1:8003)
para visualizar o site.
Use `Ctrl+C` para interromper o servidor.

## Atualização automática usando TravisCI

Este site é compilado automaticamente quando um novo *commit* é empurrado para
o branch *master*.
Assim, quando seu Pull Request for aceito e incorporado o site será atualizado
automaticamente.

Veja os arquivos `.travis.yml` e `.push-docs.sh`.
Inspirado nas mágicas por
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
e
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
