def chat_bot():

    print("\n")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ")
    print("||                                                                                                                        || ")
    print("||   /////////     ///       ///         /////        ||||||||||||||||     ///////////   ////////////  ||||||||||||||||   || ")
    print("||   /////////     ///       ///        ///////             ///            ///     ///   ////////////        ///          || ")
    print("||   ///           ///       ///       ///   ///            ///            ///     ///   ///      ///        ///          || ")
    print("||   ///           /// ///// ///      ///     ///           ///            ///////////   ///      ///        ///          || ")
    print("||   ///           ///       ///     /////////////          ///            ///     ///   ///      ///        ///          || ")
    print("||   /////////     ///       ///    ///         ///         ///            ///     ///   ////////////        ///          || ")
    print("||   /////////     ///       ///   ///           ///        ///            ///////////   ////////////        ///          || ")
    print("||                                                                                                                        || ")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

    st_ty = input("Enter 'Start' TO Run Program : ")

    if st_ty == "Start":
        print("ok.........................")
    else:
        print("\nDont Worry 'I Know Your English'.\n")
        print("Just Kidding 😁\n")

    
    while True:

        print("\nHello 👋 Welcome to Bhavesh's Support Assistant.\nPlease choose an option below:\n")

        print("1 : Order Support")
        print("2 : Account Help")
        print("3 : Payment & Refunds")
        print("4 : Product Information")
        print("5 : Subscription Services")
        print("6 : Speak to Human Agent")
        print("7 : Exit\n")
        
        user_input = int(input("Enter Your Option : "))

        while True:


            ###### for ordr support


                if user_input == 1:

                    print("1. Track My Order")
                    print("2. Cancel Order")
                    print("3. Return Product")
                    print("4. Delivery Issue")
                    print("5. Back to Main Menu\n")

                    user_order_input = int(input("Enter Your Option : "))

                    ##### track order

                    if user_order_input == 1:

                        order_id = input("Enter Your Order ID : ")

                        print("BOT :")
                        print("Your Order Is Out of Delivery !")

                    #### cancel order

                    elif user_order_input == 2:

                        order_id = input("Enter Your Order ID : ")

                        print("Resone :")
                        print("1 : Wrong Item select")
                        print("2 : Mistakly Plased")
                        print("3 : Other")

                        user_respones = int(input("Enter Your Option : "))

                        if user_respones == 1 :
                            print("BOT :")
                            print("Your Order 'CANCEL' successful !")

                        elif user_respones == 2 :
                            print("BOT :")
                            print("Your Order 'CANCEL' successful !")

                        elif user_respones == 3:
                            print("BOT :")
                            user_respones_for_other = input("Enter Your Resone : ")
                            print("Your Order 'CANCEL' successful !")
                        else:
                            print("Enter Valid Option")

                    #### return product

                    elif user_order_input == 3:

                        order_id = input("Enter Your Order ID : ")

                        print("Resone :")
                        print("1 : Wrong Item Deliver")
                        print("2 : Faulty item")
                        print("3 : Order Not Deliver")

                        user_respones = int(input("Enter Your Option : "))

                        if user_respones == 1:
                            print("BOT :")
                            print("Shedule Your Delivery")

                        elif user_respones == 2:
                            print("BOT :")
                            print("Shedule Your Delivery")

                        elif user_respones == 3:
                            print("BOT :")
                            print("Contact our Agent Dial : 1234-1234-1234")

                        else:
                            print("Enter Valid Option")


                    #### Delivery Issue

                    elif user_order_input == 4:

                        order_id = input("Enter Your Order ID : ")

                        print("1 : Order Not Deliver")
                        print("2 : Wrong Address")

                        user_respone = int(input("Enter Your Option : "))

                        if user_respone == 1:
                            print("BOT :")
                            print("Contact our Agent Dial : 1234-1234-1234")

                        elif user_respone == 2:
                            print("BOT :")
                            new_address = input("Enter Updated Address : ")
                            print("Your Address Sucessful !")
                        
                        else:
                            print("Enter Valid Option")

                    #### back to menu

                    elif user_order_input == 5:

                        break

                    else:
                        print("Enter Valid Option")


            ###### Account Help

                elif user_input == 2:

                    print("\n1: Reset Password")
                    print("2: Change Email")
                    print("3: Update Mobile Number")
                    print("4: Delete Account")
                    print("5: Back To Main Menu\n")

                    User_Account_input = int(input("Enter Your Option : "))

                    if User_Account_input == 1:
                        
                        print("\nBOT : Enter Details \n")

                        mobile_no = int(input("Enter Your Mobile Number : \n"))
                        old_pass = input("Enter Your Old Password : \n")
                        print("Verifying......\n")
                        print("Verify Sucessful ....!\n ")
                        new_pass = input("Enter Your New Password : \n")
                        print("Password Update Sucessful...!\n")

                    elif User_Account_input == 2:

                        print("BOT :\n")
                        input("Enter Your Email : ")
                        print("\nEmail Update Sucessfully...!\n")

                    elif User_Account_input == 3:

                        pwd = input("Enter Your Password : ")
                        new_num = int(input("Enter New Number : "))
                        print(f"Your Mobile Number {new_num} is Update Sucessful...")

                    elif User_Account_input == 4:

                        print("Are You SURE....\n")

                        statement = input("Enter 'DELETE MY ACCOUNT' For Procced... : ")

                        print("Deleting Account .....")

                        break

                    elif User_Account_input == 5:

                        break



            ###### Payment & Refunds
        
                elif user_input == 3:
    
                        print("\n1: Refund Status")
                        print("2: Payment Failed")
                        print("3: Download Invoice")
                        print("4: Back to Main Menu\n")
    
                        User_Payment_input = int(input("Enter Your Option : "))        
chat_bot()
