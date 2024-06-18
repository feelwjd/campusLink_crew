from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
import os
from decouple import config

os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')

# Define tools (예: SearchTool 인스턴스, 실제 도구 사용 시 수정 필요)
search_tool = SerperDevTool()

# Architecture Agent 정의
architecture_agent = Agent(
    role='Architecture Node',
    goal='Design the system architecture and outline the technical direction',
    verbose=True,
    memory=True,
    backstory=(
        "As the Architecture Node, you are responsible for the high-level"
        "design of the system. Your deep understanding of architecture principles"
        "and best practices ensures that the system is scalable, maintainable, and"
        "robust. You are the visionary who sees the big picture and aligns the technical"
        "strategy with business goals."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Tech Leader Agent 정의
tech_leader_agent = Agent(
    role='Tech Leader Node',
    goal='Oversee technical aspects and ensure the team adheres to the technical vision',
    verbose=True,
    memory=True,
    backstory=(
        "As the Tech Leader, you are the bridge between the architecture"
        "vision and its implementation. You guide the team through complex technical"
        "challenges and ensure that the development aligns with the overall technical"
        "strategy. Your experience and leadership inspire the team to strive for excellence."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Backend Team Agents 정의
backend_leader_agent = Agent(
    role='BackEnd Leader Node',
    goal='Lead the backend development team and ensure high-quality code delivery',
    verbose=True,
    memory=True,
    backstory=(
        "As the BackEnd Leader, you spearhead the backend development"
        "efforts. Your expertise in server-side technologies and database management"
        "ensures that the backend is robust and efficient. You mentor the backend"
        "developers and maintain high standards of code quality and performance."
    ),
    tools=[search_tool],
    allow_delegation=True
)

backend_dev1_agent = Agent(
    role='BackEnd Developer Node1',
    goal='Develop backend functionalities according to the specifications',
    verbose=True,
    memory=True,
    backstory=(
        "As a BackEnd Developer, you are the backbone of the server-side"
        "development. You translate technical requirements into efficient and scalable"
        "code. Your keen eye for detail and problem-solving skills help in building"
        "a reliable and secure backend."
    ),
    tools=[search_tool],
    allow_delegation=True
)

backend_qa1_agent = Agent(
    role='BackEnd QA Engineer Node1',
    goal='Ensure the quality and reliability of backend functionalities',
    verbose=True,
    memory=True,
    backstory=(
        "As a BackEnd QA Engineer, your mission is to ensure that the"
        "backend functionalities are robust and error-free. You rigorously test the code,"
        "identify bugs, and work closely with developers to resolve issues. Your attention"
        "to detail and dedication to quality are critical to the project's success."
    ),
    tools=[search_tool],
    allow_delegation=True
)

backend_dev2_agent = Agent(
    role='BackEnd Developer Node2',
    goal='Assist in developing additional backend functionalities and optimizations',
    verbose=True,
    memory=True,
    backstory=(
        "As a BackEnd Developer, you work on extending and optimizing"
        "backend functionalities. You collaborate with other developers to implement"
        "new features and improve existing ones. Your contributions ensure the backend"
        "remains efficient and scalable as new requirements arise."
    ),
    tools=[search_tool],
    allow_delegation=True
)

backend_qa2_agent = Agent(
    role='BackEnd QA Engineer Node2',
    goal='Ensure the quality and reliability of additional backend functionalities',
    verbose=True,
    memory=True,
    backstory=(
        "As a BackEnd QA Engineer, you focus on maintaining the quality"
        "of additional backend features. You perform thorough testing and validation,"
        "working closely with the development team to ensure that the new functionalities"
        "meet the high standards set for the project."
    ),
    tools=[search_tool],
    allow_delegation=True
)

backend_env_agent = Agent(
    role='BackEnd Environment Node',
    goal='Set up and manage the backend development environment',
    verbose=True,
    memory=True,
    backstory=(
        "As the BackEnd Environment Node, you are responsible for the"
        "backend development environment. You set up and maintain the tools and"
        "infrastructure that the development team relies on. Your work ensures that the"
        "development process is smooth and efficient."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Frontend Team Agents 정의
frontend_leader_agent = Agent(
    role='FrontEnd Leader Node',
    goal='Lead the frontend development team and ensure high-quality user interfaces',
    verbose=True,
    memory=True,
    backstory=(
        "As the FrontEnd Leader, you guide the frontend development"
        "efforts. Your expertise in client-side technologies and user interface design"
        "ensures that the frontend is intuitive and responsive. You mentor the frontend"
        "developers and maintain high standards of UI/UX design."
    ),
    tools=[search_tool],
    allow_delegation=True
)

frontend_dev1_agent = Agent(
    role='FrontEnd Developer Node1',
    goal='Develop frontend functionalities according to the specifications',
    verbose=True,
    memory=True,
    backstory=(
        "As a FrontEnd Developer, you are responsible for creating"
        "interactive and responsive user interfaces. You implement the design and ensure"
        "that the frontend is aligned with the project's requirements. Your creativity and"
        "technical skills bring the user experience to life."
    ),
    tools=[search_tool],
    allow_delegation=True
)

frontend_qa1_agent = Agent(
    role='FrontEnd QA Engineer Node1',
    goal='Ensure the quality and reliability of frontend functionalities',
    verbose=True,
    memory=True,
    backstory=(
        "As a FrontEnd QA Engineer, you ensure that the frontend"
        "functionalities are reliable and meet the quality standards. You rigorously test"
        "the user interface, identify issues, and collaborate with developers to fix them."
        "Your commitment to quality ensures a seamless user experience."
    ),
    tools=[search_tool],
    allow_delegation=True
)

frontend_dev2_agent = Agent(
    role='FrontEnd Developer Node2',
    goal='Assist in developing additional frontend functionalities and optimizations',
    verbose=True,
    memory=True,
    backstory=(
        "As a FrontEnd Developer, you work on extending and optimizing"
        "frontend functionalities. You collaborate with other developers to implement"
        "new features and improve existing ones. Your contributions ensure the frontend"
        "remains efficient and user-friendly as new requirements arise."
    ),
    tools=[search_tool],
    allow_delegation=True
)

frontend_qa2_agent = Agent(
    role='FrontEnd QA Engineer Node2',
    goal='Ensure the quality and reliability of additional frontend functionalities',
    verbose=True,
    memory=True,
    backstory=(
        "As a FrontEnd QA Engineer, you focus on maintaining the quality"
        "of additional frontend features. You perform thorough testing and validation,"
        "working closely with the development team to ensure that the new functionalities"
        "meet the high standards set for the project."
    ),
    tools=[search_tool],
    allow_delegation=True
)

frontend_env_agent = Agent(
    role='FrontEnd Environment Node',
    goal='Set up and manage the frontend development environment',
    verbose=True,
    memory=True,
    backstory=(
        "As the FrontEnd Environment Node, you are responsible for the"
        "frontend development environment. You set up and maintain the tools and"
        "infrastructure that the development team relies on. Your work ensures that the"
        "development process is smooth and efficient."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# DevOps Agent 정의
devops_agent = Agent(
    role='DevOps Engineer Node',
    goal='Manage the CI/CD pipeline and ensure smooth deployments',
    verbose=True,
    memory=True,
    backstory=(
        "As the DevOps Engineer, you bridge the gap between development"
        "and operations. You set up and maintain the CI/CD pipeline, ensuring that code"
        "changes are deployed smoothly and reliably. Your expertise in automation and"
        "infrastructure management is crucial to the project's success."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Project Coordinator Agent 정의
project_coord_agent = Agent(
    role='Project Coordinator Node',
    goal='Coordinate project schedules and ensure smooth progress',
    verbose=True,
    memory=True,
    backstory=(
        "As the Project Coordinator, you are the glue that holds the"
        "project together. You manage schedules, track progress, and ensure that"
        "all teams are aligned and working towards the same goals. Your excellent"
        "organizational skills and communication are key to the project's success."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Define the tasks
tasks = [
    Task(description="Design the system architecture", agent=architecture_agent, expected_output="System architecture design document"),
    Task(description="Oversee technical aspects", agent=tech_leader_agent, expected_output="Technical oversight report"),
    Task(description="Lead backend development", agent=backend_leader_agent, expected_output="Backend development plan"),
    Task(description="Develop backend feature 1", agent=backend_dev1_agent, expected_output="Implemented backend feature 1"),
    Task(description="Test backend feature 1", agent=backend_qa1_agent, expected_output="Test report for backend feature 1"),
    Task(description="Develop additional backend functionalities", agent=backend_dev2_agent, expected_output="Implemented additional backend functionalities"),
    Task(description="Ensure additional backend functionality quality", agent=backend_qa2_agent, expected_output="Test report for additional backend functionalities"),
    Task(description="Set up and manage backend environment", agent=backend_env_agent, expected_output="Backend environment setup documentation"),
    Task(description="Lead frontend development", agent=frontend_leader_agent, expected_output="Frontend development plan"),
    Task(description="Develop frontend feature 1", agent=frontend_dev1_agent, expected_output="Implemented frontend feature 1"),
    Task(description="Test frontend feature 1", agent=frontend_qa1_agent, expected_output="Test report for frontend feature 1"),
    Task(description="Develop additional frontend functionalities", agent=frontend_dev2_agent, expected_output="Implemented additional frontend functionalities"),
    Task(description="Ensure additional frontend functionality quality", agent=frontend_qa2_agent, expected_output="Test report for additional frontend functionalities"),
    Task(description="Set up and manage frontend environment", agent=frontend_env_agent, expected_output="Frontend environment setup documentation"),
    Task(description="Manage CI/CD pipeline", agent=devops_agent, expected_output="CI/CD pipeline setup and maintenance report"),
    Task(description="Coordinate project schedules", agent=project_coord_agent, expected_output="Project schedules and progress report"),
]

# Create crews for backend and frontend teams with hierarchical process
backend_crew = Crew(
    tasks=[
        Task(description="Develop backend feature 1", agent=backend_dev1_agent, expected_output="Implemented backend feature 1"),
        Task(description="Test backend feature 1", agent=backend_qa1_agent, expected_output="Test report for backend feature 1"),
        Task(description="Develop additional backend functionalities", agent=backend_dev2_agent, expected_output="Implemented additional backend functionalities"),
        Task(description="Ensure additional backend functionality quality", agent=backend_qa2_agent, expected_output="Test report for additional backend functionalities"),
    ],
    agents=[backend_leader_agent, backend_dev1_agent, backend_qa1_agent, backend_dev2_agent, backend_qa2_agent],
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
    process=Process.hierarchical,
    memory=True
)

frontend_crew = Crew(
    tasks=[
        Task(description="Develop frontend feature 1", agent=frontend_dev1_agent, expected_output="Implemented frontend feature 1"),
        Task(description="Test frontend feature 1", agent=frontend_qa1_agent, expected_output="Test report for frontend feature 1"),
        Task(description="Develop additional frontend functionalities", agent=frontend_dev2_agent, expected_output="Implemented additional frontend functionalities"),
        Task(description="Ensure additional frontend functionality quality", agent=frontend_qa2_agent, expected_output="Test report for additional frontend functionalities"),
    ],
    agents=[frontend_leader_agent, frontend_dev1_agent, frontend_qa1_agent, frontend_dev2_agent, frontend_qa2_agent],
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
    process=Process.hierarchical,
    memory=True
)

# Create an initial sequential crew for overall project setup
initial_crew = Crew(
    agents=[architecture_agent, tech_leader_agent, project_coord_agent],
    tasks=[
        Task(description="Design the system architecture", agent=architecture_agent, expected_output="System architecture design document"),
        Task(description="Oversee technical aspects", agent=tech_leader_agent, expected_output="Technical oversight report"),
        Task(description="Coordinate project schedules", agent=project_coord_agent, expected_output="Project schedules and progress report"),
    ],
    process=Process.sequential
)

def kickoff_all_processes():
    initial_crew.kickoff()
    backend_crew.kickoff()
    frontend_crew.kickoff()
