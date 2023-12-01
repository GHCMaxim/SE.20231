from fastapi import FastAPI

from . import routes

app = FastAPI()

app.include_router(routes.household_registrations.household_registrations)
app.include_router(routes.payments.payments)
app.include_router(routes.people.people)
app.include_router(routes.rewards.rewards)
app.include_router(routes.users.users)
