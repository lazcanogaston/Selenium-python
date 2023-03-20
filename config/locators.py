class Locators():
    
    # sign in section
    access_btn = '//div[@id="buttons"]//a[@aria-label="Acceder"]'
    use_other_account = '(//div[@title="Google"]/following::div[@class="BHzsHc"])[1]' #not the best option, used just for using node relationships
    signIn_user = '//input[@type="email"]'
    signIn_next_btn = '//button//span[text()="Siguiente"]'
    signIn_pass = '//input[@type="password"]'
    login_btn = '//div[@id="passwordNext"]'
    
    # Home Page
    user_avatar = '//button[@id="avatar-btn"]'
    search_bar = '//form[@id="search-form"]//input[@id="search"]'
    search_btn = '//button[contains(@id, "search-icon-legacy")]'

    #Search results page
    result_titles = '//span[@id="title" and contains(text(), "han visto")]/preceding::a[@id="video-title"]'
