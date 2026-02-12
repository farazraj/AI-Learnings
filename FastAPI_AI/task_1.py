def tsk1(name: str, age: int, skills: list[str]) -> dict:
    return {
        "name": name,
        "age": age,
        "skills": skills
    }

print(tsk1('Raj', 28, ['coding', 'ai']))
