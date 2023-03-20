class Locators():
    
    # sign in section
    access_btn = '//div[@id="buttons"]//a[@aria-label="Acceder"]'
    use_other_account = '(//div[@title="Google"]/following::div[@class="BHzsHc"])[1]' #not the best option, used just for using node relationships
    signIn_user = '//input[@type="email"]'
    signIn_next_btn = '//button//span[text()="Siguiente"]'
    signIn_pass = '//input[@type="password"]'
    login_btn = '//div[@id="passwordNext"]'
    
    # Home Page
    yt_logo ='//div[@id="start"]//a[@id="logo"]'
    avatar_btn = '//button[@id="avatar-btn"]'
    log_out_btn = '//*[text() = "Cerrar sesión"]'
    user_avatar = '//button[@id="avatar-btn"]'
    search_bar = '//form[@id="search-form"]//input[@id="search"]'
    search_btn = '//button[contains(@id, "search-icon-legacy")]'

    #Search results page
    result_titles = '//span[@id="title" and contains(text(), "han visto")]/preceding::a[@id="video-title"]'
    result_titles_notLogged = '//span[@id="title" and contains(text(), "vieron")]/preceding::a[@id="video-title"]'
    like_btn = '//div[@id="actions"]//div[@id="segmented-like-button"]//button'
    dislike_btn = '//div[@id="actions"]//div[@id="segmented-dislike-button"]//button'
    accept_modal_btn = '//div[contains(@class, "modal")]//a[@aria-label="Acceder"]'
