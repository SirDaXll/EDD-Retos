import 'dart:math';
import 'dart:io';

void main() {
  // a.Lista Aleatoria
  List<int> listaAleatoria = [];
  for (int i = 0; i < 5; i++) {
    int aux = Random().nextInt(50) + 1;
    listaAleatoria.add(aux);
  }
  print('\nLista Aleatoria:\n$listaAleatoria\n');

  // b.Lista Definida
  List<int> listaDefinida = [];
  for (int i = 0; i < 5; i++) {
    print('Ingrese un número entero para agregar a la lista:');
    String? entrada = stdin.readLineSync();
    int numeroIngresado = int.parse(entrada!);
    listaDefinida.add(numeroIngresado);
  }
  print('\nLista Definida:\n$listaDefinida');

  // c.Lista Concatenada
  List<int> listaConcatenada = [...listaAleatoria, ...listaDefinida];
  print('\nLista concatenada:\n$listaConcatenada');

  // d.Lista con inserción
  final insertar = [14, 20, 7];
  listaConcatenada.insertAll(6, insertar);
  print('\nLista con elementos insertados:\n$listaConcatenada');

  // e.Promedio de la lista
  int suma = 0;
  for (int numero in listaConcatenada) {
    suma += numero;
  }
  double promedio = (suma / listaConcatenada.length);
  print('\nEl promedio de la lista es:\n$promedio');

  // f.Lista ordenada descendentemente
  listaConcatenada.sort((a, b) => b.compareTo(a));
  print('\nLista ordenada de forma descendente:\n$listaConcatenada');
}
