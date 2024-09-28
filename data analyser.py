class TeamMember:
    def _init_(self, name, communication_score, task_contribution, role_clarity, satisfaction, conflict_resolution):
        self.name = name
        self.communication_score = communication_score  # 1 to 10 scale
        self.task_contribution = task_contribution      # 1 to 10 scale
        self.role_clarity = role_clarity                # 1 to 10 scale
        self.satisfaction = satisfaction                # 1 to 10 scale
        self.conflict_resolution = conflict_resolution  # 1 to 10 scale

    def overall_score(self):
        """Calculates the average score for the team member"""
        return (self.communication_score + self.task_contribution + 
                self.role_clarity + self.satisfaction + 
                self.conflict_resolution) / 5

class TeamDynamicsAnalyzer:
    def _init_(self):
        self.team_members = []

    def add_team_member(self, member):
        self.team_members.append(member)

    def average_team_score(self):
        """Calculates the overall average score of the team"""
        total_score = sum([member.overall_score() for member in self.team_members])
        return total_score / len(self.team_members) if self.team_members else 0

    def communication_effectiveness(self):
        """Calculates the average communication score of the team"""
        total_communication = sum([member.communication_score for member in self.team_members])
        return total_communication / len(self.team_members) if self.team_members else 0

    def task_distribution(self):
        """Calculates the average task contribution score of the team"""
        total_contribution = sum([member.task_contribution for member in self.team_members])
        return total_contribution / len(self.team_members) if self.team_members else 0

    def display_report(self):
        """Displays a basic team dynamics report"""
        print("\nTeam Dynamics Report")
        print("--------------------")
        print(f"Average Team Score: {self.average_team_score():.2f}")
        print(f"Communication Effectiveness: {self.communication_effectiveness():.2f}")
        print(f"Task Distribution: {self.task_distribution():.2f}")
        print("\nIndividual Member Scores:")
        for member in self.team_members:
            print(f"{member.name}: {member.overall_score():.2f}")

# Example usage
if _name_ == "_main_":
    # Create an instance of TeamDynamicsAnalyzer
    analyzer = TeamDynamicsAnalyzer()

    # Add team members (name, communication, task contribution, role clarity, satisfaction, conflict resolution)
    member1 = TeamMember("Alice", 8, 9, 8, 7, 8)
    member2 = TeamMember("Bob", 7, 8, 7, 9, 6)
    member3 = TeamMember("Charlie", 9, 7, 8, 6, 7)

    # Add members to the analyzer
    analyzer.add_team_member(member1)
    analyzer.add_team_member(member2)
    analyzer.add_team_member(member3)

    # Display team dynamics report
    analyzer.display_report()
