import streamlit as st
import numpy as np

# personality characteristics
c = [ ["I","E"], ["S","N"], ["F","T"], ["J","P"] ]
questions = [
    "Do you feel comfortable and happy when you are alone in a quiet place?",#0
    "Do you feel stressed and anxious in crowded places?",#1
    "Do you feel exhausted after spending time with a large number of people?",#2
    "Do you prefer working alone more than in a team?",#3
    "Do you find comfort in dealing with deep, complex feelings and thoughts?",#4
    "Do you prefer clear chores and tasks that require tangible skills?",#5
    "Do you enjoy sensory-based activities such as sports?",#6
    "Do you prefer to work within clear systems and laws?",#7
    "Do you prefer hard facts over theories and guesswork?",#8
    "Do you rely on your experience from previous experiences to make decisions?",#9
    "Does the emotional side of things affect your daily thinking and behavior?",#10
    "Do you pay great attention to personal relationships with others?",#11
    "Do you consider understanding and expressing feelings important to you?",#12
    "Do you easily recognize and understand the feelings of others?",#13
    "Do you find it difficult to separate emotions from logical decisions?",#14
    "Do you maintain a clear vision of your goals and actively work to achieve them?",#15
    "Do you find it difficult to change and move from one situation to another quickly?",#16
    "Do you make decisions with confidence and stick to them strictly?",#17
    "Do you care about planning and organization and like to stick to scheduling and routines?",#18
    "Do you prefer stability in work and life rather than constant change?",#19
    ]
info = {
    "INTJ":"""The Mastermind
    
    INTJ in a Nutshell
    
INTJs are analytical problem-solvers, eager to improve systems and processes with their innovative ideas. They have a talent for seeing possibilities for improvement, whether at work, at home, or in themselves.

Often intellectual, INTJs enjoy logical reasoning and complex problem-solving. They approach life by analyzing the theory behind what they see, and are typically focused inward, on their own thoughtful study of the world around them. INTJs are drawn to logical systems and are much less comfortable with the unpredictable nature of other people and their emotions. They are typically independent and selective about their relationships, preferring to associate with people who they find intellectually stimulating.

INTJ Values and Motivations

INTJs are perceptive about systems and strategy, and often understand the world as a chess board to be navigated. They want to understand how systems work, and how events proceed: the INTJ often has a unique ability to foresee logical outcomes. They enjoy applying themselves to a project or idea in depth, and putting in concentrated effort to achieve their goals.

INTJs have a hunger for knowledge and strive to constantly increase their competence; they are often perfectionists with extremely high standards of performance for themselves and others. They tend to have a keen interest in self-improvement and are lifelong learners, always looking to add to their base of information and awareness.

How Others See the INTJ

INTJs are typically reserved and serious, and seem to spend a lot of time thinking. They are curious about the world around them and often want to know the principle behind what they see. They thoroughly examine the information they receive, and if asked a question, will typically consider it at length before presenting a careful, complex answer. INTJs think critically and clearly, and often have an idea about how to do something more efficiently. They can be blunt in their presentation, and often communicate in terms of the larger strategy, leaving out the details.

Although INTJs aren’t usually warm or particularly gregarious, they tend to have a self-assured manner with people based on their own security in their intelligence. They relate their ideas with confidence, and once they have arrived at a conclusion they fully expect others to see the wisdom in their perceptions. They are typically perfectionists and appreciate an environment of intellectual challenge. They enjoy discussing interesting ideas, and may get themselves into trouble because of their take-no-prisoners attitude: if someone’s beliefs don’t make logical sense, the Mastermind typically has no qualms about pointing that out.

How Rare Is the INTJ Personality Type?

INTJ is one of the rarest types in the population. INTJs make up:

2.6% of the general population

3% of men

2.2% of women

Famous INTJs

Famous INTJs include:

Jane Austen

Ruth Bader Ginsburg

Dwight Eisenhower

Mark Zuckerberg

Alan Greenspan

Ulysses S. Grant

Stephen Hawking

Hillary Clinton

Al Gore

John Maynard Keynes

Ayn Rand

Isaac Asimov

Lewis Carroll

Cormac McCarthy

Sir Isaac Newton

Facts About INTJs

Interesting facts about the INTJ:

On personality trait measures, score as Discreet, Industrious, Logical, Deliberate, Self-Confident, and Methodical
Among types least likely to suffer heart disease and cardiac problems
Least likely of all the types to believe in a higher spiritual power
One of two types with highest college GPA
Among types with highest income
Personal values include Achievement
Of all types, least likely to state that they value Home/family, Financial security, Relationships & friendships, and Community service
Overrepresented among MBA students and female small business owners
Commonly found in scientific or technical fields, computer occupations, and legal professions

INTJ Hobbies and Interests

Popular hobbies for the INTJ include reading, cultural events, taking classes, appreciating art, computers and video games, and independent sports such as swimming, backpacking, or running marathons.""",
    "INFJ":"""The Counselor

INFJ in a Nutshell

INFJs are thoughtful nurturers with a strong sense of personal integrity and a drive to help others realize their potential. Creative and dedicated, they have a talent for helping others with original solutions to their personal challenges.

The Counselor has a unique ability to intuit others' emotions and motivations, and will often know how someone else is feeling before that person knows it himself. They trust their insights about others and have strong faith in their ability to read people. Although they are sensitive, they are also reserved; the INFJ is a private sort, and is selective about sharing intimate thoughts and feelings.

INFJs search for meaning and purpose in their lives and in the outer world. They tend to have an immense interest in deeply understanding culture, society, and the universe as a whole. INFJs naturally see how every thought or action could potentially have important consequences, either positive or negative. This reflective and curious worldview gives INFJs a unique perspective and thoughtful approach to how they interact with others and the world around them.

Ultimately, INFJs seek to turn their abstract and intellectual musings into concrete actions that can be applied and make a transformative impact on others. Although it is common for INFJs to get stuck in their heads and struggle with taking action, when they are at their best, their actions are aligned with their authentic values.

INFJ Values and Motivations

INFJs are guided by a deeply considered set of personal values. They are intensely idealistic, and can clearly imagine a happier and more perfect future. They can become discouraged by the harsh realities of the present, but they are typically motivated and persistent in taking positive action nonetheless. The INFJ feels an intrinsic drive to do what they can to make the world a better place.

INFJs want a meaningful life and deep connections with other people. They do not tend to share themselves freely but appreciate emotional intimacy with a select, committed few. Although their rich inner life can sometimes make them seem mysterious or private to others, they profoundly value authentic connections with people they trust.

As quintessential idealists, INFJs have many ideas about how to improve society and make the world a better place. INFJs believe a better world can only be attained if we concentrate on doing what is right, regardless of short-term consequences. However, harmonious relationships are also extremely important to the INFJ. They are skilled mediators who look for the root sources of conflict to find common ground with others. Because of this, they tend to prefer a diplomatic communication style and are careful to not unnecessarily ruffle feathers.

INFJs have a profound respect for human potential and a deep interest in understanding the mind. Because of this, they are motivated to pursue authentic self-development and strive to live up to their true potential, while encouraging and guiding others to do the same. According to idealistic INFJs, if we believe in our ability to accomplish the extraordinary, the extraordinary will instantly become a possibility — “dream it and you can achieve it,” as the saying goes. However, because of their integrity and empathy for others, it is uncommon for INFJs to cut corners or hurt others to achieve their desired future state.

How Others See the INFJ

INFJs often appear quiet, caring and sensitive, and may be found listening attentively to someone else’s ideas or concerns. They are highly perceptive about people and want to help others achieve understanding. INFJs are not afraid of complex personal problems; in fact, they are quite complex themselves, and have a rich inner life that few are privy to. They reflect at length on issues of ethics, and feel things deeply. Because Counselors initially appear so gentle and reserved, they may surprise others with their intensity when one of their values is threatened or called into question. Their calm exterior belies the complexity of their inner worlds.

Because INFJs are such complex people, they may be reluctant to engage with others who might not understand or appreciate them, and can thus be hard to get to know. Although they want to get along with others and support them in their goals, they are fiercely loyal to their own system of values and will not follow others down a path that does not feel authentic to them. When they sense that their values are not being respected, or when their intuition tells them that someone’s intentions are not pure, they are likely to withdraw.

Acquaintances of INFJs would likely describe them as quiet, intelligent, serious, gentle, and possibly a bit reclusive. Others generally perceive INFJs as pleasant people to be around, but may also notice that they can be moody, aloof, or even somewhat crabby on occasion. All in all, people who only encounter them infrequently are likely to see INFJs as tough nuts to crack and may even find them to be a bit intimidating.

Those closer to an INFJ will likely see beneath the surface and recognize the INFJs depth of empathy and their curious and insightful nature. When family members, friends or trusted co-workers need constructive feedback and a fresh perspective, INFJs are always standing by, ready to offer sensible and helpful input.

INFJs like to put out fires, not start them. When they occupy positions on work teams, non-profit boards, PTAs, city councils, organizing committees or task forces, others learn to appreciate their uncanny ability to defuse tensions, soothe wounded feelings, smooth ruffled feathers, arbitrate petty squabbles and restore the spirit of cooperation whenever it has been compromised.

How Rare Is the INFJ Personality Type?

INFJ is one of the rarest types in the population. It is the least common type among men and the third least common among women (after INTJ and ENTJ). INFJs make up:

2.3% of the general population

3.1% of women

1.4% of men

Famous INFJs

Famous INFJs include:

Mohandas Gandhi

Eleanor Roosevelt

Emily Bronte

Jane Goodall

Carl Jung

Fyodor Dostoevsky

Florence Nightingale

Shirley MacLaine

Jimmy Carter

Brené Brown

Edward Snowden

J.K. Rowling

Marianne Williamson

Facts About INFJs

Interesting facts about the INFJ:

Least common type in the population
On personality trait scales, scored as Sincere, Sympathetic, Unassuming, Submissive, Easygoing, Reserved and Patient
Among highest of all types in college GPA
Among most likely to stay in college
Most likely of all types to cope with stress by seeing a therapist
Highest of all types in marital dissatisfaction
Personal values include Spirituality, Learning, and Community Service
Commonly found in careers in religion, counseling, teaching, and the arts

INFJ Hobbies and Interests

Popular hobbies for the INFJ include writing, art appreciation, cultural events, reading, socializing in small, intimate settings, and playing or listening to music.""",
    "INTP":"""The Architect

    INTP in a Nutshell

INTPs are philosophical innovators, fascinated by logical analysis, systems, and design. They are preoccupied with theory, and search for the universal law behind everything they see. They want to understand the unifying themes of life, in all their complexity.

INTPs are detached, analytical observers who can seem oblivious to the world around them because they are so deeply absorbed in thought. They spend much of their time in their own heads: exploring concepts, making connections, and seeking understanding of how things work. To the Architect, life is an ongoing inquiry into the mysteries of the universe.

INTP Values and Motivations

INTPs present a cool exterior but are privately passionate about reason, analysis, and innovation. They seek to create complex systems of understanding to unify the principles they've observed in their environments. Their minds are complicated and active, and they will go to great mental lengths trying to devise ingenious solutions to interesting problems.

The INTP is typically non-traditional, and more likely to reason out their own individual way of doing things than to follow the crowd. The INTP is suspicious of assumptions and conventions, and eager to break apart ideas that others take for granted. INTPs are merciless when analyzing concepts and beliefs, and hold little sacred. They are often baffled by other people who remain loyal to ideology that doesn't make logical sense.

How Others See the INTP

INTPs are often thoroughly engaged in their own thoughts, and usually appear to others to be offbeat and unconventional. The INTP’s mind is a most active place, and their inward orientation can mean that they neglect superficial things like home décor or appropriate clothing. They don’t tend to bother with small talk but can become downright passionate when talking about science, mathematics, computers, or the larger theoretical problems of the universe. Reality is often of only passing interest to the Architect, as they are more interested in the theory behind it all. INTPs are typically precise in their speech, and communicate complex ideas with carefully chosen words. They insist on intellectual rigor in even the most casual of conversations, and will readily point out inconsistencies of thought or reasoning. Social niceties may fall by the wayside for an INTP who is more interested in analyzing logic, and they may offend others by submitting their dearly held values and beliefs to logical scrutiny.

How Rare Is the INTP Personality Type?

INTP is one of the less common types in the population. INTPs make up:

4.8% of the general population

5.8% of men

4% of women

Famous INTPs

Famous INTPs include:

Albert Einstein

Kristen Stewart

Elon Musk 

Tina Fey

Jesse Eisenberg

Rene Descartes

Charles Darwin

Marie Curie

Socrates

Abraham Lincoln

Facts About INTPs

Interesting facts about the INTP:

On personality trait measures, score as Candid, Ingenious, Complicated, Independent, and Rebellious
More likely than other types to study a foreign language
Most frequent type among college students committing alcohol and drug policy violations
Have lowest level of coping resources of all the types (with ISTPs)
One of types least likely to believe in a higher spiritual power
Highest of all types in career dissatisfaction (with INFPs)
In school, have lower grades than would be predicted from aptitude scores
More likely than average to complete engineering programs
Personal values include Autonomy, Freedom, and Independence
Overrepresented among working MBA students
Commonly found in science and technical occupations

INTP Hobbies and Interests

Popular leisure activities for an INTP include reading, art and cultural events, chess and other strategy games, writing, taking classes, working with computers, backpacking, hiking, and meditation.""",
    "INFP":"""The Healer

    INFP in a Nutshell

INFPs are imaginative idealists, guided by their own core values and beliefs. To a Healer, possibilities are paramount; the realism of the moment is only of passing concern. They see potential for a better future, and pursue truth and meaning with their own individual flair.

INFPs are sensitive, caring, and compassionate, and are deeply concerned with the personal growth of themselves and others. Individualistic and nonjudgmental, INFPs believe that each person must find their own path. They enjoy spending time exploring their own ideas and values, and are gently encouraging to others to do the same. INFPs are creative and often artistic; they enjoy finding new outlets for self-expression.

INFP Values and Motivations

INFPs value authenticity and want to be original and individual in what they do. They are often concerned with a search for meaning and truth within themselves. Following tradition holds little appeal for the INFP; they prefer to do their own exploration of values and ideas, and decide for themselves what seems right. INFPs are often offbeat and unconventional, but they feel no desire to conform. The INFP would rather be true to themselves than try to fit in with the crowd.

INFPs are accepting and nonjudgmental in their treatment of others, believing that each person must follow their own path. They are flexible and accommodating, and can often see many points of view. It is important to the INFP to support other people; however, the INFP may react strongly if they feel their own values are being violated. They especially hate being steamrolled by people who insist there is one right way to do things. INFPs want an open, supportive exchange of ideas.

How Others See the INFP

INFPs may initially seem cool, as they reserve their most authentic thoughts and feelings for people they know well. They are reflective and often spiritual, and often interested in having meaningful conversations about values, ethics, people, and personal growth. Typically curious and open-minded, the Healer continually seeks a deeper understanding of themselves and of the people around them. They are passionate about their ideals, but private as well; few people understand the depth of the INFP’s commitment to their beliefs. INFPs are sensitive and empathetic, and engage themselves in a lifelong quest for meaning and authenticity. The mundane aspects of life are of less interest to this type, and they are more excited by interesting ideas than by practical facts. They typically accept others without question, and may take special interest in offbeat points of view or alternative lifestyles. They often have a special affection for the arts, especially the avant garde, as they love experiencing new concepts in self-expression.

How Rare Is the INFP Personality Type?

INFPs make up:

6.3% of the general population

7.6% of women

4.9% of men

Famous INFPs

Famous INFPs include:

Audrey Hepburn

Winona Ryder

Alicia Keys 

John Lennon

Kim Tae-hyung (V)

Kurt Cobain

Keanu Reeves

Tori Amos

Morrissey

Chloe Sevigny

William Shakespeare

Bill Watterson

A.A. Milne

Helen Keller

Carl Rogers

Isabel Briggs Myers (creator of the Myers-Briggs Type Indicator)

Facts About INFPs
Interesting facts about the INFP:

On personality trait measures, score as Artistic, Reflective, Careless, Sensitive, Flexible, and Appreciative
Among least likely of all types to suffer heart disease
In men, among least likely to report chronic pain
Second highest of all types to report marital dissatisfaction
Among most likely to have suicidal thoughts in college
Tend to be more successful than the average in learning a foreign language
Among types most likely to be dissatisfied with their work
Personal values include Autonomy and Creativity
Overrepresented in occupations in counseling, writing, and the arts

INFP Hobbies and Interests

Popular hobbies for INFPs include poetry, creative writing, music, photography, theater, and visual art.""",
    "ISTJ":"""The Inspector

    ISTJ in a Nutshell

ISTJs are responsible organizers, driven to create and enforce order within systems and institutions. They are neat and orderly, inside and out, and tend to have a procedure for everything they do. Reliable and dutiful, ISTJs want to uphold tradition and follow regulations.

ISTJs are steady, productive contributors. Although they are Introverted, ISTJs are rarely isolated; typical ISTJs know just where they belong in life, and want to understand how they can participate in established organizations and systems. They concern themselves with maintaining the social order and making sure that standards are met.

ISTJ Values and Motivations

ISTJs like to know what the rules of the game are, valuing predictability more than imagination. They rely on their past experience to guide them, and are most comfortable in familiar surroundings. ISTJs trust the proven method, and appreciate the value of dedicated practice to build confidence in their skills.

ISTJs are hardworking and will persist until a task is done. They are logical and methodical, and often enjoy tasks that require them to use step-by-step reasoning to solve a problem. They are meticulous in their attention to details, and examine things closely to be sure they are correct. With their straightforward logic and orientation to detail, ISTJs work systematically to bring order to their own small parts of the world.

How Others See the ISTJ

ISTJs have a serious, conservative air about them. They want to know and follow the rules of the game, and typically seek out predictable surroundings where they understand their role. You may find the ISTJ doing something useful even in social situations (for instance, organizing coats and hats at a party) as they’re often more comfortable taking charge of a task than they are chatting up strangers. When given something to do, they are highly dependable, and follow it through to the end. ISTJs are practical and no-nonsense, and rarely call attention to themselves. Their clothes and possessions tend to be chosen based on utility rather than fashion, and they have an affection for the classics. ISTJs typically speak in a straightforward manner and have a good head for details. They are usually more enthusiastic about sharing factual information than exploring abstract concepts or unproven ideas.

How Rare Is the ISTJ Personality Type?

According to the most recent global sample, ISTJ is the most common type in the population. ISTJs make up:

15.9% of the general population

18.9% of men

13.3% of women

Famous ISTJs

Famous ISTJs include: 

Queen Elizabeth II

Harry Truman

Warren Buffett

Jeff Bezos 

Natalie Portman

Matt Damon 

George Strait

Amal Clooney

Robert DeNiro 

Denzel Washington 

Queen Victoria

Angela Merkel 

Condoleezza Rice

George H.W. Bush

J.D. Rockefeller

Henry Ford

Facts About ISTJs

Interesting facts about the ISTJ:

On personality trait measures, score as Calm, Stable, Steady, Cautious, and Conventional

More likely than other types to experience cardiac problems and hypertension

More likely than other types to experience chronic pain

Among four highest types in college GPA

More frequent among African Americans

Personal values include Financial Security

Most likely of all types to enjoy a work environment where “everything is done by the book”

Overrepresented among bank officers, financial managers, MBA students, and small business owners

Often found in careers in management, administration, law enforcement, and accounting

ISTJ Hobbies and Interests

Popular hobbies for the ISTJ include concentration games like chess and Trivial Pursuit, playing computer games, watching sporting events, pursuing physical fitness, and playing solitary sports such as golf.""",
    "ISFJ":"""The Protector
    
    ISFJ in a Nutshell

ISFJs are industrious caretakers, loyal to traditions and organizations. They are practical, compassionate, and caring, and are motivated to provide for others and protect them from the perils of life.

ISFJs are conventional and grounded, and enjoy contributing to established structures of society. They are steady and committed workers with a deep sense of responsibility to others. They focus on fulfilling their duties, particularly when they are taking care of the needs of other people. They want others to know that they are reliable and can be trusted to do what is expected of them. They are conscientious and methodical, and persist until the job is done.

ISFJ Values and Motivations

ISFJs are driven by their personal values, and are conscientious in their behavior. They typically want to work hard, get along with others, and make sure they do what is expected of them.

ISFJs value relationships highly and strive to cooperate and maintain harmony with others. They want stability and longevity in their relationships, and tend to maintain a deep devotion to family. They feel most connected with people they know they can rely upon over the long term.

ISFJs appreciate tradition and like knowing how things were done in the past. They are loyal to established methods and values, and want to observe the proper, accepted way of doing things. They place great importance on fitting in with established institutions and contributing what they can to maintain strong, stable social structures. In groups, they often take on the role of historian, ensuring that new members respect and value the established customs.

How Others See the ISFJ

ISFJs are characteristically humble and unassuming, and rarely call attention to themselves. They can often be found offering assistance to others in a modest, understated way. They are loyal and hardworking, and often commit themselves to tasks and projects with the aim of being helpful to their families, friends, and communities. They are typically involved in social groups, but do not want the spotlight: they are more likely to be found behind the scenes, working diligently to fulfill their role. ISFJs are oriented to relationships, but can be reserved with new people. They rarely disclose personal information quickly. They tend to be focused and aware of their surroundings, and relate details from their own personal experience. They often converse in terms of what has happened to them and what they have seen first-hand. They are compassionate listeners, and typically remember details about people. They often enjoy hearing the facts about others in the process of making a connection.
For more information: The Art of SpeedReading People

How Rare Is the ISFJ Personality Type?

ISFJ is one of the most common types in the population. ISFJs make up:

8.4% of the general population

11.3% of women

4.9% of men

Famous ISFJs

Famous ISFJs include: 

Aretha Franklin

Mother Teresa

Beyoncé

Laura Bush

King George VI

Kate Middleton

Rosa Parks

Fred Rogers

Selena Gomez

Elijah Wood

Princess Mary of Denmark

Clara Barton

Naomi Watts

Facts About ISFJs
Interesting facts about the ISFJ:

On personality trait measures, score as Conservative, Conventional, Guarded, and Reserved
Among types most likely to believe in a higher spiritual power
More likely than average to experience chronic pain
Among types most likely to suffer heart disease
Second most common type among education majors in college
More likely than other types to watch more than 3 hours of television per day
Personal values include Happy family, Health and Spirituality
Overrepresented among MBA students and male small business owners
Among three types with the lowest income
Commonly found in education, health care, and religious occupations

ISFJ Hobbies and Interests

Popular leisure activities for ISFJs include cooking, gardening, painting, crafts, picnics, nature walks, and watching movies. They are also often found supporting their loved ones in their interests and activities.""",
    "ISTP":"""The Craftsman

    ISTP in a Nutshell

ISTPs are observant artisans with an understanding of mechanics and an interest in troubleshooting. They approach their environments with a flexible logic, looking for practical solutions to the problems at hand. They are independent and adaptable, and typically interact with the world around them in a self-directed, spontaneous manner.

ISTPs are attentive to details and responsive to the demands of the world around them. Because of their astute sense of their environment, they are good at moving quickly and responding to emergencies. ISTPs are reserved, but not withdrawn: the ISTP enjoys taking action, and approaches the world with a keen appreciation for the physical and sensory experiences it has to offer.

ISTP Values and Motivations

ISTPs are curious about the mechanics of the world around them and typically have a unique ability to manipulate the tools in their environments. They tend to study how things work and often achieve mastery in the use and operation of machines, instruments, and equipment. They seek understanding, but in a practical sense: they like to be able to put their technical knowledge to immediate use and are quickly bored by theory.

ISTPs tend to be detached and prefer the logic of mechanical things to the complexity of human emotions. Independent and reserved, ISTPs treasure their personal space, and want to be free to be spontaneous and follow their own lead. ISTPs are selective about their relationships, and appreciate others who allow them plenty of freedom to do their own thing.

How Others See the ISTP

ISTPs are typically reserved and even aloof. Tolerant and nonjudgmental, the ISTP calmly takes in the details and facts of their surroundings, noticing sensory data and observing how things work. They often tune into what needs to be done, taking care of the immediate needs of the moment in a modest, inconspicuous way. They tend to prefer action to conversation, and are often private about their personal lives. ISTPs are unlikely to “open up” to new people in a conventional way, but may connect with others by sharing an activity or working together to solve a practical problem. ISTPs are good with their hands and often mechanical. They are typically attracted to hands-on hobbies like woodworking or crafts, and may be found tinkering with bicycles, computers, cars, or household appliances. They often have an intuitive understanding of machines and a remarkable ability to fix things. ISTPs have an appreciation for risk and action, and often enjoy thrilling leisure activities like extreme sports, motorcycling, or weaponry.

How Rare Is the ISTP Personality Type?

The ISTP personality type is much more common among men than women. ISTPs make up:

9.8% of the general population

13.3% of men

6.8% of women

Famous ISTPs

Famous ISTPs include:

Lance Armstrong

Venus Williams

Billie Eilish

Bruce Lee

Snoop Dogg

Miles Davis

Willie Nelson

Tiger Woods

Chuck Yaeger

Katherine Hepburn

Clint Eastwood

Amelia Earhart

Facts About ISTPs
Interesting facts about the ISTP:

On personality trait measures, score as Critical, Detached, Guarded, Independent, and Resourceful
Commonly found in populations of male college scholarship athletes
More likely than other types to suffer cardiac problems
Lowest ranked of all types in using social coping resources
One of four types least satisfied with their marriage or intimate relationship
Among types least likely to complete college
Personal values include Autonomy; at work, value Stability, Security, Independence, and Achievement
Commonly found in skilled trades, technical fields, agriculture, law enforcement, and military occupations

ISTP Hobbies and Interests

Popular hobbies for an ISTP include magic and comedy, archery, weaponry, hunting, scuba diving, rappelling, aviation, skydiving, motorcycles, and other extreme sports. They are often drawn to risky or thrilling activities and those that allow them to work with something mechanical.""",
    "ISFP":"""The Composer

    ISFP in a Nutshell

ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life has to offer. ISFPs are quiet and unassuming, and may be hard to get to know. However, to those who know them well, the ISFP is warm and friendly, eager to share in life's many experiences.

ISFPs have a strong aesthetic sense and seek out beauty in their surroundings. They are attuned to sensory experience, and often have a natural talent for the arts. ISFPs especially excel at manipulating objects, and may wield creative tools like paintbrushes and sculptor's knives with great mastery.

ISFP Values and Motivations

ISFPs tend to be tolerant and nonjudgmental, but are deeply loyal to the people and causes that matter to them. They endeavor to accept and support other people, but are ultimately guided by their own core values. They will typically look for ways to be accommodating and may have difficulty dealing with others who are not willing to do the same.

ISFPs are typically modest and may underestimate themselves. They usually do not like to be in the spotlight, preferring instead to take a supporting role, and will avoid planning and organizing whenever possible. Sensitive and responsive, they step in to do what needs to be done and are satisfied by their personal sense of being helpful to others.

How Others See the ISFP

ISFPs can be difficult to recognize because of their tendency to express themselves through action rather than words. They may initially appear distant or aloof, but if you watch closely, you can observe their caring in the thoughtful things they do for others. They are carefully observant of the practical needs of other people, and often step in with quiet, unassuming assistance at just the moment it is needed. ISFPs prefer to take a supportive role and are rarely assertive or demanding of attention. They are typically tolerant and accepting of others. ISFPs typically have finely tuned artistic sensibilities. They are sensitive to color, texture, and tone, and often have an innate sense of what will be aesthetically pleasing. They are often naturals when it comes to arranging something artistically, and enjoy the process of taking in the sensations around them. ISFPs focus mostly on the experiences of the present moment, and are rarely ambitious, preferring instead to enjoy the simple pleasures of life: friends, family, and sensory delights such as food, music, and art.

How Rare Is the ISFP Personality Type?

ISFPs make up:

6.6% of the general population

7.5% of women

5.5% of men

Famous ISFPs

Famous ISFPs include:

Cher

Barbra Streisand

Frida Kahlo

Jacqueline Kennedy Onassis

David Beckham

Bob Dylan

Wolfgang Amadeus Mozart

Jimi Hendrix

Rihanna

Michael Jackson

Facts About ISFPs
Interesting facts about the ISFP:

On personality trait measures, score as Easygoing
Among types most likely to report heart disease and hypertension
In college, likely to report low levels of assertiveness
In essays, projected themselves the fewest number of years into the future of all the types
Among the types least likely to stay in college
Most likely of all types to report stress associated with finances and children
In a national sample, likely to value a work environment which provides security, clear and simple instructions, and no expectation of extra work hours
Underrepresented among MBA students and small business owners
Commonly found in occupations in health care, business, and law enforcement

ISFP Hobbies and Interests

Popular hobbies for ISFPs are those that use their physical or artistic skills, including independent athletics like skiing or swimming, dance, and craft projects. ISFPs also enjoy entertaining in intimate groups and exploring art and nature.""",
    "ENTJ":"""The Commander

    ENTJ in a Nutshell

ENTJs are strategic leaders, motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are usually articulate and quick-witted.

ENTJs are analytical and objective, and like bringing order to the world around them. When there are flaws in a system, the ENTJ sees them, and enjoys the process of discovering and implementing a better way. ENTJs are assertive and enjoy taking charge; they see their role as that of leader and manager, organizing people and processes to achieve their goals.

ENTJ Values and Motivations

ENTJs are often very motivated by success in their careers and enjoy hard work. They are ambitious and interested in gaining power and influence. To the ENTJ, decision-making is a vocation. They want to be in a position to make the call and put plans into motion.

ENTJs tend to be blunt and decisive. Driven to get things done, they can sometimes be critical or brusque in the pursuit of a goal. They are typically friendly and outgoing, although they may not pick up on emotional subleties in other people. They often love working with others toward a common goal, but may not find time to attend to their feelings. They are focused on results and want to be productive, competent, and influential.

How Others See the ENTJ

ENTJs are natural leaders, and often take charge no matter where they are. They typically have a clear vision for the future, and intuitively understand how to move people and processes towards that goal. They tend to approach every situation with the attitude of an efficiency analyst, and are not shy about pointing out what could be done better. For the ENTJ, their ideas are a foregone conclusion: it’s just a matter of time before they can move the players to get everything accomplished.

ENTJs are often gregarious, and seem to have an idea for how a person will fit into their grand scheme from the moment they are introduced. They are typically direct and may seem presumptuous or even arrogant; they size people and situations up very quickly, and have trouble being anything but honest about what they see. ENTJs are sensitive to issues of power, and seek positions and people of influence. They are characteristically ambitious, and often very engaged in their careers. More than any other type, ENTJs enjoy their work, and may even say that working is what they do for fun.

How Rare Is the ENTJ Personality Type?

ENTJ is one of the least common types in the population, and the rarest type among women. ENTJs make up:

1.8% of the general population

2.3% of men

1.5% of women

Famous ENTJs

Famous ENTJs include:

Margaret Thatcher

Kamala Harris

Sheryl Sandberg

Napoleon Bonaparte

Carl Sagan

General Norman Schwarzkopf

David Letterman

Douglas MacArthur

Harrison Ford

Mindy Kaling

Quentin Tarantino

Bill Gates

Facts About ENTJs
Interesting facts about the ENTJ:

On personality trait measures, score as Ambitious, Forceful, Optimistic, Egotistical, Adaptable, and Energetic
Least likely of all types to report stress resulting from work or finances
More likely than average to suffer cardiac problems
Among the least likely of all types to believe in a higher spiritual power
Among top 4 types in college GPA
Among most likely to stay in college
Personal values include Home/Family, Achievement, Creativity, and Learning
Overrepresented among MBA students and small business owners
One of two types most likely to be satisfied with their work

ENTJ Hobbies and Interests

Popular hobbies for ENTJs include taking leadership positions in community groups, attending social gatherings or sporting events, and playing competitive sports. Because ENTJs are so often focused on their careers, they may have few interests outside of work, or they may participate in leisure activities that also help to further their careers.""",
    "ENFJ":"""The Teacher

    ENFJ in a Nutshell

ENFJs are idealist organizers, driven to implement their vision of what is best for humanity. They often act as catalysts for human growth because of their ability to see potential in other people and their charisma in persuading others to their ideas. They are focused on values and vision, and are passionate about the possibilities for people.

ENFJs are typically energetic and driven, and often have a lot on their plates. They are tuned into the needs of others and acutely aware of human suffering; however, they also tend to be optimistic and forward-thinking, intuitively seeing opportunity for improvement. The ENFJ is ambitious, but their ambition is not self-serving: rather, they feel personally responsible for making the world a better place.

ENFJ Values and Motivations

ENFJs are driven by a deep sense of altruism and empathy for other people. They have an intuitive sense of the emotions of others, and often act as an emotional barometer for the people around them. However, their compassion not reserved for the people close to them: they are often humanitarian in nature, and may feel genuine concern for the ills of the entire human race. They tend to personally experience the feelings of others, and feel compelled to act when they see people suffering.

ENFJs want close, supportive connections with others, and believe that cooperation is the best way to get things done. They like to be liked and are very sensitive to feedback, both positive and negative. They expect the best not just from themselves, but from others as well, and may find themselves disappointed when others are not as genuine in their intentions as the ENFJ. ENFJs work hard to maintain strong relationships, and strive to be valuable members of their families, groups, and communities.

How Others See the ENFJ

ENFJs are natural teachers, often found organizing people to take part in some educational activity. They tend to take charge of a situation, and guide a group towards those activities and experiences which will help them learn and grow. They intuitively see the potential in people, and with charisma and warmth, they encourage others to pursue greater development of their strengths. They are typically dynamic and productive, and are often visibly energized when leading others to discover new knowledge. ENFJs are typically good communicators, talented at using words to connect with others. They are perceptive about people and enjoy talking about relationships. They often enjoy helping others solve personal problems and like to share their insights about people, their emotions, and their motivations. They are empathetic sometimes to the point of being overinvolved, and can become exhausted if they are surrounded by too much negative emotion.

How Rare Is the ENFJ Personality Type?

ENFJ is one of the less common types in the population, especially for men. ENFJs make up:

2.2% of the general population

2.8% of women

1.4% of men

Famous ENFJs

Famous ENFJs include: 

Oprah Winfrey

Pope John Paul II

Maya Angelou

Meghan Markle

Michael Jordan

Reese Witherspoon 

Margaret Mead

Ralph Nader

Abraham Maslow

Dr. Phil McGraw

Martin Luther King, Jr.

Facts About ENFJs
Interesting facts about the ENFJ:

On personality trait scales, scored as Active, Pleasant, Sociable, Demanding, Impatient, Appreciative, and Compromising
Most likely of all types to cope with stress by exercising
Most likely of all types to believe in a higher spiritual power
Ranked by psychologists as among least likely to have trouble in school
Personal values include Friendships, Education & Learning, Creativity, and Community Service
Among types highest in job satisfaction, but also among most likely to report plans to leave their jobs
Commonly found in careers in religion, teaching, and the arts

ENFJ Hobbies and Interests

Popular hobbies for the ENFJ include organizing social events, reading, the arts, museums, storytelling, listening to music, writing, and gourmet cooking.""",
    "ENTP":"""The Visionary

    ENTP in a Nutshell

ENTPs are inspired innovators, motivated to find new solutions to intellectually challenging problems. They are curious and clever, and seek to comprehend the people, systems, and principles that surround them. Open-minded and unconventional, Visionaries want to analyze, understand, and influence other people.

ENTPs enjoy playing with ideas and especially like to banter with others. They use their quick wit and command of language to keep the upper hand with other people, often cheerfully poking fun at their habits and eccentricities. While the ENTP enjoys challenging others, in the end they are usually happy to live and let live. They are rarely judgmental, but they may have little patience for people who can't keep up.

ENTP Values and Motivations

ENTPs are energized by challenge and are often inspired by a problem that others perceive as impossible to solve. They are confident in their ability to think creatively, and may assume that others are too tied to tradition to see a new way. The Visionary relies on their ingenuity to deal with the world around them, and rarely finds preparation necessary. They will often jump into a new situation and trust themselves to adapt as they go.

ENTPs are masters of re-inventing the wheel and often refuse to do a task the same way twice. They question norms and often ignore them altogether. Established procedures are uninspiring to the Visionary, who would much rather try a new method (or two) than go along with the standard.

How Others See the ENTP

ENTPs are typically friendly and often charming. They usually want to be seen as clever and may try to impress others with their quick wit and incisive humor. They are curious about the world around them, and want to know how things work. However, for the ENTP, the rules of the universe are made to be broken. They like to find the loopholes and figure out how they can work the system to their advantage. This is not to say the Visionary is malicious: they simply find rules limiting, and believe there is probably a better, faster, or more interesting way to do things that hasn’t been thought of before. The ENTP is characteristically entrepreneurial and may be quick to share a new business idea or invention. They are confident and creative, and typically excited to discuss their many ingenious ideas. The ENTP’s enthusiasm for innovation is infectious, and they are often good at getting other people on board with their schemes. However, they are fundamentally “big-picture” people, and may be at a loss when it comes to recalling or describing details. They are typically more excited about exploring a concept than they are about making it reality, and can seem unreliable if they don’t follow through with their many ideas.

How Rare Is the ENTP Personality Type?

ENTP is one of the rarer types in the population. ENTPs make up:

4.3% of the general population

5.1% of men

3.6% of women

Famous ENTPs

Famous ENTPs include:

Steve Jobs

Amy Poehler 

Sacha Barron Cohen

Walt Disney

Joan Rivers 

Barack Obama

Anna Kendrick 

Thomas Edison

Benjamin Franklin

Richard Feynman

Leonardo da Vinci

Niccolo Machiavelli

Kate McKinnon 

Jon Stewart

“Weird Al” Yankovic

Conan O’Brien

Facts About ENTPs
Interesting facts about the ENTP:

On personality trait scales, scored as Enterprising, Friendly, Resourceful, Headstrong, Self-Centered, and Independent
Least likely of all types to suffer heart disease and hypertension
Least likely of all types to report stress associated with family and health
Scored among highest of all types in available resources for coping with stress
Overrepresented among those with Type A behavior
Among highest of all types on measures of creativity
One of two types most frequent among violators of college alcohol policy
Among types most dissatisfied with their work, despite being among the types with highest income
Commonly found in careers in science, management, technology, and the arts

ENTP Hobbies and Interests

Popular hobbies for the ENTP include continuing education, writing, art appreciation, playing sports, computers and video games, travel, and cultural events.""",
    "ENFP":"""The Champion

    ENFP in a Nutshell

ENFPs are people-centered creators with a focus on possibilities and a contagious enthusiasm for new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other people explore their creative potential.

ENFPs are typically agile and expressive communicators, using their wit, humor, and mastery of language to create engaging stories. Imaginative and original, ENFPs often have a strong artistic side. They are drawn to art because of its ability to express inventive ideas and create a deeper understanding of human experience.

ENFP Values and Motivations

ENFPs tend to be curious about others and preoccupied with discovering the deeper meaning in people and ideas. They want authentic experience and often seek emotional intensity. ENFPs are easily bored by details and repetition and seek out situations that offer an escape from the mundane. Novelty is attractive to ENFPs, who often have a wide range of interests and friends from many backgrounds.

ENFPs prize individuality and often consider the pursuit of happiness to be the highest priority in life, both for themselves and for others. They place great importance on personal freedom and self-expression, and want to be able to go wherever inspiration leads.

How Others See the ENFP

ENFPs love to talk about people: not just the facts, but what motivates them, what inspires them, and what they envision achieving in life. They’ll often share their own aspirations freely, and want to hear others’ in return. The ENFP is unlikely to judge anyone’s dream, and will discuss the most imaginative and outlandish of fantasies with warm, enthusiastic intensity. They love to explore creative possibilities, and nothing deflates them faster than talking about dry facts or harsh reality.

ENFPs often seem unconventional, and may come off as scattered; they don’t tend to be in touch with their physical surroundings. They often overlook the details, as they are more likely to focus on connecting with other people or on exploring their own imagination and self-expression. They have little patience for the mundane and want to experience life with intensity and flair. ENFPs often have an artistic streak, and may be artistic in appearance. Many have developed a distinctive and quirky personal style.

How Rare Is the ENFP Personality Type?

ENFP is a moderately common personality type. ENFPs make up:

8.2% of the general population

10.2% of women

5.8% of men

Famous ENFPs

Famous ENFPs include:

Robin Williams

Drew Barrymore

Julie Andrews

Alicia Silverstone

Kristen Bell 

Jim Carrey

Kim Nam-joon (RM)

Bill Clinton

Phil Donahue

Mark Twain

Edith Wharton

Will Rogers

Carol Burnett

Dr. Seuss

Joan Baez 

Regis Philbin

Facts About ENFPs
Interesting facts about the ENFP:

On personality trait scales, scored as Enthusiastic, Outgoing, Spontaneous, Changeable, Impulsive, Energetic, and Understanding
Scored among highest of all types in available resources for coping with stress
ENFP women are less likely to suffer from heart disease
ENFP men are less likely to suffer from chronic pain
Rated by psychologists as among most likely of all types to have trouble in school
Overrepresented among academically talented elementary school students
Personal values include Home & family, Friendships, Creativity, Learning, and Community Service
Commonly found in careers in counseling, teaching, religion, and the arts

ENFP Hobbies and Interests

Popular hobbies for the ENFP include writing, creating and appreciating art, playing musical instruments, listening to music, participating in community theater, and reading fiction.""",
    "ESTJ":"""The Supervisor

    ESTJ in a Nutshell

ESTJs are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a systematic, methodical way.

ESTJs are the consummate organizers, and want to bring structure to their surroundings. They value predictability and prefer things to proceed in a logical order. When they see a lack of organization, the ESTJ often takes the initiative to establish processes and guidelines, so that everyone knows what's expected.

ESTJ Values and Motivations

ESTJs are conventional, factual, and grounded in reality. For the ESTJ, the proof is in the past: what has worked and what has been done before. They value evidence over conjecture, and trust their personal experience. ESTJs look for rules to follow and standards to meet, and often take a leadership role in helping other people meet expectations as well. They concern themselves with maintaining the social order and keeping others in line.

ESTJs often take on a project manager role at home as well as at work, and excel at setting goals, making decisions, and organizing resources to accomplish a task. The ESTJ wants to achieve efficient productivity and typically believes this is best accomplished when people and systems are well organized.

How Others See the ESTJ

ESTJs command a situation, with the sense that they know how things should go and are ready to take charge to make sure that it happens. They are task-oriented and put work before play. Confident and tough-minded, the ESTJ appears almost always to be in control. ESTJs appreciate structure and often begin to organize as soon as they enter a room. They want to establish the ground rules and make sure everyone does what they’re supposed to. ESTJs are often involved in institutions: clubs, associations, societies, and churches, where they usually take a leadership role. They typically connect with others through sharing ritual and routine. Social interaction for ESTJs often means following an established tradition to engage with others in a structured way. ESTJs tend to respect and seek out hierarchy. They want to know who’s in charge, and will assign levels of responsibility if none exist. Once a structure is in place, ESTJs typically trust authority figures and expect obedience from people of lower rank.

How Rare Is the ESTJ Personality Type?

ESTJs make up:

9% of the general population

11.3% of men

7% of women

Famous ESTJs

Famous ESTJs include:

Colin Powell

Judge Judy Sheindlin

Michelle Obama

Martha Stewart 

Alec Baldwin

Dr. Laura Schlessinger

George Washington

Sandra Day O’Connor

Mike Wallace

Vince Lombardi

Facts About ESTJs
Interesting facts about the ESTJ:

On personality trait measures, likely to score as Contented, Energetic, Prejudiced, Self-Satisfied, and Practical
More likely than other types to exhibit Type A behavior
Of all types, scored highest in coping resources (with ENFP)
Ranked 3rd highest in marital satisfaction among all types
Among top four types in college GPA
Least likely of all types to think about suicide in college
Among most likely to stay in college
Among types most satisfied with their work
High-ranking personal values include Health, Financial Security, Achievement, and Prestige
Overrepresented among bank officers, financial managers, and business owners

ESTJ Hobbies and Interests

Popular hobbies for the ESTJ include building and repairing things around the home, gardening, volunteering, community service, and playing and watching sports.""",
    "ESFJ":"""The Provider

    ESFJ in a Nutshell

ESFJs are conscientious helpers, sensitive to the needs of others and energetically dedicated to their responsibilities. They are highly attuned to their emotional environment and attentive to both the feelings of others and the perception others have of them. ESFJs like a sense of harmony and cooperation around them, and are eager to please and provide.

ESFJs value loyalty and tradition, and usually make their family and friends their top priority. They are generous with their time, effort, and emotions. They often take on the concerns of others as if they were their own, and will attempt to put their significant organizational talents to use to bring order to other people's lives.

ESFJ Values and Motivations

ESFJs act according to a strict moral code, and look for others to do the same. They often see things in terms of black and white, right and wrong, and they are typically not shy about sharing their evaluations of others' behavior. ESFJs seek harmony and cooperation, and feel this is best accomplished when everyone follows the same set of rules. They have a sense of order in the way people relate to one another, and often take on roles that allow them to help enforce that social order.

ESFJs feel a sense of personal responsibility for other people's needs, and are usually eager to get involved and help out. They tend to be serious and practical, dutifully putting business before pleasure—especially the business of caring for others. They typically enjoy routine and often keep a regular schedule that allows them to be organized and productive.

How Others See the ESFJ

ESFJs may often be found playing host or hostess. They tend to take on the role of organizer without hesitation, and want to be sure that everyone is taken care of. Roles such as committee leader, event planner, and church volunteer suit the ESFJ well. They are typically engaged with their communities and work hard to do their part in maintaining the social order. ESFJs are interested in other people and like to know the details of their lives. Gossip is a favorite pasttime of many ESFJs; they love to share stories about the people around them.

ESFJs have a clear moral code that guides their behavior and their expectations from others. They often have strong opinions about how people should behave and the proper thing to do. Manners and other codes of social interaction are often of great interest to ESFJs. They may think in terms of black and white, right and wrong. They can be judgmental of others who they do not think are acting appropriately, but they have the best of intentions: they simply want everyone to follow the rules so they can all get along. The ESFJ wants things to be all right with the people around them, and may become very involved with others’ problems and concerns.

For more information: The Art of SpeedReading People

How Rare Is the ESFJ Personality Type?

ESFJs make up:

5.7% of the general population

7.5% of women

3.5% of men

Famous ESFJs

Famous ESFJs include:

Jennifer Garner

Steve Harvey

Hugh Jackman 

Sam Walton

Barbara Walters

Ariana Grande

Joe Biden

William Howard Taft

Dave Thomas

JC Penney

Sally Field

Mary Tyler Moore

Jennifer Lopez

Ray Kroc

Facts About ESFJs
Interesting facts about the ESFJ:

Underrepresented among people suffering from substance abuse
Among types highest in resources for coping with stress
Second most likely of all types to report believing in a higher spiritual power
Highest of all types in reported satisfaction with their marriage or intimate relationship
Among most likely of all types to stay in college
Most likely of all types to be satisfied with their co-workers
Values at work include clear structure, security, and the ability to be of service to others
Among the types most satisfied with their work
Commonly found in careers in education, health care, and religion

ESFJ Hobbies and Interests

Popular leisure activities for ESFJs include volunteering in community, charity, or religious organizations; celebrating holidays and family traditions; cooking; entertaining; and social sports.""",
    "ESTP":"""The Dynamo

    ESTP in a Nutshell

ESTPs are energetic thrill-seekers who are at their best when putting out fires, whether literal or metaphorical. They bring a sense of dynamic energy to their interactions with others and the world around them. They assess situations quickly and move adeptly to respond to immediate problems with practical solutions.

Active and playful, ESTPs are often the life of the party and have a good sense of humor. They use their keen powers of observation to assess their audience and adapt quickly to keep interactions exciting. Although they typically appear very social, they are rarely sensitive; the ESTP prefers to keep things fast-paced and silly rather than emotional or serious.

ESTP Values and Motivations

ESTPs are often natural athletes; they easily navigate their physical environment and are typically highly coordinated. They like to use this physical aptitude in the pursuit of excitement and adventure, and they often enjoy putting their skills to the test in risky or even dangerous activities.

The ESTP's focus is action in the moment. They are engaged with their environments and solve practical problems quickly. ESTPs are excellent in emergencies, when they can apply their logical reasoning to situations where immediate action is necessary. Long-term goals are less interesting to the ESTP, who prefers to see tangible results in the moment.

How Others See the ESTP

The first thing you notice about the ESTP is likely to be their energy. They’re often chatting, joking, and flirting with friends and strangers alike. They enjoy engaging playfully with others and amusing everyone around them with their irreverent sense of humor. They tend to keep people on their toes, never quite knowing what the ESTP will poke fun at next. ESTPs are unabashedly gregarious with people, but their interest in individuals may not last long; they are more likely to work a room, having a laugh with everyone, than they are to engage in depth with any one person. ESTPs are comfortable in their physical environment and always looking for some action or activity. They tend to be the most naturally coordinated of all the types and are often found playing sports or engaging in various physical activities, especially ones with an element of danger. They are the stereotypical “adrenaline junkies” and may be found skydiving, motorcycle racing, or enjoying other extreme sports.

For more information: The Art of SpeedReading People

How Rare Is the ESTP Personality Type?

ESTPs make up:

6.1% of the general population

7.8% of men

4.7% of women

Famous ESTPs

Famous ESTPs include:

Mike Tyson

Angelina Jolie 

Donald Trump

George W. Bush

Winston Churchill

Kevin Spacey

Park Ji-min (Jimin)

Meryl Streep

Mae West

Eddie Murphy

Miley Cyrus

Bruce Willis

Madonna

John Wayne

Evel Knievel


Facts About ESTPs
Interesting facts about the ESTP:

On personality trait measures, score as Dominant, Flexible, Demanding, and Sociable
More frequent among patients suffering from chronic pain
One of four types reporting highest levels of assertiveness in college
One of two types with lowest college GPA
Among most likely of all types to stay in college
Values at work include autonomy, variety, independence, and structure
Overrepresented among MBA students
Commonly found in careers in marketing, skilled trades, business, and law enforcement

ESTP Hobbies and Interests

Popular hobbies for an ESTP include all sorts of sports and athletic pursuits, especially team sports and risky or adventurous activities like race car driving, boxing, or flying.""",
    "ESFP":"""The Performer

    ESFP in a Nutshell

ESFPs are vivacious entertainers who charm and engage those around them. They are spontaneous, energetic, and fun-loving, and take pleasure in the things around them: food, clothes, nature, animals, and especially people.

ESFPs are typically warm and talkative and have a contagious enthusiasm for life. They like to be in the middle of the action and the center of attention. They have a playful, open sense of humor, and like to draw out other people and help them have a good time.

ESFP Values and Motivations

ESFPs live in the moment, enjoying what life has to offer. They are especially tuned into their senses and take pleasure in the sights, sounds, smells, and textures around them. ESFPs like to keep busy, filling their lives with hobbies, sports, activities, and friends. Because they'd rather live spontaneously than plan ahead, they can become overextended when there are too many exciting things to do. An ESFP hates nothing more than missing out on the fun.

Although they are characteristically fun-loving, ESFPs are also typically practical and down-to-earth. They are grounded in reality and are usually keenly aware of the facts and details in their environment, especially as they pertain to people. They are observant of others and their needs, and responsive in offering assistance. ESFPs enjoy helping other people, especially in practical, tangible ways.

How Others See the ESFP

ESFPs are often the life of the party, entertaining and engaging others with humor and enthusiasm. They notice whether other people are having fun, and do their best to create a good time for all. Typically at home in their physical environment, ESFPs may take the lead in getting everyone involved in some active diversion. ESFPs are generally friendly and likable, but can be hard to get close to; although they tend to be very open, they are reluctant to be serious or to talk about anything negative. ESFPs are tuned into their senses, and often gravitate towards pleasing colors and textures in their environments. They often carefully choose fabrics and decorations with which to surround themselves. This attention also often translates into their appearance; ESFPs are often dressed in sensuous fabrics or bright, dazzling colors. They are often up on the latest trends, and like to excite the people around them with new environments and experiences.

For more information: The Art of SpeedReading People

How Rare Is the ESFP Personality Type?

According to the most recent global sample, ESFPs make up:

6% of the general population

6.7% of women

5.1% of men

Famous ESFPs

Famous ESFPs include:

Marilyn Monroe

Dolly Parton

Elizabeth Taylor

Judy Garland

Will Smith

Magic Johnson

Elvis Presley

Ronald Reagan

Serena Williams

Paul McCartney

Bob Hope

Goldie Hawn


Facts About ESFPs
Interesting facts about the ESFP:

On personality trait measures, score as Changeable, Energetic, Forceful, Initiating, and Resourceful
More likely to use emotional coping techniques over spiritual or physical resources
Tend to look to authority in education rather than expressing intellectual curiosity; prefer hands-on learning
Among most likely to stay in college
More likely than other types to watch television for more than 3 hours a day
Second highest of all types in marital satisfaction
Among types with lowest income
At work, tend to be satisfied with co-workers but dissatisfied with job security, stress, salary, and accomplishment
Personal values include Home/Family, Health, Friendships, Financial Security, and Spirituality
Overrepresented in health care, teaching, coaching, and child care occupations

ESFP Hobbies and Interests

Popular hobbies for ESFPs include socializing, team sports, home improvement projects, cooking, entertaining, games, and dance. ESFPs love big parties and gatherings and are quick to join any group or activity that sounds like fun."""
        }
# ___________________________________________________________________________
st.image(r"cropedLogo.png")
st.title("I Care",)
st.title("MBTI Personality Analysis Test")
st.info("Getting your personality type by answering 20 questions")
def get_info():
    l = [ [],[],[],[] ]
    ctr = 0
    for i in range(20):
        choice = st.radio( f"{i+1}\. {questions[i]}", ["Yes", "No"])
        if choice == "Yes":
            l[ctr].append(1)
        else:
            l[ctr].append(0)
        if i == 4 or i == 9 or i == 14 or i == 19:
            ctr += 1
    return l
# personality analysis
def scan(a):
    s = ""
    for i in range(4):
        if a[i].count(1) >= 3:
            s = s + c[i][0]
        else:
            s = s + c[i][1]
    return s

l = get_info()
submit = st.button("Submit")
if submit:
    p = scan(l)
    st.write(p)
    st.write(info[p])
