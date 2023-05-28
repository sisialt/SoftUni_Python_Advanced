class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MustContainDotSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain '@'.")

    name = email[:email.index("@")]

    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters.")

    if len(name) > 30:
        raise NameTooLongError("Name must be less than 30 characters.")

    check_valid_name = [ch for ch in name if ch.isdigit() or ch.isalpha() or ch == "_"]

    if name != "".join(check_valid_name):
        raise InvalidNameError("Name can contain only letters, digits and underscores.")

    if "." not in email:
        raise MustContainDotSymbolError("Email must contain '.'.")

    domain = email[email.index("."):]

    if domain not in [".com", ".bg", ".org", ".net"]:
        raise InvalidDomainError("Domain must be one of the following: '.com', '.bg', '.org', '.net'.")

    print("Email is valid. :)")

# abc@abv.bg
#
# hfbveubviwncoincosndcbvuibriuivsndcsncsebvubvriu@abv.bg
#
# petergmail.com
#
# peter@gmailde
#
# peter@gmail.hotmail
#
# peter#@abv.bg
