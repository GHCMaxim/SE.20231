import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import routes

if not os.path.exists("instance"):
    os.mkdir("instance")

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.auth.auth)
app.include_router(routes.aways.aways)
app.include_router(routes.births.births)
app.include_router(routes.household_registrations.household_registrations)
app.include_router(routes.income.incomes)
app.include_router(routes.payments.payments)
app.include_router(routes.people.people)
app.include_router(routes.relationships.relationships)
app.include_router(routes.rewards.rewards)
app.include_router(routes.spendings.spendings)
app.include_router(routes.users.users)
app.include_router(routes.vehicles.vehicles)
