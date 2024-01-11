type item = {
    name : string;
    id : number;
    type_id : number;
    creation_date : string;
    price : number;
    household : string;
    income_id : number;
    paid : boolean;
}

export type EssentialsFeeViewType = item[];
