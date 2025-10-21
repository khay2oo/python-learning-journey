username = "khay2oo"
total_attempts = 25
successful_logins = 20
security_score = 87.654
print(
    f"[SEVURITY REPORT] \
    \nUser:{username} \
        \nTotal Login Attempt:{total_attempts} \
            \nSeccussful Attempt:{successful_logins} ({successful_logins/total_attempts:.0%})\
                \nSecurity Posture: {security_score:.2f}/100")
