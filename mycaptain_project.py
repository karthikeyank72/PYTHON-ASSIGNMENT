#Basic school Administration tool
import csv
def write_into_csv(info_list):
    with open("student_info.csv","a", newline="") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact number","Email-ID"])
        writer.writerow(info_list)



if __name__=="__main__"
    condition=True
    student_num=1
    while (condition):
        student_info =input("Enter student information for student #{} in the following format(Name Age Contact_number Email_ID):".format(student_num))
        print("Entered information"+student_info)

        #split
        student_info_list=student_info.split(' ')
        print("Entered splitup information is:",student_info_list)
        print("\n The entered information is- \nName:{} \nAge:{} \nContact Number:{} \nEmail-ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the entered information correct?:")

        if choice_check=="yes":
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no) if you enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num =+1
            else:
                condition = False
        else:
            print("\n Please re-enter the values!")


