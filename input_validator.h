#include <stdexcept>
#include <string>
#include <cctype>
#include <cstddef>

class InputValidator{

    // making a private constant for MAX_COMMAND_LENGTH
    // in C++ we will always declare our private methods before public which we will use to call
    private:
    static constexpr std::size_t MAX_COMMAND_LENGTH = 50;
    //basically not null but remember in c++ we must not use not null as its not a function instead we will use detect whitespace or trailing whitespace early to mimic.

    void validateNotEmptyOrWhitespace(const std::string& s) const {
        // Assume the string contains only whitespace until proven otherwise

        bool allWhiteSpaces = true;
        // Iterate through each character in the string
        // Use unsigned char to avoid undefined behaviour with std::isspace

        for(unsigned char ch : s){

             // If any character is not whitespace, the string is not whitespace-only
            if (!std::isspace(ch)){
                allWhiteSpaces = false;
                break;
            }
        }
        // Reject the input if it is empty or consists only of whitespace
        if (s.empty() || allWhiteSpaces) {
            throw std:: invalid_argument("Command cannot be empty");
        }

    }

    std:: string trim(const std::string& s) const {
        // Index of the first non-whitespace character from the start
        std::size_t start = 0;
        // Move start forward while leading whitespace is found
        while (start < s.size() && std::isspace(static_cast <unsigned char>(s[start]))){
            start++;
        }


    // Index one past the last non-whitespace character
    std::size_t end = s.size();
    // Move end backward while trailing whitespace is found
    while (end > start &&  std::isspace(static_cast <unsigned char> (s[end - 1]))){
        end --;
    }
     // Extract the substring containing only non-whitespace characters
    std::string trimmed = s.substr(start, end - start);
    // If trimming results in an empty string, reject the input
    if (trimmed.empty()) {
        throw std:: invalid_argument(" Command must not be empty");
    }
     // Return the normalized (trimmed) string
    return trimmed;

    }

    void validateLengthOfString(const std::string& s) const {
        if (s.size() > MAX_COMMAND_LENGTH) {
            throw std:: invalid_argument("Command is too long must be within 50 characters.");
        }

    }

    void validateCharactersAreValid(const std::string& s) const {

        for (unsigned char ch : s) {
            if (!(std:: isupper(ch) || std:: isdigit(ch))){
                throw std:: invalid_argument("character is invalid or not supported can only be a capital or number");
            }
        }

    }


    public:
    std:: string validateCommand(const std::string& command)   const {
        validateNotEmptyOrWhitespace(command);
        std:: string normalized = trim(command);
        validateLengthOfString(normalized);
        validateCharactersAreValid(normalized);


        return normalized;



    }


};