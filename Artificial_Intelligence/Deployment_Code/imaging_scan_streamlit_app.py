# Scan
from PIL import Image
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import img_to_array

scan_info = {"Avulsion fracture": """Overview
- What is an avulsion fracture?
Avulsion fractures happen when a bone fragment separates from the rest of the bone. In children, they are most common in sports like soccer, football, gymnastics, and other sports that involve sudden changes in direction, leaping, and kicking. Avulsion fractures are most common around the hip or pelvis but can also occur in the ankle, foot, finger, elbow, or knee.

Avulsion fractures occur most frequently in female athletes between the of ages 13 and 14 and in male athletes between the ages of 15 and 17.

Avulsion Fracture |Symptoms & Causes
- What causes avulsion fractures?
To understand avulsion fractures, it helps to understand the interactions between tendons, muscles, and bones. Tendons connect muscles to bones. When a soccer player kicks a ball, for instance, their muscles provide the power while their tendons transfer this power to their bones, moving the leg so that it sends the ball down the field.

Avulsion fractures happen when a set of muscles puts more pressure on the bone than the bone can withstand. As youth sports have become more competitive, many young athletes are developing extremely strong muscles. When a muscle is stronger than the bone it’s attached to, it becomes more likely that the force of the tendon can cause a small piece of bone to break away from the rest of the bone.

In addition to the rapid development of muscle strength during adolescence, the rapid rate of growth during childhood and adolescence can lead to tighter muscles and tendons in young athletes, which can result in increased tension on the location where the tendon attaches to the bone.

In growing athletes, avulsion fractures typically occur around soft areas of cartilage called apophyses — areas of the skeleton where the bone is rapidly developing and not yet fully ossified (hardened). Once a child reaches mature height, these areas become as strong as the rest of the bone, but until then, the apophyses are prone to injury.
             
- you can see more information here: https://www.childrenshospital.org/conditions/avulsion-fracture""",
             "Comminuted fracture": """Overview
- What is a comminuted fracture?
Comminuted (pronounced “kah-meh-noot-ed”) fractures are a type of broken bone. The term comminuted fracture refers to a bone that is broken in at least two places. These fractures can affect any large or long bone in your body. Some of the most common include:

Femur (thigh).
Tibia (shin).
Fibula (calf).
Humerus (upper arm).
Radius and ulna (forearm).
Clavicle (collarbone).
Skull.
Comminuted fractures are almost always caused by serious traumas like car accidents or falls from a high place. They are very serious in large bones, and you will often need surgery to repair your bones. Sometimes, comminuted fractures happen to smaller bones and can heal without surgery. How long it takes to recover depends on which of your bones are fractured and what caused the breaks. Most people need up to a year to recover from a comminuted fracture if it involved one of the long or larger bones in your body, especially if it requires surgery.

Symptoms and Causes
- What are the symptoms of a comminuted fracture?
If you have a comminuted fracture, you’ll also likely experience serious symptoms of the trauma that caused it. Your symptoms will depend on the other injuries you have. But, in general, the symptoms of a comminuted fracture can include:

Intense pain.
Not being able to move a part of your body you normally can.
A part of your body is noticeably different looking or out of its usual place.
Seeing your bone through your skin.
Swelling.
Bruising.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/22252-comminuted-fracture""",
             "Compression-Crush fracture": """Overview
- What is a compression fracture?
Compression fractures are small breaks or cracks in the vertebrae (the bones that make up your spinal column). The breaks happen in the vertebral body, which is the thick, rounded part on the front of each vertebra. Fractures in the bone cause the spine to weaken and collapse. Over time, these fractures affect posture. The spine curves forward and the person looks “hunched over” (kyphosis).

Compression fractures usually happen in the thoracic (middle) part of the spine, especially in the lower thoracic area. Providers also call them vertebral compression fractures (VCF). They often result from osteoporosis. But they can also happen after trauma (such as a car crash) or as a result of tumors on the spine.

Providers treat compression fractures with medications and a special type of back brace. Some people require a minimally invasive procedure to strengthen the vertebrae and stabilize their spine.

Symptoms and Causes
- What are the symptoms of compression fractures?
Compression fracture symptoms range from mild to severe. Some people may not have symptoms. Their provider may discover the fracture when they do an X-ray for another condition. But many people are unable to stand or walk without pain. Symptoms of a fractured spine include:

Back pain, which can come on suddenly and last a long time (chronic back pain). It usually develops anywhere between the shoulders and the lower back. Pain usually gets better when you lie down, and it worsens when you stand or walk.
Decreased mobility or flexibility in the spine. You may not be able to twist or bend over.
Hunched over appearance (some people call this curved upper back a “dowager’s hump” or hunchback).
Loss of height as the vertebrae compress and the back curves.
Pinched nerves and nerve damage, which can cause tingling and numbness in the back and difficulty walking.
Problems controlling the bladder or bowels (these symptoms happen with severe, untreated fractures).

- you can see more information here: https://my.clevelandclinic.org/health/diseases/21950-compression-fractures""",
             "Fracture Dislocation": """Overview
- Dislocations or Fractures
Two of the most common bone and joint injuries are dislocations and fractures.

A dislocation occurs when two bones slip out of place at the joint that connects them. It’s usually caused by a sudden impact from a blow, fall or other trauma. You can dislocate almost any joint in your body— your ankles, knees, shoulders, hips, elbows or jaw. You can even dislocate your finger and toe joints.

When more pressure is put on a bone than it can stand, the bone may split or break. A break of any size is referred to as a fracture. It can result from a fall, trauma, accident, direct blow or repetitive stress, as well as numerous medical conditions that weaken bones.

- Dislocation and Fracture Symptoms
It’s hard to identify a dislocated joint from a bone fracture. Symptoms of both include:
A visibly out-of-place or misshapen limb
Swelling, bruising or bleeding
Intense pain
Numbness and tingling
Broken skin with bone protrusion
Loss of motion

- you can see more information here: https://www.summahealth.org/orthopedic/our-services/sports-medicine/dislocations-or-fractures""",
             "Greenstick fracture": """Overview
- What are greenstick fractures?
A greenstick fracture is a type of bone fracture (broken bone). Greenstick fractures happen when something bends a bone enough to crack it without breaking it into multiple pieces.

Greenstick fractures get their name from the shape (pattern) of the break in your bone. Picture the difference between snapping a young, green twig and an older, dried out branch. Green twigs bend without snapping, but — at a certain point — they crack or splinter where you’re bending them. Older branches snap cleanly apart. Greenstick fractures are the same as bending that young twig — a break along one side of a bone that doesn’t snap it into more than one piece.

Almost all greenstick fractures happen to children younger than 10 because kids have softer and less brittle bones than adults.

Your child will probably need to wear a cast while their bone heals after a greenstick fracture. More severe fractures require surgery to repair — especially if they have other injuries.

Types of greenstick fractures
Greenstick fractures usually affect longer bones, including your:

Humerus (upper arm bone).
Radius and ulna (forearm bones).
Phalanges (finger and toe bones).
Femur (thigh bone).
Fibula (calf bone).

Symptoms and Causes
- What are greenstick fracture symptoms?
The most common greenstick fracture symptoms include:

Pain.
Bruising or discoloration.
Tenderness.
Swelling.
Part of your child’s body looking more bent or twisted than usual.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/17812-greenstick-fractures""",
             "Hairline Fracture": """Overview
- What is Hairline Fracture?
Hairline or stress fractures are tiny cracks on a bone that often develop in the foot or lower leg. The most significant risk for a hairline fracture is playing high impact sports that involve repetitive jumping or running.

Hairline fractures may also occur in the upper limb and are often related to falls or accidents.

Hairline fractures usually develop gradually as a result of overuse, as opposed to larger bone fractures or breaks that are mostly caused by acute traumas, such as a fall. While hairline fractures may heal with sufficient rest, they can be painful and last several weeks.

Anyone who engages in regular physical activity can develop a hairline fracture, especially if the activity involves repetitive movements that put a strain on a bone or a group of bones. The most common treatment approach is rest.

- Symptoms
Symptoms are different from those of a more severe fracture or break when a person often feels a sharp pain immediately.

The pain from a hairline fracture will intensify when the person engages in activities that put a strain on the injured bone. This can inhibit a person’s mobility, which means they will be restricted as to how much weight they can put on the affected area.

Other symptoms may include:

swelling
bruising
tenderness

- you can more information here: https://www.medicalnewstoday.com/articles/319822#symptoms""",
             "Impacted fracture": """Overview
What is an Impaction Fracture?
An impaction fracture, also called a torus or buckle fracture, is one of the more “subtle” types of fractures that can affect children. Impaction fractures happen when a bone is compressed. This puts pressure on the area, therefore causing parts of the bone to crumble under the weight of the compression. Children are prone to this type of injury because their bones are still developing, which means their bones are softer and more malleable than adult bones.

Signs and Symptoms
Impaction fractures are incomplete breaks, which means that they do not cause a deformed appearance. Therefore, they usually don’t look like broken bones at all. Pain, pressure, swelling, and bruising are all common symptoms of this injury. If your child complains of these problems, especially after hurting themselves, then get the area examined by a professional.

Treatment and Recovery
Any type of broken bone can be scary for children- and also for their parents. Luckily though, impaction fractures are common injuries and your child should make a full recovery. However, getting the right treatment is important for both comfort and healing. Usually, these breaks are treated with a simple splint, though a cast might also be used. Properly setting the bone and resting the area will help your child heal.

you can see more information here: https://www.emergencyhospitals.care/whats-an-impaction-fracture-learn-about-this-common-childhood-injury-2/""",
             "Intra-articular fracture": """Overview
An intraarticular fracture is a fracture that crosses a joint surface. Such fractures also involve some cartilage damage. Fractures to joints are more complicated to treat and heal than simple fractures, as multiple bones are involved. Bone fragments inside the damaged joint may impede healing time and efficacy. Often, ligaments are torn or separated from the joint surfaces as well, also impeding the healing process.

Common areas of intraarticular fracture include the:
Shoulder - may involve the humerus, scapula and acromion and coracoid processes, as well as the glenoid and articular cartilage
Hip - - may involve some portion of the pelvis and the upper neck or head of the femur, as well as the hip's articular cartilage
Elbow - may involve the lower end of the humerus, the upper end of the radius and the ulnar collateral ligament as well as cartilage between the bones
Wrist - may involve the lower ends of the radius and the ulna, and the carpal bones, as well as cartilage found between each of the small bones of the carpals
Knee - may involve the lower end of the femur, the patella or knee cap, and the upper ends of the tibia and/or fibula as well as articular cartilage and collateral ligaments
Ankle - may involve the lower end of the tibia or fibula, the subtalar joint and the articular cartilage and the anterior tibiofibular and lateral collateral ligaments

Causes
Blunt force trauma
Automobile accidents

Symptoms
Pain
Limited use or range of motion
Weakness
Swelling
Bruising

Treatment
Immobilization is the first step toward stabilizing the joint. Following imaging, the doctor will attempt to realign bones in their proper place. If torn ligaments are observed, or bones have been shattered or pieces badly damaged, surgery will be required for proper reconstruction of the affected joint.

- you can see more information here: https://www.faoconline.com/home/conditions/shoulder/intraarticular-fractures
""",
             "Longitudinal fracture": """Overview
What is Longitudinal fracture?
Longitudinal fractures are fractures that occur along (or nearly along) the axis of the bone. This is most often used in the context of a long-bone fracture although traditional classification of temporal bone fractures also used this term.

Signs and Symptoms
- pain

- swelling

- bruising

- discolored skin around the affected area

- protrusion of the affected area at an unusual angle

- inability to put weight on the injured area

- inability to move the affected area

- a grating sensation in the affected bone or joint

- bleeding if it is an open fracture

Treatment
Bone healing is a natural process that, in most cases, will occur naturally. Therefore, treatment typically focuses on providing the injured bone with the best circumstances for healing, and ensuring optimal future function.
For the natural healing process to begin, a doctor will reduce the fracture. This involves lining up the ends of the broken bones. In smaller fractures, a doctor can do this by manipulating the affected area externally. However, in some instances, this may require surgery.
Once a medical professional has aligned the fracture, they will ensure it stays in place. Methods of doing so includes:
casts or braces
metal plates and screws
intramedullary nails, or rods, placed in bone cavities
external fixings

you can see more information here: https://quizlet.com/ca/624720814/longitudinal-fracture-flash-cards/""",
             "Oblique fracture": """Overview
What is an oblique fracture?
Oblique fractures are a type of broken bone. They happen when one of your bones is broken at an angle. You might see oblique fractures referred to as complete fractures. This means the line of the break goes all the way through your bone.

Oblique fractures usually affect long bones in your body. Some of the most common include:

Femur (thigh).
Tibia (shin).
Fibula (calf).
Humerus (upper arm).
Radius and ulna (forearm).
Clavicle (collarbone).
Oblique fractures are almost always caused by falls or other traumas. You might need surgery to repair your bone. Some people only need a splint or cast for the bone to heal. How long it takes to recover fully depends on which of your bones are fractured — and what caused the breaks. Most people need a few months to recover from an oblique fracture.

Symptoms and Causes
What are the symptoms of an oblique fracture?
Symptoms of an oblique fracture include:

Pain.
Swelling.
Tenderness.
Inability to move a part of your body that you usually can.
Bruising or discoloration.
A deformity or bump that’s not usually on your body.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/22185-oblique-fracture""",
             "Pathological fracture": """Overview
Pathologic = having to do with a pathology (a disease)
Fracture = a break in a bone

A pathologic fracture is a break in a bone that is caused by an underlying disease. At the Spine Hospital at the Neurological Institute of New York, we specialize in pathologic fractures of vertebrae, or bones of the spine.

For the most part, bones need a reason to break–for example, a significant trauma. However, some pathologies (diseases) weaken the bones of the spine. Forces as slight as the weight of the body or a minor trauma that would otherwise be tolerated can cause a fracture in the diseased bone.

Symptoms
Pathologic vertebral fractures may or may not cause symptoms. If pathologic fractures cause symptoms, these may include:

pain in back, legs, and arms
neurological impairment–such as numbness and/or weakness in the arms or legs (if the fracture has affected the spinal cord and/or nerves in the spine)

you can see more information here: https://www.neurosurgery.columbia.edu/patient-care/conditions/pathologic-fracture""",
             "Spiral Fracture": """Overview
What is a spiral fracture?
Spiral fractures are a type of broken bone. They happen when one of your bones is broken with a twisting motion. They create a fracture line that wraps around your bone and looks like a corkscrew. You might see spiral fractures referred to as complete fractures. This means the line of the break goes all the way through your bone.

Spiral fractures usually affect long bones in your body. Some of the most common include:

Femur (thigh).
Tibia (shin).
Fibula (calf).
Talus (ankle).
Humerus (upper arm).
Radius and ulna (forearm).
Phalanges and metacarpals (fingers and hand).
Spiral fractures are almost always caused by falls or other traumas. You might need surgery to repair your bone. How long it takes to recover fully depends on which of your bones are fractured — and what caused the breaks. Most people need a few months to recover from a spiral fracture.

Symptoms and Causes
What are the symptoms of a spiral fracture?
Symptoms of a spiral fracture include:

Pain.
Swelling.
Tenderness.
Inability to move a part of your body that you usually can.
Bruising or discoloration.
A deformity or bump that’s not usually on your body.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/22241-spiral-fracture""",
             "glioma_tumor": """Overview
What is a glioma?
Glioma is a common type of tumor originating in the brain. About 33 percent of all brain tumors are gliomas, which originate in the glial cells that surround and support neurons in the brain, including astrocytes, oligodendrocytes and ependymal cells.

Gliomas are called intra-axial brain tumors because they grow within the substance of the brain and often mix with normal brain tissue.

What are the symptoms of glioma?
Gliomas cause symptoms by pressing on the brain or spinal cord. The most common, including glioblastoma symptoms are:

Headaches

Seizures

Personality changes

Weakness in the arms, face or legs

Numbness

Problems with speech

Other symptoms include:

Nausea and vomiting

Vision loss

Dizziness

Glioblastoma symptoms and other symptoms of glioma appear slowly and may be subtle at first. Some gliomas do not cause any symptoms and might be diagnosed when you see the doctor about something else.

- you can see more information here: https://www.hopkinsmedicine.org/health/conditions-and-diseases/gliomas""",
             "meningioma_tumor": """Overview
What Is Meningioma?
A meningioma is a tumor that arises from the meninges — the membranes that surround your brain and spinal cord. Although not technically a brain tumor, it is included in this category because it may compress or squeeze the adjacent brain, nerves and vessels. Meningioma is the most common type of tumor that forms in the head.

Most meningiomas grow very slowly, often over many years without causing symptoms. But in some instances, their effects on adjacent brain tissue, nerves or vessels may cause serious disability.

Meningiomas occur most commonly in women, and are often discovered at older ages, but a meningioma may occur at any age.

Symptoms of Meningioma
Signs and symptoms of a meningioma typically begin gradually and may be very subtle at first. Depending on where in the brain or, rarely, spine the tumor is situated, signs and symptoms may include:

Changes in vision, such as seeing double or blurriness
Headaches that worsen with time
Hearing loss or ringing in the ears
Memory loss
Loss of smell
Seizures
Weakness in your arms or legs
Causes of Meningioma
It isn't clear what causes a meningioma. Doctors know that something alters some cells in your meninges to make them multiply out of control, leading to a meningioma tumor.

you can see more information here: https://www.pennmedicine.org/for-patients-and-visitors/patient-information/conditions-treated-a-to-z/meningioma""",
             "pituitary_tumor": """Overview
Pituitary tumors are unusual growths that develop in the pituitary gland. This gland is an organ about the size of a pea. It's located behind the nose at the base of the brain. Some of these tumors cause the pituitary gland to make too much of certain hormones that control important body functions. Others can cause the pituitary gland to make too little of those hormones.

Most pituitary tumors are benign. That means they are not cancer. Another name for these noncancerous tumors is pituitary adenomas. Most adenomas stay in the pituitary gland or in the tissue around it, and they grow slowly. They typically don't spread to other parts of the body.

Pituitary tumors can be treated in several ways. The tumor may be removed with surgery. Or its growth may be controlled with medications or radiation therapy. Sometimes, hormone levels are managed with medicine. Your health care provider may suggest a combination of these treatments. In some cases, observation — also called a ''wait-and-see'' approach — may be the right choice.

Symptoms
Not all pituitary tumors cause symptoms. Sometimes these tumors are found during an imaging test, such as an MRI or a CT scan, that is done for another reason. If they don't cause symptoms, pituitary tumors usually don't need treatment.

Pituitary tumor symptoms may be caused by a tumor putting pressure on the brain or on other parts of the body nearby. Symptoms also can be caused by a hormone imbalance. Hormone levels can rise when a pituitary tumor makes too much of one or more hormones. Or a large tumor that disrupts the way the pituitary gland works may cause hormone levels to fall.

Symptoms from tumor pressure
Macroadenomas can put pressure on the pituitary gland, on nerves, on the brain and on other parts of the body nearby. That can cause symptoms such as:

Headache.
Eye problems due to pressure on the optic nerve, especially loss of side vision, also called peripheral vision, and double vision.
Pain in the face, sometimes including sinus pain or ear pain.
Drooping eyelid.
Seizures.
Nausea and vomiting.

- you can see more infromation here: https://www.mayoclinic.org/diseases-conditions/pituitary-tumors/symptoms-causes/syc-20350548""",
             "Cyst": """Overview
A cyst is an abnormal pocket of fluid, like a blister, that can form in many different areas of the body including the skin, genitals and internal organs. A cyst can vary in size from a tiny sac right up to a heavy bag containing litres of fluid. The common symptom is swelling around the area, but a cyst may or may not be painful. Sometimes, depending on the cause and location, a cyst contains semi-solid or solid material.

The typical treatment for any cyst is removal by surgery and a routine test for cancer, even though most cysts are benign. All unusual lumps need to be investigated by a qualified health professional.

Causes of cysts
Most cysts form for no apparent reason. Some of the known causes of cysts include:
Blocked ducts, which cause a build-up of fluid
A defect in the cells
An impact injury that pops a blood vessel
A parasite.
Different cysts and treatment
Some of the different types of cysts include:
Arachnoid cyst – the arachnoid membrane covers the brain. A baby may be born with an arachnoid cyst. It is caused by the arachnoid membrane doubling up or splitting to form an abnormal pocket of cerebrospinal fluid. This can be treated by surgical drainage if necessary.
Bartholin’s cyst – the Bartholin glands are situated inside the vagina. A cyst occurs if the ducts become blocked. Treatment includes surgery and antibiotics.
Breast cyst – these cysts are usually painful and need to be drained with a needle. There is some evidence that breast cysts might indicate an increased risk of breast cancer.
Cystic hygroma – occasionally, a baby is born with a small cyst or bursa. This birth defect can be corrected with surgery.
Hydatid disease – a small tapeworm forms cysts in the liver or lungs. The tapeworm eggs are spread by contact with infected dogs, their faeces (poo) or anything contaminated with faeces such as soil. Treatment includes surgery and drugs.
Ovarian cyst – most are benign, but can grow to such a size that the woman looks pregnant. Cysts less than 5cm are a common part of normal egg formation in the reproductive years. Sometimes, bleeding occurs into these cysts (this is called a haemorrhagic cyst). In some cases, the cysts are cancerous. Treatment includes surgery.
Pilonidal disease – a cyst forms in the skin of the lower back, sometimes containing an ingrown hair. Pilonidal cysts can grow in clusters and sometimes create a hole or cavity in the skin. Treatment includes draining the cyst or surgical removal.
Sebaceous cyst – the skin is lubricated by sebaceous fluid. This fluid can build up inside a pore or hair follicle and form a hard lump filled with thick, greasy matter. When squeezed, a small dome-shaped projection will appear (the punctum), representing the opening of the cyst. This may allow material to be expressed (squeezed out). Treatment includes drugs, draining the cyst with a small needle, or removal by surgery. Sebaceous cysts are common on the face, back, scalp and scrotum.

- you can see more information here: https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/cysts""",
             "Stone": """Overview
Stone disease occurs when chemicals in your urine become concentrated and form crystals in your urinary tract. It most often affects your kidneys, though it can also affect your bladder, the tubes that carry urine from your kidneys to your bladder (ureters), or the tube that connects your bladder to the outside of your body (urethra).

When these crystals – or stones – get stuck in any part of your urinary tract, they can cause severe pain, blockage and infection. Men are more likely to develop them than women, though lots of other factors can increase your risk, including dehydration, obesity and a family history of stone disease.

Symptoms
If you have stone disease, your symptoms will likely include:

Blood in your urine (also known as hematuria)
Feeling the need to urinate frequently
Inability to urinate
Nausea and/or vomiting
Sharp pain on one side of your back or in your lower abdomen

- you can see more information here: https://www.aurorahealthcare.org/services/urology/stone-disease""",
             "Tumor": """Overview
What is a tumor?
A tumor is a mass or group of abnormal cells that form in the body. If you have a tumor, it isn’t necessarily cancer. Many tumors are benign (not cancerous).

Tumors can form throughout the body. They can affect bone, skin, tissues, glands and organs. Neoplasm is another word for tumor.

What’s the difference between a tumor and a cyst?
A tumor is a solid mass of tissue. It may or may not be cancerous.

A cyst is a small sac that may contain fluid, air or solid material. The majority of cysts are not cancerous.

Symptoms and Causes
What causes a tumor?
Your body is constantly making new cells to replace old or damaged ones that die off. Sometimes, the cells don’t die off as expected. Or, new cells grow and multiply faster than they should. The cells start to pile up, forming a tumor.

What are the risk factors for tumors?
Tumors affect people of all ages, including children. Factors that increase the chances of developing a tumor include:

Gene mutations (changes), such as mutated BRCA (breast cancer) genes.
Inherited conditions, such as Lynch syndrome and neurofibromatosis (NFS).
Family history of certain types of cancer like breast cancer or prostate cancer.
Smoking, including exposure to secondhand smoke.
Exposure to toxins like benzene or asbestos.
Previous radiation exposure.
Viruses like HPV.
Having obesity.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/21881-tumor""",
             "CNV: Choroidal Neovascularization": """Overview
Some patients with dry age-related macular degeneration (AMD) eventually develop “wet AMD,” in which abnormal blood vessels grow into the retina and leak fluid, making the retina “wet.” Technically, this is called CNV or choroidal (core-oyd-al) neovascularization (nee-oh-vas-kyoo-lar-eye-zay-shun).
What Does Choroidal Neovascularization Mean?
“Neovascularization” means “new blood vessels.” These new, abnormal blood vessels originate in the choroid, a vessel-containing layer under the retina. When the retinas of people with AMD produce too much vascular endothelial growth factor (VEGF), new blood vessels sprout from the choroid, then grow into the retina. The new vessels, unlike normal ones, are leaky, and they allow fluid from the blood, and sometimes even red blood cells, to enter the retina. This fluid can immediately distort the vision because it forms a “blister” in the retina, which is normally flat. Over the course of days to months, this fluid can damage the retina, killing the light-sensing cells, called photoreceptors.

Symptoms of Choroidal Neovascularization
The symptoms of CNV include a distortion or waviness of central vision or a gray/black/void spot in the central vision. This should prompt a call to an ophthalmologist right away to get a priority emergency visit. The ophthalmologist can halt the growth and leakage of the blood vessels by injecting a drug blocking a protein called VEGF into the eye, but only if they can deliver the drug as soon as possible, within hours or days or so from the time you notice the change in vision. Time lost is vision lost!

- you can see more information here: https://www.brightfocus.org/macular/article/what-choroidal-neovascularization""",
             "DME: Diabetic Macular Edema": """Overview
What is Diabetic Macular Edema (DME)?
Diabetes is the leading cause of new blindness in the United States, with DME contributing greatly to this vision loss. DME may affect up to 10% of people with diabetes. DME is a complication of diabetes caused by fluid accumulation in the macula that can affect the fovea. The macula is the central portion in the retina which is in the back of the eye and where vision is the sharpest.Vision loss from DME can progress over a period of months and make it impossible to focus clearly.

What Causes DME?
DME is an eye condition which can occur in people living with diabetes – both type 1 and type 2. Consistently high blood sugar due to poor glucose control over time can damage small blood vessels in the body, including the eye. Diabetic retinopathy is a disease that damages the blood vessels in the retina, resulting in vision impairment. Left untreated, fluid can leak into the center of the macula, called the fovea, the part of the eye where sharp, straight-ahead vision occurs. The fluid makes the macula swell, blurring vision. This condition is called DME. It can occur at any stage of diabetic retinopathy, although it is more likely to occur as the disease progresses.

Diabetes Resources at Prevent Blindness
These resources are designed to support individuals living with diabetes and help them gain access to eye care that they require to maintain healthy vision.

Diabetes and Your Eyes
Diabetic Macular Edema (DME)
Diabetic Retinopathy
Diabetes and the Eyes Educational Toolkit
Diabetes Infographics
Diabetes and Your Eyes Videos
Health Insurance and Your Eyes
Healthy Living, Healthy Vision
Juvenile Diabetes and Vision Health
Medicare Benefits and Your Eyes
Vision Care Financial Assistance Information
ASPECT Patient Engagement Program
What Are the Symptoms of DME?
People who have diabetes are at risk of developing DME over time. A person with diabetes should have their vision checked yearly, or as directed by their eye doctor.  Vision changes due to DME are:

Blurred vision
Double vision
Sudden increase in eye floaters

- can see more information here: https://preventblindness.org/diabetic-macular-edema-dme/""",
             "Drusen": """Overview
Drusen are yellow deposits under the retina. Drusen are made up of lipids and proteins. Drusen can be different sizes—small, medium, and large. Small drusen are common in those 50 and older without age-related macular degeneration (AMD). But having many small drusen and larger drusen are often signs of AMD.

There are other drusen found in the optic nerve, which usually do not affect vision.

What Causes Drusen?
Drusen occur naturally with age. The exact relationship between degenerative macular disease and drusen is not clear. However, having large drusen is a sign of AMD.

Drusen of the Optic Nerve
Drusen can also occur in the optic nerve. These drusen are made up of protein and calcium salts and generally appear in both eyes. Unlike the drusen associated with AMD, optic nerve drusen (also known as optic disc drusen) are not related to aging, may be inherited, and typically appear in children. Optic nerve drusen usually do not affect vision, but some patients with these drusen may lose peripheral (side) vision.

Drusen Symptoms
Most people with drusen do not have any symptoms. Often, a routine eye exam will incidentally reveal their presence. A few small drusen are not a symptom of eye disease. However, the presence of a large number of larger drusen is an early sign of dry age-related macular degeneration (AMD). The symptoms of AMD include hazy vision, difficulty seeing when going from bright light to low light, and a blank or blurry spot in your central vision.

Optic nerve drusen also often do not produce symptoms. However, some patients with optic nerve drusen experience vision problems, including loss of peripheral (side) vision and temporary flickering or graying out of their vision.

- you can see more information here: https://www.aao.org/eye-health/diseases/what-are-drusen""",
             "Covid": """Overview
Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.

Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age. 

The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance.

The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell.

COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.

Most common symptoms:

fever
cough
tiredness
loss of taste or smell.
Less common symptoms:

sore throat
headache
aches and pains
diarrhoea
a rash on skin, or discolouration of fingers or toes
red or irritated eyes.

Serious symptoms:

difficulty breathing or shortness of breath
loss of speech or mobility, or confusion
chest pain.
Seek immediate medical attention if you have serious symptoms.  Always call before visiting your doctor or health facility. 

People with mild symptoms who are otherwise healthy should manage their symptoms at home. 

On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days. 

- you can see more information here: https://www.who.int/health-topics/coronavirus#tab=tab_3""",
             "Pneumonia": """Overview
What is pneumonia?
Pneumonia is an infection in your lungs caused by bacteria, viruses or fungi. Pneumonia causes your lung tissue to swell (inflammation) and can cause fluid or pus in your lungs. Bacterial pneumonia is usually more severe than viral pneumonia, which often resolves on its own.

Pneumonia can affect one or both lungs. Pneumonia in both of your lungs is called bilateral or double pneumonia.

Symptoms and Causes
What are the signs and symptoms of pneumonia?
Symptoms of pneumonia depend on the cause. Symptoms can range from mild to severe. Babies, young children and older adults may have different symptoms.

Symptoms of bacterial pneumonia
Symptoms of bacterial pneumonia can develop gradually or suddenly. Symptoms include:

High fever (up to 105 F or 40.55 C).
Cough with yellow, green or bloody mucus.
Tiredness (fatigue).
Rapid breathing.
Shortness of breath.
Rapid heart rate.
Sweating or chills.
Chest pain and/or abdominal pain, especially with coughing or deep breathing.
Loss of appetite.
Bluish skin, lips or nails (cyanosis).
Confusion or altered mental state.
Symptoms of viral pneumonia
Symptoms of viral pneumonia usually develop over several days. You might have symptoms similar to bacterial pneumonia or you might additionally have:

Dry cough.
Headache.
Muscle pain.
Extreme tiredness or weakness.

- you can see more information here: https://my.clevelandclinic.org/health/diseases/4471-pneumonia""",
             "breast_cancer": """Overview
Breast cancer is a disease in which abnormal breast cells grow out of control and form tumours. If left unchecked, the tumours can spread throughout the body and become fatal.

Breast cancer cells begin inside the milk ducts and/or the milk-producing lobules of the breast. The earliest form (in situ) is not life-threatening and can be detected in early stages. Cancer cells can spread into nearby breast tissue (invasion). This creates tumours that cause lumps or thickening. 

Invasive cancers can spread to nearby lymph nodes or other organs (metastasize). Metastasis can be life-threatening and fatal.

Treatment is based on the person, the type of cancer and its spread. Treatment combines surgery, radiation therapy and medications.

Signs and symptoms
Most people will not experience any symptoms when the cancer is still early hence the importance of early detection.

Breast cancer can have combinations of symptoms, especially when it is more advanced. Symptoms of breast cancer can include:

a breast lump or thickening, often without pain 
change in size, shape or appearance of the breast
dimpling, redness, pitting or other changes in the skin
change in nipple appearance or the skin surrounding the nipple (areola) 
abnormal or bloody fluid from the nipple.
People with an abnormal breast lump should seek medical care, even if the lump does not hurt. 

Most breast lumps are not cancer. Breast lumps that are cancerous are more likely to be successfully treated when they are small and have not spread to nearby lymph nodes. 

Breast cancers may spread to other areas of the body and trigger other symptoms. Often, the most common first detectable site of spread is to the lymph nodes under the arm although it is possible to have cancer-bearing lymph nodes that cannot be felt. 

Over time, cancerous cells may spread to other organs including the lungs, liver, brain and bones. Once they reach these sites, new cancer-related symptoms such as bone pain or headaches may appear. 

- you can see more information here: https://www.who.int/news-room/fact-sheets/detail/breast-cancer"""
            }

#  Classes
body_parts = {0:'Chest x-ray',
              1:'Feet x-ray',
              2:'Hand x-ray',
              3:'Nick x-ray',
              4:'Other:unsuported x-ray type!',
              5:'Skull x-ray'}
# _____________________________________________
fracture_type = {0 : 'Avulsion fracture',
                 1 : 'Comminuted fracture',
                 2 : 'Compression-Crush fracture',
                 3 : 'Fracture Dislocation',
                 4 : 'Greenstick fracture',
                 5 : 'Hairline Fracture',
                 6 : 'Impacted fracture',
                 7 : 'Intra-articular fracture',
                 8 : 'Longitudinal fracture',
                 9 : 'Oblique fracture',
                 10 : 'Pathological fracture',
                 11 : 'Spiral Fracture'}
# ______________________________________________
tumor_type = {0 : 'glioma_tumor',
              1 : 'meningioma_tumor',
              2 : 'normal no_tumor',
              3 : 'pituitary_tumor'}
# ______________________________________________
ct = {0 : 'Cyst',
      1 : 'Normal',
      2 : 'Stone',
      3 : 'Tumor'}
# ______________________________________________
oct = {0 : 'CNV: Choroidal Neovascularization',
       1 : 'DME: Diabetic Macular Edema',
       2 : 'Drusen',
       3 : 'Normal'}
# ______________________________________________
s = """Apple Pie: ~2.5 calories per gram
Baby Back Ribs: ~3.5 calories per gram
Baklava: ~5 calories per gram
Beef Carpaccio: ~2 calories per gram
Beef Tartare: ~2.5 calories per gram
Beet Salad: ~0.5 calories per gram
Beignets: ~3.5 calories per gram
Bibimbap: ~1.5 calories per gram
Bread Pudding: ~2.5 calories per gram
Breakfast Burrito: ~2 calories per gram
Bruschetta: ~1 calorie per gram
Caesar Salad: ~0.5 calories per gram
Cannoli: ~3.5 calories per gram
Caprese Salad: ~1 calorie per gram
Carrot Cake: ~3.5 calories per gram
Ceviche: ~0.5 calories per gram
Cheese Plate: ~3.5 calories per gram
Cheesecake: ~3.5 calories per gram
Chicken Curry: ~1.5 calories per gram
Chicken Quesadilla: ~2.5 calories per gram
Chicken Wings: ~3 calories per gram
Chocolate Cake: ~4 calories per gram
Chocolate Mousse: ~3 calories per gram
Churros: ~4 calories per gram
Clam Chowder: ~1.5 calories per gram
Club Sandwich: ~2.5 calories per gram
Crab Cakes: ~2 calories per gram
Creme Brulee: ~3.5 calories per gram
Croque Madame: ~3 calories per gram
Cupcakes: ~3.5 calories per gram
Deviled Eggs: ~1 calorie per gram
Donuts: ~4 calories per gram
Dumplings: ~2.5 calories per gram
Edamame: ~1 calorie per gram
Eggs Benedict: ~2.5 calories per gram
Escargots: ~1 calorie per gram
Falafel: ~2 calories per gram
Filet Mignon: ~2.5 calories per gram
Fish and Chips: ~2.5 calories per gram
Foie Gras: ~4.5 calories per gram
French Fries: ~3.5 calories per gram
French Onion Soup: ~1 calorie per gram
French Toast: ~2 calories per gram
Fried Calamari: ~2.5 calories per gram
Fried Rice: ~1.5 calories per gram
Frozen Yogurt: ~1 calorie per gram
Garlic Bread: ~4 calories per gram
Gnocchi: ~1.5 calories per gram
Greek Salad: ~0.5 calories per gram
Grilled Cheese Sandwich: ~3 calories per gram
Grilled Salmon: ~2 calories per gram
Guacamole: ~2 calories per gram
Gyoza: ~2 calories per gram
Hamburger: ~3.5 calories per gram
Hot and Sour Soup: ~0.5 calories per gram
Hot Dog: ~3.5 calories per gram
Huevos Rancheros: ~2 calories per gram
Hummus: ~1.5 calories per gram
Ice Cream: ~2 calories per gram
Lasagna: ~1.5 calories per gram
Lobster Bisque: ~1 calorie per gram
Lobster Roll Sandwich: ~2.5 calories per gram
Macaroni and Cheese: ~3 calories per gram
Macarons: ~4 calories per gram
Miso Soup: ~0.5 calories per gram
Mussels: ~0.5 calories per gram
Nachos: ~2.5 calories per gram
Omelette: ~1.5 calories per gram
Onion Rings: ~2.5 calories per gram
Oysters: ~0.5 calories per gram
Pad Thai: ~2 calories per gram
Paella: ~1.5 calories per gram
Pancakes: ~2 calories per gram
Panna Cotta: ~3.5 calories per gram
Peking Duck: ~4 calories per gram
Pho: ~1 calorie per gram
Pizza: ~2.5 calories per gram
Pork Chop: ~2.5 calories per gram
Poutine: ~2.5 calories per gram
Prime Rib: ~2.5 calories per gram
Pulled Pork Sandwich: ~2.5 calories per gram
Ramen: ~1 calorie per gram
Ravioli: ~1.5 calories per gram
Red Velvet Cake: ~4 calories per gram
Risotto: ~1.5 calories per gram
Samosa: ~2 calories per gram
Sashimi: ~1 calorie per gram
Scallops: ~1 calorie per gram
Seaweed Salad: ~0.5 calories per gram
Shrimp and Grits: ~2 calories per gram
Spaghetti Bolognese: ~1.5 calories per gram
Spaghetti Carbonara: ~2 calories per gram
Spring Rolls: ~1.5 calories per gram
Steak: ~2.5 calories per gram
Strawberry Shortcake: ~3.5 calories per gram
Sushi: ~1 calorie per gram
Tacos: ~2 calories per gram
Takoyaki: ~2.5 calories per gram
Tiramisu: ~3 calories per gram
Tuna Tartare: ~1.5 calories per gram
Waffles: ~2 calories per gram
"""
calories = s.splitlines()
s = "These values are approximations and can vary based on factors such as ingredients and cooking methods."

url1 = 'model1_lite.tflite'
url2 = 'model2_lite.tflite'
url3 = 'model3_lite.tflite'
url4 = 'model4_lite.tflite'
url5 = 'model5_lite.tflite'
url6 = 'model6_lite.tflite'
url8 = 'model8_lite.tflite'
url9 = 'model9_lite.tflite'
url10 = 'model10_lite.tflite'
url12 = 'model12_lite.tflite'
url13 = 'model13_lite.tflite'
url14 = 'model14_lite.tflite'
url15 = 'model15_lite.tflite'
url16 = 'model16_lite.tflite'

def load_model(url):
    model = tf.lite.Interpreter(model_path=url)
    model.allocate_tensors()
    return model

def rescale(img):
    img2 = img_to_array(img.convert('RGB'))
    img2 = img2/255
    img2 = img2.reshape(1,224,224,3)
    return img2

def predict(model,img):
    input_details = model.get_input_details()
    output_details = model.get_output_details()
    model.set_tensor(input_details[0]['index'],img)
    model.invoke()
    output_data = model.get_tensor(output_details[0]['index'])
    return output_data

def detect(original_img):
  output = ""
  img = rescale(original_img)
  model = load_model(url1)
  p1 = predict(model,img).argmax()
  # Food
  if p1==0:
    output = output+"Food image detected!  \n"
    model = load_model(url16)
    p1 = predict(model,img).argmax()
    output = output +f"{calories[p1]}  \nNote: {s}  \n"
  # Medical Imaging
  elif p1==1:
    output = output+"Medical Imaging image detected!  \n"
    model = load_model(url2)
    p1 = predict(model,img).argmax()
#_____________________________________________________________ 
    # CT
    if p1==0:
      output = output+"CT Scan detected!  \n"
      model = load_model(url14)
      p1 = predict(model,img).argmax()
      output = output+ f"{ct[p1]} detected!  \n"
      if ct[p1] == "Normal":
        pass
      else:
        output = output +f"{scan_info[ct[p1]]}  \n"
    # MRI
    elif p1==1:
      output = output+"MRI detected!  \n"
      model = load_model(url8)
      p1 = (predict(model,img)>=0.5).astype(int)[0,0]
      # Brain MRI
      if p1==0:
        output = output+"Brain MRI detected!  \n"
        model = load_model(url9)
        p1 = (predict(model,img)>=0.5).astype(int)[0,0]
        # No tumor
        if p1==0:
          output = output+"No tumor found  \n"
        # tumor
        else: # =1
          output =output+"Brain tumor detected!  \n"
          model = load_model(url10)
          p1 = predict(model,img).argmax()
          output = output+f"{tumor_type[p1]} type detected!  \n"
          if tumor_type[p1] == "normal no_tumor":
            pass
          else:
            output = output+f"{scan_info[tumor_type[p1]]}  \n"
      # Breast MRI
      else: # =1
        output = output+"Breast MRI detected!  \n"
        model = load_model(url12)
        p1 = (predict(model,img)>=0.5).astype(int)[0,0]
        # no cancer
        if p1==0:
          output = output+"Healthy breast  \n"
        # Breast cancer
        else: #1
          output = output+"Breast Cancer detected!  \n"
          model = load_model(url13)
          p1 = (predict(model,img)>=0.5).astype(int)[0,0]
          # Benign Breast Cancer
          if p1==0:
            output = output+"Benign breast cancer detected!  \n"
          # Malignant
          else: #1
            output = output+"Malignant breast cancer detected!  \n"
          output = output+f"{scan_info['breast_cancer']}  \n"
    # OCT
    elif p1==2:
      output = output+"OCT Scan detected!  \n"
      model = load_model(url15)
      p1 = predict(model,img).argmax()
      output = output+f"{oct[p1]} eyes detected!  \n"
      if oct[p1] == "Normal":
        pass
      else:
        output = output+f"{scan_info[oct[p1]]}  \n"
        # print(scan_info[oct[p1]])
    # xray
    else: # = 3
      output = output+"x-ray detected!  \n"
      model = load_model(url3)
      p1 = predict(model,img).argmax()
      # chest body part
      if p1==0:
        output = output+"Chest x-ray detected!  \n"
        model = load_model(url4)
        p1 = (predict(model,img)).argmax()
        # covid
        if p1==0:
          output = output+"Covid_19 detected!  \n"
          output = output+f"{scan_info['Covid']}  \n"
        # Normal
        elif p1==1:
          output = output+"Normal Healthy chest x-ray  \n"
        # Pneumonia
        elif p1==2:
          output = output+"Pneumonia on chest detected!  \n"
          output = output+f"{scan_info['Pneumonia']}  \n"
      # Other body parts
      else:
        output = output+f"{body_parts[p1]} body part x-ray detected!  \n"
        model = load_model(url5)
        p1 = (predict(model,img)>=0.5).astype(int)[0,0]
        # Fractured
        if p1==0:
          output = output+"Fractured bones detected!  \n"
          model = load_model(url6)
          p1 = (predict(model,img)).argmax(axis=1)[0]
          output = output+f"{fracture_type[p1]}  \n"
          output = output +f"{scan_info[fracture_type[p1]]}  \n"
        # Not fractured
        else: # =1
          output = output+"Normal unfractured bones  \n"
#_____________________________________________________________
  # Other
  else: # == 2
      output = output+"ERROR: Unsupported image object!  \nPlease try to enter a valid 'Medical imaging' or 'food' image  \n"
  return output

st.image("cropedLogo.png")
st.title("I-Care")
st.info("Medical Imaging Scan - Easy Healthcare for Anyone Anytime")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    # img = rescale(image)
    output = detect(img)
    st.write(output)
