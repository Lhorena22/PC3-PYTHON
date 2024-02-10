from funciones import alumno

def main():
    alumno_1 = alumno("Carlos", "1002")
    alumno_1.setAge(18)
    alumno_1.setNota([18, 20, 16, 15])
    alumno_1.Display()
pass

if __name__ == "__main__":
    main()