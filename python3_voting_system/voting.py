nominee1 = input("Enter the 1st noinee name:")
nominee2 = input("Enter the 2nd noinee name:")

nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
        if voter_id == []:
            print("Voting session ended...!!")
            if nm1_votes > nm2_votes:
                percent = (nm1_votes/no_of_voter)*100
                print("----------------------------------")
                print(nominee1,"has won the election with", percent,"%")
                break
            elif nm2_votes > nm1_votes:
                percent = (nm2_votes/no_of_voter)*100
                print("----------------------------------")
                print(nominee2,"has won the election with", percent,"%")
                break
            else:
                print("Both candidates have equal number of votes...GOVERNMENT WILL DECIDE WHO WILL BE IN POWER")
                break
            
        voter = int(input("Enter your voter id:"))
        if voter in voter_id:
         print("You are a voter")
         voter_id.remove(voter)
         print("----------------------------------")
         print("To give vote ", nominee1, "Press 1")
         print("To give vote ", nominee2, "Press 2")
         print("----------------------------------")
         vote = int(input("Enter your previous vote:"))
         if vote == 1:
            nm1_votes +=1
            print(nominee1, "Thank you to give your important vote to them")
         elif vote ==2:
            nm2_votes +=1
            print(nominee2, "Thank you to give your important vote to them")
         elif vote > 2:
            print("Check your pressed key!!!")
         else :
            print("You are not a valid voter OR You have already voted")    
        
        
        