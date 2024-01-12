import {defineRule} from 'vee-validate';
import {required, email, min, max, confirmed} from '@vee-validate/rules';


defineRule('required', required);
defineRule('email', email);
defineRule('min', min);
defineRule('max', max);
defineRule('confirmed', confirmed);
defineRule('date_format' , (value : string) => {
    return value.match(/^\d{4}-\d{2}-\d{2}$/) ? true : 'Invalid date format';
})

export const rules = {
    required,
    email,
    min,
    max,
    confirmed,
    date_format: (value : string) => {
        return value.match(/^\d{4}-\d{2}-\d{2}$/) ? true : 'Invalid date format';
    }
};