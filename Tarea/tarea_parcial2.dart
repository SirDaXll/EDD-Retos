import 'dart:math';

void main(){
  final random = Random();
  // Longitud aleatoria entre 10 y 30
  final length = random.nextInt(21) + 10;
  // Elementos aleatorios entre 0 y 10
  final List<int> arreglo = List.generate(length, (_) => random.nextInt(11));

  print('Arreglo generado:\n$arreglo');
  arreglo.sort();
  print('\nArreglo ordenado ascendentemente:\n$arreglo');

  // Ordenar de manera aleatoria
  for (var i = 0; i < arreglo.length; i++){
    final index1 = random.nextInt(arreglo.length);
    final index2 = random.nextInt(arreglo.length);
    final temp = arreglo[index1];
    arreglo[index1] = arreglo[index2];
    arreglo[index2] = temp;
  }
  print('\nArreglo ordenado de manera aleatoria:\n$arreglo');
}