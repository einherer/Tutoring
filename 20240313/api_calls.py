import requests


def call_cat_facts():
    url = "https://cat-fact.herokuapp.com"

    facts = "/facts"

    response = requests.get(url + facts)
    data = response.json()
    # print(data)
    for entry in data:
        print(f"- {entry['text']}")


# call_cat_facts()


def call_rand_facts(type="cat"):
    url = "https://cat-fact.herokuapp.com"

    facts = f"/facts/random/?animal_type={type}"

    response = requests.get(url + facts)
    if not response.ok:
        print("something went wrong")
        return

    if not response.content:
        print(f"No fact for {type}")
        return

    data = response.json()
    print(f"Fact about {data['type']}: {data['text']}")


call_rand_facts()
call_rand_facts("dog")
call_rand_facts("horse")
call_rand_facts("snail")
call_rand_facts("snake")
