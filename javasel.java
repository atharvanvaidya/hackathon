import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


public class Test 
{


public static void main(String[] args) throws Exception 
{

        WebDriver driver = new FirefoxDriver();
        driver.manage().deleteAllCookies();
        driver.get("file:///var/www/html/hackathon/helloworld.html");
}
}

