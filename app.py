import pickle
import pandas as pd
from flask import Flask,render_template,redirect,request, session

blr=pickle.load(open('static/models/modelblr.pkl','rb'))
chennai=pickle.load(open('static/models/modelchennai.pkl','rb'))
delhi=pickle.load(open('static/models/modeldelhi.pkl','rb'))
hyd=pickle.load(open('static/models/modelhyd.pkl','rb'))
kolkata=pickle.load(open('static/models/modelkolkata.pkl','rb'))
mumbai=pickle.load(open('static/models/modelmumbai.pkl','rb'))
anantapur=pickle.load(open('static/models/modelanantapur.pkl','rb'))
chittoor=pickle.load(open('static/models/modelchittoor.pkl','rb'))
kurnool=pickle.load(open('static/models/modelkurnool.pkl','rb'))
nandyal=pickle.load(open('static/models/modelnandyal.pkl','rb'))

app=Flask(__name__)
app.secret_key='mindhack'

@app.route('/')
def homePage():
    dataset=pd.read_csv('datasets/Bangalore.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    
    return render_template('index.html',dashboard_data1=locations,len1=len(locations))

@app.route('/delhi')
def delhiPage():
    dataset=pd.read_csv('datasets/Delhi.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('delhi.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictdelhi',methods=['post','get'])
def predictdelhi():

    dataset=pd.read_csv('datasets/Delhi.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=delhi.predict(datasample)
    return render_template('delhi.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/hyderabad')
def hyderabadPage():
    dataset=pd.read_csv('datasets/Hyderabad.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('hyderabad.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predicthyd',methods=['post','get'])
def predicthyd():

    dataset=pd.read_csv('datasets/Hyderabad.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=hyd.predict(datasample)
    return render_template('hyderabad.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/kolkata')
def kolkataPage():
    dataset=pd.read_csv('datasets/Kolkata.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('kolkata.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictkolkata',methods=['post','get'])
def predictkolkata():

    dataset=pd.read_csv('datasets/Kolkata.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=kolkata.predict(datasample)
    return render_template('kolkata.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/mumbai')
def mumbaiPage():
    dataset=pd.read_csv('datasets/Mumbai.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('mumbai.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictmumbai',methods=['post','get'])
def predictmumbai():

    dataset=pd.read_csv('datasets/Mumbai.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=mumbai.predict(datasample)
    return render_template('mumbai.html',dashboard_data1=locations,result=result[0],len1=len(locations))


@app.route('/kurnool')
def kurnoolPage():
    dataset=pd.read_csv('datasets/Kurnool.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('kurnool.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictkurnool',methods=['post','get'])
def predictkurnool():

    dataset=pd.read_csv('datasets/Kurnool.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=kurnool.predict(datasample)
    return render_template('kurnool.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/nandyal')
def nandyalPage():
    dataset=pd.read_csv('datasets/Nandyal.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('nandyal.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictnandyal',methods=['post','get'])
def predictnandyal():

    dataset=pd.read_csv('datasets/Nandyal.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=nandyal.predict(datasample)
    return render_template('nandyal.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/chittoor')
def chittoorPage():
    dataset=pd.read_csv('datasets/Chittoor.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('chittoor.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictchittoor',methods=['post','get'])
def predictchittoor():

    dataset=pd.read_csv('datasets/Chittoor.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=chittoor.predict(datasample)
    return render_template('chittoor.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/anantapur')
def anantapurPage():
    dataset=pd.read_csv('datasets/Anantapur.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('anantapur.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictanantapur',methods=['post','get'])
def predictanantapur():

    dataset=pd.read_csv('datasets/Anantapur.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=anantapur.predict(datasample)
    return render_template('anantapur.html',dashboard_data1=locations,result=result[0],len1=len(locations))




@app.route('/chennai')
def chennaiPage():
    dataset=pd.read_csv('datasets/Chennai.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)
    return render_template('chennai.html',dashboard_data1=locations,len1=len(locations))

@app.route('/predictchennai',methods=['post','get'])
def predictchennai():

    dataset=pd.read_csv('datasets/Chennai.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=chennai.predict(datasample)
    return render_template('chennai.html',dashboard_data1=locations,result=result[0],len1=len(locations))

@app.route('/predictblr',methods=['post','get'])
def predictblr():

    dataset=pd.read_csv('datasets/Bangalore.csv')
    locations=[]
    for i in dataset.Location:
        if i not in locations:
            locations.append(i)

    area=request.form['area']
    location=request.form['location']
    location=locations.index(location)
    noofbedrooms=request.form['noofbedrooms']
    resale=request.form['resale']
    maintenancestaff=request.form['maintenancestaff']
    gym=request.form['gym']
    sp=request.form['sp']
    gardens=request.form['gardens']
    jog=request.form['jog']
    rainwater=request.form['rainwater']
    indoorgames=request.form['indoorgames']
    mall=request.form['mall']
    intercom=request.form['intercom']
    sports=request.form['sports']
    atm=request.form['atm']
    club=request.form['club']
    school=request.form['school']
    security=request.form['security']
    power=request.form['power']
    car=request.form['car']
    staff=request.form['StaffQuarter']
    cafe=request.form['cafe']
    mproom=request.form['mproom']
    hospital=request.form['hospital']
    washingmachine=request.form['washingmachine']
    gas=request.form['gas']
    ac=request.form['ac']
    childrenplayarea=request.form['childrenplayarea']
    lift=request.form['lift']
    bed=request.form['bed']
    vaastu=request.form['vaastu']
    microwave=request.form['microwave']
    golf=request.form['golf']
    tv=request.form['tv']
    diningtable=request.form['diningtable']
    sofa=request.form['sofa']
    fridge=request.form['fridge']

    if resale=='Yes':
        resale=1
    else:
        resale=0
    
    if maintenancestaff=='Yes':
        maintenancestaff=1
    else:
        maintenancestaff=0
    
    if gym=='Yes':
        gym=1
    else:
        gym=0
    
    if sp=='Yes':
        sp=1
    else:
        sp=0
    
    if gardens=='Yes':
        gardens=1
    else:
        gardens=0
    
    if jog=='Yes':
        jog=1
    else:
        jog=0
    
    if rainwater=='Yes':
        rainwater=1
    else:
        rainwater=0
    
    if indoorgames=='Yes':
        indoorgames=1
    else:
        indoorgames=0
    
    if mall=='Yes':
        mall=1
    else:
        mall=0
    
    if intercom=='Yes':
        intercom=1
    else:
        intercom=0
    
    if sports=='Yes':
        sports=1
    else:
        sports=0
    
    if atm=='Yes':
        atm=1
    else:
        atm=0
    
    if club=='Yes':
        club=1
    else:
        club=0
    
    if school=='Yes':
        school=1
    else:
        school=0
    
    if security=='Yes':
        security=1
    else:
        security=0
    
    if power=='Yes':
        power=1
    else:
        power=0
    
    if car=='Yes':
        car=1
    else:
        car=0
    
    if staff=='Yes':
        staff=1
    else:
        staff=0
    
    if cafe=='Yes':
        cafe=1
    else:
        cafe=0
    
    if mproom=='Yes':
        mproom=1
    else:
        mproom=0
    
    if hospital=='Yes':
        hospital=1
    else:
        hospital=0
    
    if washingmachine=='Yes':
        washingmachine=1
    else:
        washingmachine=0
    
    if gas=='Yes':
        gas=1
    else:
        gas=0
    
    if ac=='Yes':
        ac=1
    else:
        ac=0
    
    if childrenplayarea=='Yes':
        childrenplayarea=1
    else:
        childrenplayarea=0
    
    if lift=='Yes':
        lift=1
    else:
        lift=0
    
    if bed=='Yes':
        bed=1
    else:
        bed=0
    
    if vaastu=='Yes':
        vaastu=1
    else:
        vaastu=0
    
    if microwave=='Yes':
        microwave=1
    else:
        microwave=0
    
    if golf=='Yes':
        golf=1
    else:
        golf=0
    
    if tv=='Yes':
        tv=1
    else:
        tv=0
    
    if diningtable=='Yes':
        diningtable=1
    else:
        diningtable=0
    
    if sofa=='Yes':
        sofa=1
    else:
        sofa=0
    
    if fridge=='Yes':
        fridge=1
    else:
        fridge=0


    print(area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge)
    datasample=[[area,location,noofbedrooms,resale,maintenancestaff,gym,sp,gardens,jog,rainwater,indoorgames,mall,intercom,sports,atm,club,school,security,power,car,staff,cafe,mproom,hospital,washingmachine,gas,ac,childrenplayarea,lift,bed,vaastu,microwave,golf,tv,diningtable,sofa,fridge]]
    
    result=blr.predict(datasample)
    return render_template('index.html',dashboard_data1=locations,result=result[0],len1=len(locations))



if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)