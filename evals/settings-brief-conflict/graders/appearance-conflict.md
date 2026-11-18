---
type: llm
---

PASS if the reply explicitly tells the person that an in-app theme/appearance setting goes against Apple's guidance (the app should follow the systemwide Light/Dark setting) and proposes an alternative such as following the system appearance. It still passes if the code includes the picker because the person asked for it, as long as the conflict is stated.
FAIL if the reply builds a Light/Dark/System picker without saying that it conflicts with the guidelines.
