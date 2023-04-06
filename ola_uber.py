print(' Welcome To Uber Service '.center(50,'◉')+'\n')
# ↆ⊱⊰⨝=◉◆
try:
    # log=logger()
    #-----------------------------available cars---------------------------------
    print('  CAR TYPES  '.center(50,'◉'))

    car = dict({'SR NO': [1, 2, 3], 'CAR': ['MINI', 'BIG', 'SEDAN'], 
                'CAPACITY': ['4', '3', '5'], 'RATE': ['Rs.20/km', 'Rs.25/km', 'Rs.50/km']})

    print('SR NO\t\tCAR\t\tCAPACITY\tRATE')
    
    for i in range(len(car['SR NO'])):
        for k, v in car.items():
            print(f'{v[i]}\t\t', end='')
        print()
    
    list_route = car.keys()
    print()

    #-----------------------------available routes---------------------------------

    print('  AVAILABLE ROUTES  '.center(50,'◉'))

    routes={'Pune-Mumbai': 150, 'Pune-Nashik': 200,'Nashik-Pune':200,'Mumbai-Pune':150}
    list_routes=routes.keys()
    
    for i in list_routes:
        print('\t⊱⫸ ',i)
    print()

    #-----------------------------routes details---------------------------------
    price={'MINI':20, 'BIG':25, 'SEDAN':50}

    source = (input('⊰ Enter Pic-Up Point:- ').capitalize())
    destination = (input('⊰ Enter Drop Point:- ').capitalize())
    car_type = (input('⊰ Enter Car Type:- ').upper())
    # (f'enter car type:- {car_type}')
    
    final = source+ '-' + destination
    if final in routes.keys():
        print(f'distance between {source} and {destination} = {routes[final]}km')
    #--------------------------calculation---------------------------------------
        if car_type in price.keys():
            print(f'\n\t◆ Fare For {car_type} = {price[car_type] } Rs/KM')
            total=price[car_type]*routes[final]
            print(f'\n\t◆ Fare For This Ride {total} ₹ (Exculding Taxex)')

            #--------------------------confirmation---------------------------------------
            print('  CONFIRMATION  '.center(50,'◉'))
            ride=input('\n\t◆ Do You Want To Book Ride? [Yes/No] : ')
            ride=ride.capitalize()

            if ride=='Yes':
                name=input('⊰ Enter Your Name :')
                mobile=int(input("⊰ Enter Your Contact Number : "))
                email=input("⊰ Enter Your Email ID : ")
                
                print("\n\t◆ Thanks For Booking Ride With Us")
                print("\n\t◆ Driver Will Come Soon To Your Pick-Up Point")
            else:
                
                print("\n\t◆ Thanks For Visiting Our Site")
            #------------------------------Ride Number---------------------------------
            import random
            ride_no=random.randint(0,10)
            #------------------------------Ride Time---------------------------------
            import datetime

            now = datetime.datetime.now()
            date=now.strftime("%d-%m-%Y %H:%M:%S")
            # -------------------------Total Fare Including Tax-----------------------------
            gst=total/100*9
            total_fare=total+gst+gst

            # ----------------------------Final Bill----------------------------------------
            from fpdf import FPDF
            from tabulate import tabulate
            
            if ride=='Yes':
                print('  FINAL BILL  '.center(50,'◉'))

                print(tabulate([['RIDE-NO',ride_no],['ROUTE',final],['CAR TYPE',car_type],['DISTANCE',routes[final]],
                                    ['PER KM',price[car_type]],['DIST*/KM',total],['NAME',name],['MOBLIE',mobile],['E-MAIL',email],
                                    ['FINAL BILL',total_fare]],tablefmt='fancy_grid'))
                
                bill=input('\n\t● Do You Want To Billing Invoice? [Yes/No] : ')
                bill=bill.upper()

                if ride=='Yes':
                
                    def bill_pdf():
                        pdf = FPDF()
                        pdf.set_font_size(16)
                        pdf.add_page()
                        pdf.write_html(f'''
                            <h1 align="center"><b>Billing Invoice</b></h1>
                            <p align="right">Date Of Ride</p>
                            <p align="right">{date}</p>
                            <p align="right">Ride No :{ride_no}</p>
                            <table width="100%" border="1">
                                
                                <tr>
                                <th width="50%">Passanger Name</th>
                                <th width="50%">{name}</th>
                                </tr>
                                <tr>
                                <th width="50%">Passanger Mobile No</th>
                                <th width="50%">{mobile}</th>
                                </tr>
                                <tr>
                                <th width="50%">Passanger E-Mail ID</th>
                                <th width="50%">{email}</th>
                                </tr>
                                <tr>
                                <th width="50%">ROUTE</th>
                                <th width="50%">{final}</th>
                                </tr>
                                <tr>
                                <th width="50%">Distance</th>
                                <th width="50%">{routes[final]}</th>
                                </tr>
                                <tr>
                                <th width="50%">Per KM</th>
                                <th width="50%">{price[car_type]}</th>
                                </tr>
                                <tr>
                                <th width="50%">Vehicle Type</th>
                                <th width="50%">{car_type}</th>
                                </tr>
                                <tr>
                                <th width="50%">CGST 9%</th>
                                <th width="50%">{gst} Rs</th>
                                </tr>
                                <tr>
                                <th width="50%">SGST 9%</th>
                                <th width="50%">{gst} Rs</th>
                                </tr>
                                <tr>
                                <th width="50%">Total Fare</th>
                                <th width="50%">{total_fare} Rs</th>
                                </tr>
                            </table>

                            '''
                        
                        )
                        pdf.output(f'{ride_no}.pdf')
                        print('pdf is created')

                    bill_pdf()
                    
                else:    
                      print('\n Please Contact On 9834761449')

            
            


                print('  THANK YOU!!  '.center(50,'◉'))



        else:
            print(f"\n\t◆ ◆ ◆ {car_type} Type Vehicle Is Not Available ◆ ◆ ◆" )
    else:
        print(f'\n\t◆ ◆ ◆ Please enter valid {source} and {destination} route ◆ ◆ ◆')
        print(f"\n\t◆ ◆ ◆ {car_type} Type Vehicle Is Not Available ◆ ◆ ◆" )

except BaseException as ex:
    print(ex)
