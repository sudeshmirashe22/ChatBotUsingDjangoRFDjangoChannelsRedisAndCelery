custom_data = {
    "do you sell dog food?": "Yes, we have a wide variety of dog food available online and in-store.",
    "what brands of cat food do you have?": "We carry brands like Whiskas, Me-O, and Royal Canin.",
    "do you have toys for puppies?": "Yes, we have chew toys, squeaky toys, and more for puppies.",
    "what are your store hours?": "Our store is open from 9 AM to 9 PM, Monday to Saturday.",
    "are you open on sundays?": "Yes, we are open on Sundays from 10 AM to 6 PM.",
    "do you deliver pet food?": "Yes, we offer same-day delivery within city limits.",
    "what payment methods do you accept?": "We accept UPI, credit/debit cards, and cash on delivery.",
    "do you offer grooming services?": "Yes, we offer grooming by appointment. Please call to book.",
    "how can i track my order?": "You can track your order through the 'My Orders' section in your account.",
    "what is your return policy?": "Returns are accepted within 7 days for unopened products with receipt.",
    "where is your store located?": "We are located at XYZ Road, Pet Nagar, Mumbai.",
    "how can i contact support?": "You can call us at 9876543210 or email us at support@petshop.com.",
}

def get_answer(user_input: str) -> str:
    return custom_data.get(user_input.lower(), None)