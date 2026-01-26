import inspect
import TamaraSamokhvalova_ProgrammingExercise_1 # replace with your assignment name (without .py)

#replace docstring_example with your assignment name in the next 2 lines of code
with open("TamaraSamokhvalova_ProgrammingExercise_1_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {TamaraSamokhvalova_ProgrammingExercise_1.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Tamara Samokhvalova\n")
    doc.write(f"# Date: January 24, 2025\n")
    doc.write(f"# Program Description: The program sells a limited number of cinema tickets, "
          f"allowing each buyer to purchase up to 4 tickets. It tracks the remaining "
          f"tickets and counts the total number of buyers until all tickets are sold.\n\n")
    #replace docstring_example with your assignment name
    for name, func in inspect.getmembers(TamaraSamokhvalova_ProgrammingExercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
        #replace with link to your repository
        doc.write(f"#Link to your repository: https://github.com/tamara240906/COP2373 tab=repositories")
print('Complete')