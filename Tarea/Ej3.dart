import 'dart:io';

void main() {
  List<int> lista = [];
  int longitud;
  do {
    print('Ingrese el tamaño de la lista:');
    longitud = int.parse(stdin.readLineSync()!);
  } while (longitud <= 0);

  for (int i = 0; i < longitud; i++) {
    int elemento;
    do {
      print('Ingrese el elemento ${i + 1}:');
      elemento = int.parse(stdin.readLineSync()!);
    } while (elemento <= 0);
    lista.add(elemento);
  }
  
  lista.sort();
  print('Lista ordenada ascendentemente:\n$lista');
  lista.sort((a, b) => b.compareTo(a));
  print('Lista ordenada descendentemente:\n$lista');
  
  int min = lista.last;
  int max = lista.first;
  print('Valor máximo de la lista: $max');
  print('Valor mínimo de la lista: $min');
}
