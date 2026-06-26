class TrainersDepartment:
    def conduct_training(self):
        print("Conducting Python training session.")

    def evaluate_students(self):
        print("Evaluating student performance.")


class SalesDepartment:
    def generate_leads(self):
        print("Generating new leads.")

    def close_deals(self):
        print("Closing sales deals.")


class HrDepartment:
    def recruit_employees(self):
        print("Recruiting new employees.")

    def manage_attendance(self):
        print("Managing employee attendance.")


class MarketingDepartment:
    def create_campaign(self):
        print("Creating marketing campaign.")

    def analyze_market(self):
        print("Analyzing market trends.")


# Creating objects
trainers_dept = TrainersDepartment()
sales_dept = SalesDepartment()
hr_dept = HrDepartment()
marketing_dept = MarketingDepartment()

# Calling methods
trainers_dept.conduct_training()
trainers_dept.evaluate_students()

sales_dept.generate_leads()
sales_dept.close_deals()

hr_dept.recruit_employees()
hr_dept.manage_attendance()

marketing_dept.create_campaign()
marketing_dept.analyze_market()