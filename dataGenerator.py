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
    'Anesthesia',
    'Cardiology',
    'Pediatrics',
    'Ophthalmology',
    'Neurology',
    'Hematology',
    'Gynecology',
    'Dermatology',
    'Family Practice',
    'Oncology',
    'Psychiatry',
    'Orthopedic',
    'Urology'
];
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
LIM = 1000;
amountDoctors = 100;
while i < LIM:
    patient = random.randint(1, LIM);
    posYear = random.randint(0,len(years)-1);
    month = random.randint(1,12);
    #day = random.randint(1,
    posState = random.randint(0,len(states)-1);
    posHospital = random.randint(0,len(hospitals[posState])-1);
    posDisease = random.randint(0,amountDoctors-1);
    posSpecialty = random.randint(0,len(specialties)-1);

    line = [patient,years[posYear],month,states[posState],hospitals[posHospital],
            specialties[posSpecialty]
            ];
    output.append(line);
    
    i = i + 1;

print(output);   
#print (states);
#print ('\n');
#print(hospitals);
#print ('\n');
#print(diseases);
#print ('\n');
#print(specialties);
#print ('\n');


