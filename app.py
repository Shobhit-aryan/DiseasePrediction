from flask import Flask, render_template, request
import pickle
import pandas as pd

sympDesc = pd.read_csv(r'E:\S-5\HealthProject\Disease-prediction\data-disease-symptom-description\symptom_Description.csv')
sympDesc.head()

classifier = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/symptom.html')
def symp():
    return render_template('symptom.html')
@app.route('/output.html')
def out():
    return render_template('output.html')
@app.route('/atozmedicine.html')
def atozmedicine():
    return render_template('atozmedicine.html')
@app.route('/atozdisease.html')
def atozdisease():
    return render_template('atozdisease.html')
@app.route('/atoztest.html')
def atoztest():
    return render_template('atoztest.html')
@app.route('/a1.html')
def a1():
    return render_template('a1.html')
@app.route('/a2.html')
def a2():
    return render_template('a2.html')
@app.route('/a3.html')
def a3():
    return render_template('a3.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        symptom1 = request.form['symp1']
        symptom2 = request.form['symp2']
        symptom3 = request.form['symp3']
        symptom4 = request.form['symp4']
        input_symptoms = symptom1+" "+symptom2+" "+symptom3+" "+symptom4
        data = [input_symptoms]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        if(my_prediction==0):
            return render_template('output.html', prediction="Yellow Fever", description='Yellow fever is a viral infection spread by a particular type of mosquito. The infection is most common in areas of Africa and South America, affecting travelers to and residents of those areas.',treatment='No antiviral medications have proved helpful in treating yellow fever. As a result, treatment consists primarily of supportive care in a hospital. This includes providing fluids and oxygen, maintaining adequate blood pressure, replacing blood loss, providing dialysis for kidney failure, and treating any other infections that develop.')
        elif (my_prediction == 1):
            return render_template('output.html', prediction="AIDS", description='Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV). By damaging your immune system, HIV interferes with your body\'s ability to fight infection and disease.',treatment='Antibody tests. These tests look for antibodies to HIV in blood or saliva. Most rapid HIV tests, including self-tests done at home, are antibody tests. Antibody tests can take three to 12 weeks after you are exposed to become positive.')
        elif (my_prediction == 2):
            return render_template('output.html', prediction="Acne", description='Acne is a skin condition that occurs when your hair follicles become plugged with oil and dead skin cells. It causes whiteheads, blackheads or pimples. Acne is most common among teenagers, though it affects people of all ages.',treatment='Acne medications work by reducing oil production and swelling or by treating bacterial infection. With most prescription acne drugs, you may not see results for four to eight weeks. It can take many months or years for your acne to clear up completely.')
        elif (my_prediction == 3):
            return render_template('output.html', prediction="Alcoholic hepatitis", description='Alcoholic hepatitis is most likely to occur in people who drink heavily over many years. However, the relationship between drinking and alcoholic hepatitis is complex. ',treatment='Treatment for alcoholic hepatitis involves quitting drinking and therapies to ease the signs and symptoms of liver damage.')
        elif (my_prediction == 4):
            return render_template('output.html', prediction="Allergy", description='Allergies occur when your immune system reacts to a foreign substance — such as pollen, bee venom or pet dander — or a food that doesnot cause a reaction in most people.',treatment='Medications. Depending on your allergy, medications can help reduce your immune system reaction and ease symptoms. Your doctor might suggest over-the-counter or prescription medication in the form of pills or liquid, nasal sprays, or eyedrops.')
        elif (my_prediction == 5):
            return render_template('output.html', prediction="Arthritis", description='Arthritis is the swelling and tenderness of one or more of your joints. The main symptoms of arthritis are joint pain and stiffness, which typically worsen with age.',treatment='Arthritis treatment focuses on relieving symptoms and improving joint function. You may need to try several different treatments, or combinations of treatments, before you determine what works best for you.')
        elif (my_prediction == 6):
            return render_template('output.html', prediction="Bronchial Asthma", description='Asthma is a condition in which your airways narrow and swell and may produce extra mucus. This can make breathing difficult and trigger coughing, a whistling sound (wheezing) when you breathe out and shortness of breath.',treatment='Prevention and long-term control are key to stopping asthma attacks before they start. Treatment usually involves learning to recognize your triggers, taking steps to avoid triggers and tracking your breathing to make sure your medications are keeping symptoms under control. ')
        elif (my_prediction == 7):
            return render_template('output.html', prediction="Cervical spondylosis", description='Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck. As the disks dehydrate and shrink, signs of osteoarthritis develop, including bony projections along the edges of bones (bone spurs).',treatment='Treatment for cervical spondylosis depends on the severity of your signs and symptoms. The goal of treatment is to relieve pain, help you maintain your usual activities as much as possible, and prevent permanent injury to the spinal cord and nerves.')
        elif (my_prediction == 8):
            return render_template('output.html', prediction="Chicken pox", description='Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 and 500 itchy blisters.',treatment='There are several things that you can do at home to help relieve chickenpox symptoms and prevent skin infections. Calamine lotion and a cool bath with added baking soda, uncooked oatmeal, or colloidal oatmeal may help relieve some of the itching. Try to minimize scratching to prevent the virus from spreading to others and potential bacterial infection from occurring.')
        elif (my_prediction == 9):
            return render_template('output.html', prediction="Chronic cholestasis", description='Intrahepatic cholestasis of pregnancy, commonly known as cholestasis of pregnancy, is a liver condition that occurs in late pregnancy. The condition triggers intense itching, but without a rash. Itching usually occurs on the hands and feet but can also affect other parts of the body.',treatment='The goals of treatment for cholestasis of pregnancy are to ease itching and prevent complications in your baby.')
        elif (my_prediction == 10):
            return render_template('output.html', prediction="Common Cold", description='The common cold is a viral infection of your nose and throat (upper respiratory tract). It is usually harmless, although it might not feel that way. Many types of viruses can cause a common cold.',treatment='There is no cure for the common cold. Antibiotics are of no use against cold viruses and shouldnot be used unless there is a bacterial infection. Treatment is directed at relieving signs and symptoms.')
        elif (my_prediction == 11):
            return render_template('output.html', prediction="Dengue", description='Dengue (DENG-gey) fever is a mosquito-borne disease that occurs in tropical and subtropical areas of the world. Mild dengue fever causes a high fever, rash, and muscle and joint pain. A severe form of dengue fever, also called dengue hemorrhagic fever',treatment='No specific treatment for dengue fever exists. Your doctor may recommend that you drink plenty of fluids to avoid dehydration from vomiting and a high fever.')
        elif (my_prediction == 12):
            return render_template('output.html', prediction="Diabetes", description='Diabetes mellitus refers to a group of diseases that affect how your body uses blood sugar (glucose). Glucose is vital to your health because it is an important source of energy for the cells that make up your muscles and tissues. It is also your brain is main source of fuel.',treatment='Depending on what type of diabetes you have, blood sugar monitoring, insulin and oral medications may play a role in your treatment. Eating a healthy diet, maintaining a healthy weight and participating in regular activity also are important factors in managing diabetes.')
        elif (my_prediction == 13):
            return render_template('output.html', prediction="Dimorphic hemmorhoids(piles)", description='Hemorrhoids (HEM-uh-roids), also called piles, are swollen veins in your anus and lower rectum, similar to varicose veins. Hemorrhoids can develop inside the rectum (internal hemorrhoids) or under the skin around the anus (external hemorrhoids).',treatment=' Apply an over-the-counter hemorrhoid cream or suppository containing hydrocortisone, or use pads containing witch hazel or a numbing agent.')
        elif (my_prediction == 14):
            return render_template('output.html', prediction="Drug Reaction", description='Drug addiction, also called substance use disorder, is a disease that affects a persons  brain and behavior and leads to an inability to control the use of a legal or illegal drug or medication. Substances such as alcohol, marijuana and nicotine also are considered drugs. ',treatment='Although there is no cure for drug addiction, treatment options explained below can help you overcome an addiction and stay drug-free. Your treatment depends on the drug used and any related medical or mental health disorders you may have. Long-term follow-up is important to prevent relapse.')
        elif (my_prediction == 15):
            return render_template('output.html', prediction="Fungal infection", description='Nail fungus is a common condition that begins as a white or yellow spot under the tip of your fingernail or toenail. ',treatment='Fungal nail infections can be difficult to treat. Talk with your doctor if self-care strategies and over-the-counter (nonprescription) products havenot helped. Treatment depends on the severity of your condition and the type of fungus causing it. It can take months to see results. ')
        elif (my_prediction == 16):
            return render_template('output.html', prediction="GERD", description='Gastroesophageal reflux disease (GERD) occurs when stomach acid frequently flows back into the tube connecting your mouth and stomach (esophagus). This backwash (acid reflux) can irritate the lining of your esophagus.',treatment='Your doctor is likely to recommend that you first try lifestyle modifications and over-the-counter medications. If you donot experience relief within a few weeks, your doctor might recommend prescription medication or surgery.')
        elif (my_prediction == 17):
            return render_template('output.html', prediction="Gastroenteritis", description='Viral gastroenteritis is an intestinal infection marked by watery diarrhea, abdominal cramps, nausea or vomiting, and sometimes fever.',treatment='There is often no specific medical treatment for viral gastroenteritis. Antibiotics arenot effective against viruses, and overusing them can contribute to the development of antibiotic-resistant strains of bacteria. Treatment initially consists of self-care measures.')
        elif (my_prediction == 18):
            return render_template('output.html', prediction="Heart attack", description='A heart attack occurs when the flow of blood to the heart is blocked. The blockage is most often a buildup of fat, cholesterol and other substances, which form a plaque in the arteries that feed the heart (coronary arteries).',treatment='Aspirin. The 911 operator might tell you to take aspirin, or emergency medical personnel might give you aspirin immediately. Aspirin reduces blood clotting, thus helping maintain blood flow through a narrowed artery.Thrombolytics. These drugs, also called clotbusters, help dissolve a blood clot that is blocking blood flow to your heart. ')
        elif (my_prediction == 19):
            return render_template('output.html', prediction="Hepatitis B", description='Hepatitis B is a serious liver infection caused by the hepatitis B virus (HBV). For some people, hepatitis B infection becomes chronic, meaning it lasts more than six months. Having chronic hepatitis B increases your risk of developing liver failure, liver cancer or cirrhosis — a condition that permanently scars of the liver.',treatment='If you know you have been exposed to the hepatitis B virus and arenot sure if you have been vaccinated, call your doctor immediately. An injection of immunoglobulin (an antibody) given within 12 hours of exposure to the virus may help protect you from getting sick with hepatitis B.')
        elif (my_prediction == 20):
            return render_template('output.html', prediction="Hepatitis C", description='Hepatitis C is a viral infection that causes liver inflammation, sometimes leading to serious liver damage. The hepatitis C virus (HCV) spreads through contaminated blood.',treatment='Hepatitis C infection is treated with antiviral medications intended to clear the virus from your body. The goal of treatment is to have no hepatitis C virus detected in your body at least 12 weeks after you complete treatment.')
        elif (my_prediction == 21):
            return render_template('output.html', prediction="Hepatitis D", description='Autoimmune hepatitis is liver inflammation that occurs when your body is immune system turns against liver cells. The exact cause of autoimmune hepatitis is unclear, but genetic and enviromental factors appear to interact over time in triggering the disease.',treatment='Regardless of which type of autoimmune hepatitis you have, the goal of treatment is to slow or stop the immune system attack on your liver. This may help slow the progression of the disease. To meet this goal, you will need medications that lower immune system activity.')
        elif (my_prediction == 22):
            return render_template('output.html', prediction="Hepatitis E", description='Toxic hepatitis is an inflammation of your liver in reaction to certain substances to which you are exposed. Toxic hepatitis can be caused by alcohol, chemicals, drugs or nutritional supplements.',treatment='Doctors will work to determine what is causing your liver damage. Sometimes it is clear what is causing your symptoms, and other times it takes more detective work to pinpoint a cause. In most cases, stopping exposure to the toxin causing liver inflammation will reduce the signs and symptoms you experience.')
        elif (my_prediction == 23):
            return render_template('output.html', prediction="Hypertension", description='High blood pressure is a common condition in which the long-term force of the blood against your artery walls is high enough that it may eventually cause health problems, such as heart disease.',treatment='The category of medication your doctor prescribes depends on your blood pressure measurements and your other medical problems. It is helpful if you work together with a team of medical professionals experienced in providing treatment for high blood pressure to develop an individualized treatment plan.')
        elif (my_prediction == 24):
            return render_template('output.html', prediction="Hyperthyroidism", description='Hyperthyroidism (overactive thyroid) occurs when your thyroid gland produces too much of the hormone thyroxine. Hyperthyroidism can accelerate your body is metabolism, causing unintentional weight loss and a rapid or irregular heartbeat.',treatment='Anti-thyroid medications. These medications gradually reduce symptoms of hyperthyroidism by preventing your thyroid gland from producing excess amounts of hormones. ')
        elif (my_prediction == 25):
            return render_template('output.html', prediction="Hypoglycemia", description='Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal. Glucose is your body is main energy source.',treatment='Eat or drink 15 to 20 grams of fast-acting carbohydrates. These are sugary foods without protein or fat that are easily converted to sugar in the body. Try glucose tablets or gel, fruit juice, regular — not diet — soft drinks, honey, and sugary candy.')
        elif (my_prediction == 26):
            return render_template('output.html', prediction="Hypothyroidism", description='Hypothyroidism (underactive thyroid) is a condition in which your thyroid gland doesnot produce enough of certain crucial hormones.',treatment='Standard treatment for hypothyroidism involves daily use of the synthetic thyroid hormone levothyroxine (Levo-T, Synthroid, others). This oral medication restores adequate hormone levels, reversing the signs and symptoms of hypothyroidism.')
        elif (my_prediction == 27):
            return render_template('output.html', prediction="Impetigo", description='Impetigo (im-puh-TIE-go) is a common and highly contagious skin infection that mainly affects infants and children. Impetigo usually appears as red sores on the face, especially around a child nose and mouth, and on hands and feet. The sores burst and develop honey-colored crusts.',treatment='Impetigo typically is treated with an antibiotic ointment or cream that you apply directly to the sores. You may need to first soak the affected area in warm water or use wet compresses to help remove the scabs so the antibiotic can penetrate the skin.')
        elif (my_prediction == 28):
            return render_template('output.html', prediction="Jaundice", description='Jaundice causes your skin and the whites of your eyes to turn yellow. Too much bilirubin causes jaundice. Bilirubin is a yellow chemical in hemoglobin, the substance that carries oxygen in your red blood cells. ',treatment='Anemia-induced jaundice may be treated by boosting the amount of iron in the blood by either taking iron supplements or eating more iron-rich foods.')
        elif (my_prediction == 29):
            return render_template('output.html', prediction="Malaria", description='Malaria is a disease caused by a parasite. The parasite is transmitted to humans through the bites of infected mosquitoes. People who have malaria usually feel very sick, with a high fever and shaking chills.',treatment='Malaria is treated with prescription drugs to kill the parasite. The types of drugs and the length of treatment will vary. New antimalarial drugs are being researched and developed. Malaria treatment is marked by a constant struggle between evolving drug-resistant parasites and the search for new drug formulations. ')
        elif (my_prediction == 30):
            return render_template('output.html', prediction="Migraine", description='A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. It is often accompanied by nausea, vomiting, and extreme sensitivity to light and sound.',treatment='Pain-relieving medications. Also known as acute or abortive treatment, these types of drugs are taken during migraine attacks and are designed to stop symptoms.')
        elif (my_prediction == 31):
            return render_template('output.html', prediction="Osteoarthristis", description='Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide. It occurs when the protective cartilage that cushions the ends of your bones wears down over time.',treatment='Osteoarthritis cannot be reversed, but treatments can reduce pain and help you move better.')
        elif (my_prediction == 32):
            return render_template('output.html', prediction="Paralysis (brain hemorrhage)", description='Paralysis is the loss of muscle function in part of your body. It happens when something goes wrong with the way messages pass between your brain and muscles.',treatment='Physical therapy uses treatments such as heat, massage, and exercise to stimulate nerves and muscles.')
        elif (my_prediction == 33):
            return render_template('output.html', prediction="Vertigo", description='Benign paroxysmal positional vertigo (BPPV) is one of the most common causes of vertigo — the sudden sensation that you are spinning or that the inside of your head is spinning.',treatment='Benign paroxysmal positional vertigo may go away on its own within a few weeks or months. But, to help relieve BPPV sooner, your doctor, audiologist or physical therapist may treat you with a series of movements known as the canalith repositioning procedure.')
        elif (my_prediction == 34):
            return render_template('output.html', prediction="Pneumonia", description='Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. ',treatment='Treatment for pneumonia involves curing the infection and preventing complications. People who have community-acquired pneumonia usually can be treated at home with medication.')
        elif (my_prediction == 35):
            return render_template('output.html', prediction="Psoriasis", description='Psoriasis is a skin disease that causes red, itchy scaly patches, most commonly on the knees, elbows, trunk and scalp.',treatment='Psoriasis treatments aim to stop skin cells from growing so quickly and to remove scales. Options include creams and ointments (topical therapy), light therapy (phototherapy), and oral or injected medication.')
        elif (my_prediction == 36):
            return render_template('output.html', prediction="Tuberculosis", description='Tuberculosis (TB) is a potentially serious infectious disease that mainly affects your lungs. The bacteria that cause tuberculosis are spread from one person to another through tiny droplets released into the air via coughs and sneezes.',treatment='Medications are the cornerstone of tuberculosis treatment. But treating TB takes much longer than treating other types of bacterial infections.')
        elif (my_prediction == 37):
            return render_template('output.html', prediction="Typhoid", description='Typhoid fever is caused by Salmonella typhi bacteria. Typhoid fever is rare in industrialized countries. However, it remains a serious health threat in the developing world, especially for children.',treatment='Ciprofloxacin (Cipro) ,Azithromycin (Zithromax), and Ceftriaxone  drugs can cause side effects, and long-term use can lead to the development of antibiotic-resistant strains of bacteria.')
        elif (my_prediction == 38):
            return render_template('output.html', prediction="Urinary tract infection", description='A urinary tract infection (UTI) is an infection in any part of your urinary system — your kidneys, ureters, bladder and urethra. Most infections involve the lower urinary tract — the bladder and the urethra.',treatment='Antibiotics usually are the first line treatment for urinary tract infections. Which drugs are prescribed and for how long depend on your health condition and the type of bacteria found in your urine.')
        elif (my_prediction == 39):
            return render_template('output.html', prediction="Varicose veins", description='Varicose veins are twisted, enlarged veins. Any superficial vein may become varicosed, but the veins most commonly affected are those in your legs.',treatment='Fortunately, treatment usually doesnot mean a hospital stay or a long, uncomfortable recovery. Thanks to less invasive procedures, varicose veins can generally be treated on an outpatient basis.')
        elif (my_prediction == 40):
            return render_template('output.html', prediction="hepatitis A", description='Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. The virus is one of several types of hepatitis viruses that cause inflammation and affect your liver ability to function.',treatment='No specific treatment exists for hepatitis A. Your body will clear the hepatitis A virus on its own. In most cases of hepatitis A, the liver heals within six months with no lasting damage.')
        else:
            return render_template('output.html', prediction="Sorry Can't Predict")
    
if __name__=='__main__':
    app.run(debug=True)
