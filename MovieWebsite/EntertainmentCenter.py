# -*- coding: cp1252 -*-
import media
import fresh_tomatoes
#instances of class movie below this line.
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


phantomMenace = media.Movie("Star Wars: Episode I, The Phantom Menace ",
                     "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to reclaim their old glory.",
                     "https://s-media-cache-ak0.pinimg.com/originals/43/c7/4a/43c74a6bfea9d5ce8337b7d976431fb4.jpg",
                     "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

attackOfClones = media.Movie("Star Wars: Episode II, Attack Of The Clones",
                      "Ten years after initially meeting, Anakin Skywalker shares a forbidden romance with Padmé, while Obi-Wan investigates an assassination attempt on the Senator and discovers a secret clone army crafted for the Jedi.",
                      "https://s-media-cache-ak0.pinimg.com/564x/45/84/96/4584962a4fb1f6ccf1f7f33da4de91eb.jpg",
                      "https://www.youtube.com/watch?v=gYbW1F_c9eM")

revengeOfSith = media.Movie("Star Wars: Episode III, Revenge Of The Sith",
                            "Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku. As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into a sinister plan to rule the galaxy.",
                            "https://hobbydb-production.s3.amazonaws.com/processed_uploads/subject_photo/subject_photo/image/9760/1450470843-3-0920/Star-Wars-Episode-III-Revenge-of-the-Sith-2005.jpg",
                            "https://www.youtube.com/watch?v=5UnjrG_N8hU")

newHope = media.Movie("Star Wars: Episode IV, A New Hope",
                      "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empires world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
                      "https://s-media-cache-ak0.pinimg.com/736x/f3/60/45/f36045d34133eeeb664fa76c5209ed03.jpg",
                      "https://www.youtube.com/watch?v=9gvqpFbRKtQ")

empireStrikesBack = media.Movie("Star Wars: Epidosde V, The Empire Strikes Back",
                                "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
                                "http://img.goldposter.com/2015/04/Star-Wars-Episode-V-The-Empire-Strikes-Back_poster_goldposter_com_13.jpg",
                                "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

returnOfJedi = media.Movie("Star Wars: Episode VI, Return Of The Jedi",
                           "After rescuing Han Solo from the palace of Jabba the Hutt, the rebels attempt to destroy the second Death Star, while Luke struggles to make Vader return from the dark side of the Force.",
                           "http://img.goldposter.com/2015/04/Star-Wars-Episode-VI-Return-of-the-Jedi_poster_goldposter_com_7.jpg",
                           "https://www.youtube.com/watch?v=5UfA_aKBGMc")
                           
                                
                        

#array of movies to be displayed on website
movies = [phantomMenace, attackOfClones, revengeOfSith, newHope, empireStrikesBack, returnOfJedi]
#opens movie website
fresh_tomatoes.open_movies_page(movies)

                                          
                            
                            
            

