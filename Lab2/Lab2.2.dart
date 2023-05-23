import 'dart:math';

void main(){
  List<int> Lista = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];

  List<int> ListaRandom = [];
  for (int i = 0; i < 10; i++){
    int aux = -(Random().nextInt(5) + 1);
    ListaRandom.add(aux);
  }

  List<int> Resultante = [];

  for (int i = 0; i < Lista.length; i++) {
    int suma = Lista[i] + ListaRandom[i];
    Resultante.add(suma);
  }

  print('Lista resultante de la suma de las listas:');
  print(Resultante);
  
  Resultante.removeAt(6); // Eliminar el séptimo elemento
  Resultante.removeAt(6); // Eliminar el octavo elemento
  
  print('Lista resultante después de eliminar los elementos:');
  print(Resultante);
}