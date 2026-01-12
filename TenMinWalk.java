public class TenMinWalk {
  public static boolean isValid(char[] walk) {
    int Hcount = 0;
    int Vcount = 0;
    if(walk.length != 10){
      return false;
    }
    for(int i = 0; i < walk.length; i++){
      if(walk[i] == 'n'){
        Hcount += 1;
      }
      else if(walk[i] == 's'){
        Hcount -= 1;
      }
      else if(walk[i] == 'w'){
        Vcount += 1;
      }
      else if(walk[i] == 'e'){
        Vcount -= 1;
      }
    }
    
    if(Hcount == 0 && Vcount == 0){
      return true;
    }else{
      return false;
    }
  }
}