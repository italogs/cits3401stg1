#http://emedicine.medscape.com/

import random

states = [
    'New South Wales',
    'Northern Territory',
    'Queensland',
    'South Australia',
    'Tasmania',
    'Victoria',
    'Western Australia'
];

months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
];
hospitals = [
    #New South Wales
    [
        'Manly Hospital',
        'Royal North Shore Hospital',
        'Gosford Hospital',
        'Mater Hospital'
    ],
    #Northern Territory
    [
        'Alice Springs Hospital',
        'Royal Darwin Hospital',
        'Katherine District Hospital'
    ],
    #Queensland
    [
        'Princess Alexandra Hospital',
        'The Prince Charles Hospital',
        'Ipswich Hospital',
        'Normanton Hospital'
    ],
    #South Australia
    [
        'Flinders Medical Centre',
        'The Queen Elizabeth Hospital',
        'Quorn Hospital',
        'Port Lincoln Health Services'
    ],
    #Tasmania
    [
        'Royal Hobart Hospital',
        'St Lukes Private Hospital',
        'Mersey Community Hospital'
    ],
    #Victoria
    [
        'The Alfred Hospital',
        'Monash Medical Centre',
        'Werribee Mercy Hospital',
        'Geelong Hospital'
    ],
    #Western Australia
    [
        'Royal Perth Hospital',
        'Sir Charles Gairdner Hospital',
        'King Edward Memorial Hospital for Women',
        'Graylands Hospital'
    ]
];
i = 0;
amountDoctors = 0;
doctors = [];
while i < len(hospitals):
    #3 doctors for each hospital
    doctors.append(len(hospitals[i])*3);
    amountDoctors = amountDoctors + len(hospitals[i])*3;
    i = i + 1


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

years = [
    2006,
    2007,
    2008,
    2009,
    2010,
    2011
];

output = [];
line = [];
i = 0;
LIM = 50;
variableNames = [
    'Patient',
    'Year',
    'Month',
    'State',
    'Doctor',
    'Hospital',
    'Specialty',
    'Disease'
];
while i < LIM:
    patient = random.randint(1, LIM);
    posYear = random.randint(0,len(years)-1);
    month = random.randint(0,11);
    posState = random.randint(0,len(states)-1);
    numDoctor = random.randint(1,doctors[posState]);
    posHospital = random.randint(0,len(hospitals[posState])-1);
    posDisease = random.randint(0,amountDoctors-1);
    posSpecialty = random.randint(0,len(specialties)-1);
    posDisease = random.randint(0,len(diseases[posSpecialty])-1);
    treatmentCost = 1000;
    daysInHospital = random.randint(0,100);
    line = [
            #str(patient),
            str(years[posYear]),
            str(months[month]),
            str(states[posState]),
            #str(numDoctor),
            #hospitals[posState][posHospital],
            #specialties[posSpecialty]
            diseases[posSpecialty][posDisease],
            #str(1000),
            #str("Units"),
            str(1)
            #str(daysInHospital),
            #str(treatmentCost)
            #str(33)
    ];
    output.append(line);
    i = i + 1;

f = open('output.txt', 'w')

for s in output:
    f.write(','.join(s)+'\n');

f.close();
print('END');
