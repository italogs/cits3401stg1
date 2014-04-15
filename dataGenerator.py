import random, sys
##
##for i in range(0,3*7):
##    print (i);
##
##sys.exit();



states = ['New South Wales','Northern Territory','Queensland','South Australia','Tasmania','Victoria','Western Australia'];
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
years = ["2006","2007","2008","2009","2010","2011"];

hospitals = [
    [#New South Wales
        'Manly Hospital',
        'Royal North Shore Hospital',
        'Gosford Hospital',
        'Mater Hospital'
    ],
    [#Northern Territory
        'Alice Springs Hospital',
        'Royal Darwin Hospital',
        'Katherine District Hospital'
    ],
    [#Queensland
        'Princess Alexandra Hospital',
        'The Prince Charles Hospital',
        'Ipswich Hospital',
        'Normanton Hospital'
    ],
    [#South Australia
        'Flinders Medical Centre',
        'The Queen Elizabeth Hospital',
        'Quorn Hospital',
        'Port Lincoln Health Services'
    ],
    [#Tasmania
        'Royal Hobart Hospital',
        'St Lukes Private Hospital',
        'Mersey Community Hospital'
    ],
    [#Victoria
        'The Alfred Hospital',
        'Monash Medical Centre',
        'Werribee Mercy Hospital',
        'Geelong Hospital'
    ],
    [#Western Australia
        'Royal Perth Hospital',
        'Sir Charles Gairdner Hospital',
        'King Edward Memorial Hospital for Women',
        'Graylands Hospital'
    ]
];#26 hospitals


#http://emedicine.medscape.com/
diseases = [
    'Acute encephalitis',
    'Acute infectious hepatitis',
    'Acute meningitis',
    'Acute poliomyelitis',
    'Anthrax',
    'Botulism',
    'Brucellosis',
    'Cholera',
    'Diphtheria',
    'Enteric fever',
    'Food poisoning',
    'Leprosy',
    'Malaria',
    'Tetanus',
    'Tuberculosis',
    'Typhus',
    'Yellow fever'
];

specialties = [
    'Cardiology',
    'Oncology',
    'Dermatology',
    'Neurology',
    'Radiology',
    'Endocrinology',
    'Hematology',
    'Gynecology'
];

diseases = [];
diseases.append(['Cardiac Sarcoma','Hypertension','Pediatric Tachycardia']);
diseases.append(['Breast Cancer','Adrenal Carcinoma','Thyroid Lymphoma']);
diseases.append(['Drug Eruptions','Chancroid','Ecthyma']);
diseases.append(['Depression','Panic Disorder','Schizophrenia']);
diseases.append(['Cardiac Tumor Imaging','Empyema Imaging','Pneumothorax Imaging']);
diseases.append(['Hypoglycemia','Insulinoma','Osteopetrosis']);
diseases.append(['Neutrophilia','Splenomegaly','Anemia']);
diseases.append(['Vaginitis','Endometritis','Hysteroscopy']);


output = [];
line = [];



i = 0;


#Control variables

pricePerDayTreatment = 500;
numberOfGPPerHospital = 3;

numberOfHospitalsPerRegion = [len(hospitals[j]) for j in range(len(hospitals))];

patientsPerState = 20;
numberOfPatients = len(states)*patientsPerState;#The number of patients is 100 per State
numberOfInteractions = 50;#Number of register that will appear on output file

LIMITPharmaceuticalBenefit = 350;

while i < numberOfInteractions:
    posState = random.randint(0,len(states)-1);
    patientID = random.randint(posState*patientsPerState,((posState+1)*patientsPerState)- 1);
    gpID = random.randint(posState*numberOfGPPerHospital,((posState+1)*numberOfGPPerHospital)- 1);
    

    
    posYear = random.randint(0,len(years)-1);
    posMonth = random.randint(0,11);
    day = random.randint(1,28);
    durationAppointment = str(random.randint(20,50)) + ':' + str(random.randint(10,59));
    
    posHospital = random.randint(0,len(hospitals[posState])-1);
    
    posDisease = random.randint(0,3);
    posSpecialty = random.randint(0,len(specialties)-1);
    posDisease = random.randint(0,len(diseases[posSpecialty])-1);

    specialistID = 1;
    
    delayDays = random.randint(0,365);
    durationTreatment = random.randint(1,180);
    daysInHospital = random.randint(0,100);
    totalTreatmentCost = daysInHospital*pricePerDayTreatment;
    privateInsurance = random.randint(0,5);
    totalSpentPharmaceuticalBenefit = random.randint(0,500);

    if(privateInsurance > 4):
        privateInsurance = "Yes";
    else:
        privateInsurance = "No";
    
    line = [
            #General Data
            str(patientID),
            str(gpID),
            str(specialistID),
            years[posYear],
            months[posMonth],
            str(day),
            hospitals[posState][posHospital],
            diseases[posSpecialty][posDisease],
            

            #Measures
            privateInsurance,
            str(delayDays),
            durationAppointment,
            str(1),#just a counter
            str(totalTreatmentCost),
            str(totalSpentPharmaceuticalBenefit)
    ];
    output.append(line);
    i = i + 1;



    

f = open('output.txt', 'w')

for s in output:
    f.write(','.join(s)+'\n');

f.close();
print('END');
