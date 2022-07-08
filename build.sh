#!/bin/sh 

# cd biblioteca
# lib=$(pwd) 
# cd ../comercio/modelos

# echo $lib

cd comercio/modelos

ln -sr ../../biblioteca/endereco.py . 
ln -sr ../../biblioteca/pessoa.py .
ln -sr ../../biblioteca/usuario.py .
ln -sr ../../biblioteca/colaborador.py . 

echo "links criados"