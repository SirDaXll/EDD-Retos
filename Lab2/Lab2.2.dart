import 'dart:math';

void main(){
  List<int> Lista1 = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];

  List<int> ListaRandom = [];
  for (int i = 0; i < 10; i++){
    int aux = -(Random().nextInt(5) + 1);
    ListaRandom.add(aux);
  }
}