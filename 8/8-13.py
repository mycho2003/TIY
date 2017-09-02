def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

me = build_profile("Michael", "Cho", Location= "Seoul", School= "SIS", Floor= 17)
print(me)