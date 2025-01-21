import java.util.Random;

public class Ghost {
  Random rand = new Random();
  String[] colors = {"white", "yellow", "purple", "red"};
  String color = colors[rand.nextInt(4)];
  
  public String getColor(){
    return color;
  }
}