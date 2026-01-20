#pragma once
#include <string>

// Handlers implementation */
namespace Handlers {
inline std::string ping() {
    return "PONG";
}

inline std::string status() {
    return "STATUS:OK";
}

}
