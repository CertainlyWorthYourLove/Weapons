# პნევმატური იარაღები
<img src='swjf16-air-lead.png'>

-----------------------------------------------------------------------------------------------------------------------------------------------------
  ავირჩიე https://stvol.ua/catalog/pnevmatika/?PAGEN_1=1 საიტი, რომელზეც განთავსებული იყო პნევმატური იარაღები და გადავწყვიტე, რომ წამომეღო იარაღების დასახელებები თავისი ფასით. შესაბამისად, კავშირის დასამყარებლად ვიყენებ requests მოდულს, ასევე bs4 მოდულის BeautifulSoup ბიბლიოთეკას, რომლის საშუალებითაც ვახორციელებ html parsing-ს და ვწვდები სასურველ ინფორმაციას. 

  სერვერზე request-ებს შორის ლოგიკური ხანგრძლივობისთვის ვიყენებ time მოდულიდან sleep() ფუნქციას, რომელსაც არგუმენტად გადავცემ random მოდულის randint() ფუნქციას,რათა სერვერს დავუკავშირდე სხვადასხვა ლოგიკური დროის შუალედებით და განვახორციელო "ლოგიკური" paging(ინფორმაცია მომაქვს 5გვერდიდან). გარდა ამისა, ვიყენებ sqlite3 მოდულს, რომლითაც მონაცემთა ბაზაში ვათავსებ მიღებულ მონაცემებს.
  
  
