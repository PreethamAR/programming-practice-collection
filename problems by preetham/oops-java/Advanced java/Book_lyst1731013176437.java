/*
* -----------------------------------------------------------------------------
* 
* Copyright <2024> <algorithms365>
* 
* Professional Coding Skills Workshops
* 
* Licensed under the MIT License:
*  
* https://opensource.org/licenses/MIT
* 
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365 
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://in.linkedin.com/company/algorithms365
* 
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
* 
* -----------------------------------------------------------------------------
*/
// Derived class or Child class 
public class Book extends LibraryItem {
    private int pages;

    public Book(String id, String author, String title, int pages)
    {
        super(id, title, author);
        this.pages = pages;
    }

    @Override 
    public void displayInfo()
    {
        super.displayInfo();
        System.out.println("No of pages: " + this.pages);
    }
    
    public void checkout()
    {
        System.out.println("Checking out the book");
    }
}
