import time,sys
# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

#image to ASCII generator : https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
cake=cyan + bcyan + '''

           _..._  ,s$$$s.                                                                                          _..._  ,s$$$s.
         .$$$$$$$s$$ss$$$$,                                                                                     .$$$$$$$s$$ss$$$$,
         $$$sss$$$$s$$$$$$$                                                                                     $$$sss$$$$s$$$$$$$
         $$ss$$$$$$$$$$$$$$                                   (             )                                   $$ss$$$$$$$$$$$$$$
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                           '$$$s$$$$$$$$$$$$'
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                           '$$$$$$$$$$$$$$'
            S$$$$$$$$$$$'                             |      |~|           |~|      |                              S$$$$$$$$$$$'
             '$$$$$$$$$'                             |~|     | |           | |     |~|                              '$$$$$$$$$'
               '$$$$$'                               | |     | |           | |     | |                                '$$$$$'
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                '$$$'
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            ;
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         ; 
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a                        ;
                 ',                         ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';                        ',
                  ;                         ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;                         ;
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        ,'
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        ;
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        ',
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         ',
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          ;
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      '
                                     .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                 """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                                                `%%%%%%%'
                                                                 `%%%%%'
                                                                   %%% 
                                                                  %%%%%
                                                               .,%%%%%%%,.
                                                          ,%%%%%%%%%%%%%%%%%%%,

'''
wish='''

 /$$   /$$                                               /$$       /$$             /$$     /$$             /$$                                                      
| $$  | $$                                              | $$      |__/            | $$    | $$            | $$                                                      
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$      | $$$$$$$  /$$  /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$                                  
| $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$| $$  | $$      | $$__  $$| $$ /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$ |____  $$| $$  | $$                                  
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  | $$      | $$  \ $$| $$| $$  \__/  | $$    | $$  \ $$| $$  | $$  /$$$$$$$| $$  | $$                                  
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$      | $$  | $$| $$| $$        | $$ /$$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$                                  
| $$  | $$|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$$      | $$$$$$$/| $$| $$        |  $$$$/| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$                                  
|__/  |__/ \_______/| $$____/ | $$____/  \____  $$      |_______/ |__/|__/         \___/  |__/  |__/ \_______/ \_______/ \____  $$                                  
                    | $$      | $$       /$$  | $$                                                                       /$$  | $$                                  
                    | $$      | $$      |  $$$$$$/                                                                      |  $$$$$$/                                  
                    |__/      |__/       \______/                                                                        \______/                                   
                                                                                                                                                                    
                                                                                                                                                                    



                                           
                                           
__________ ____    ___________  ________   

╔═══╦╗─╔═══╦═══╦═══╦╗
║╔═╗║║─║╔═╗║╔═╗║╔═╗║║
║╚═╝║╚═╣║║║╠╝╔╝╠╝╔╝║║╔╦╦═╗╔══╗
║╔╗╔╣╔╗║║║║║─║╔╝─║╔╣╚╝╬╣╔╗╣╔╗║
║║║╚╣║║║╚═╝║─║║──║║║╔╗╣║║║║╚╝║
╚╝╚═╩╝╚╩═══╝─╚╝──╚╝╚╝╚╩╩╝╚╩═╗║
──────────────────────────╔═╝║
──────────────────────────╚══╝
                                           
                                           
                                           
 >>FROM D1ARK-VA4U3<<<                                                                                          
                                                                                                                                                                    
'''




def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
logop(cake + wish)
