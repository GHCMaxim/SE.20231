type item = {
	name: string;
	id: number;
	type_id: number;
	creation_date: string;
	expiration_date: string;
	price: number;
	household: string;
	income_id: number;
	paid: boolean;
};

export type PaymentByHouseholdType = item[];
