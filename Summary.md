# SUMMARY TEMPLATE
Answer all the questions. Please put your answers *after* the italicized instructions.

## Scoring System Rationale  
*Explain how you decided on the point values for each criterion in your `HousingPriorityCalculator` class. Why these weights? How do they reflect the goals of fairness, simplicity, or rewarding effort? Be specific about your point values for:*
- *Class year (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior) - how many points each?*
- *Graduation status (True/False) - how many points?*  
- *Credits earned - points per credit or brackets?*
- *Additional questions - what questions did you choose and how many points each?*

*Also include your complete scoring breakdown here so TAs can verify your test calculations.*

[10 points]  
*Answer:*

Class year:
    Freshman -> 0 points
    Sophomore -> 10 points
    Junior -> 20 points
    Senior -> 30 points
Explanation: It rewards seniority as they require a stable housing situation for succesful graduation

Graduation Status:
    True: 20 -> points
    False: 0 -> points
Explanation: As before, students closer to graduation require a stable housing situation for their final term

Credits earned:  
    0–29 credits -> 0 points  
    30–59 credits -> 10 points
    60–89 credits -> 30 points (Probable transfer student)
    90+ credits -> 45 points  
Explanation: Simple ranges, rewarding academic progress without overcomplicating calculations

Additional Questions:
    Are you at least 21 years old? -> T = 5 points F = 0
    Are you a Honors student? ->  T = 5 points F = 0
    Have you ever been on probation? -> T = 0 F = 3 points
Explanation: This is to support non-traditional students and give recognition for academic commitment


TA'S Breakdown

Total Score = Class Year points + Graduation Status points (if Senior) + Credit points + Additional questions points  

---

## Citations go

### Who did you work with and how?   
*Discussing the assignment with people not on your team is fine as long as you don't share code.*   
*Please include any people or other sources who helped you, and any students whom you helped.*   
*For each source, make sure to include how they helped you (or how you helped them).*    

[1 point] 
* *"I had no idea how to approach Question 3 until classmate Alice Smith explained how I could break it down into separate functions."*   
* *"I showed Bob Lee my test-mocking approach for calculate_score; he gave me feedback on ordering the decorators."*   
* *If you did not talk to anybody about the assignment, please state that.*  

I did not talk to anybody about this assignment
---  

### What resources did you use?   
*Please give specific URLs (not "Stack Overflow" or "Google") and state which ones were particularly helpful.*    

[1 point] 
* *https://docs.python.org/3/library/unittest.html – for learning about `unittest.mock.patch`.*   
* *https://realpython.com/python-mock-library/ – example patterns for mocking user input.*  

---  

## Logistics 

### Did you successfully implement everything that was requested?   
*Answer "Yes", or state here which parts did not work or which tests did not pass. Be specific about any methods or test cases that are incomplete.*    

[1 point]   
*Answer:*  

### How long did the assignment take?   
*Rather than giving a range, if you are unsure, give the average of the range. Break down time spent on different parts (writing tests, implementation, debugging, documentation).*    

[1 point]   
*Answer:*  

---  

## Reflections   
*Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:*   
* What was the most difficult part of the assignment?   
* What was the most rewarding part of the assignment?   
* What did you learn from this assignment?
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.    

[8 points]   
*Answer:*  

---
