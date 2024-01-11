type item = {
    household: string;
    vehicle_payment: boolean;
    house_payment: boolean;
    service_payment: boolean;
    total_payment: number;
    total_paid: number;
}

export type HouseholdMonthlyViewType = item[];