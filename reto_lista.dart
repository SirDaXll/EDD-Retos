import 'dart:io';

List<int> lista(int longitud) {
  List<int> lista = [];

  for (int i = 0; i < longitud; i++) {
    print('Ingrese un número entero para agregar a la lista:');
    String? entrada = stdin.readLineSync();
    int numeroIngresado = int.parse(entrada!);
    lista.add(numeroIngresado);
  }
  return lista;
}
void main() {
  print('Ingrese el tamaño de la lista:');
  String? entrada = stdin.readLineSync();
  int l = int.parse(entrada!);
  List<int> miLista = lista(l);
  print(miLista);
  for (int i = 0; i = lista.length; i++);
}
