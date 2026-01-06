#pragma once
#include <string>

// Handlers implementation */
namespace Handlers {
inline std::string handlePing() {
    return "PONG";
}

inline std::string handleStatus() {
    return "STATUS_OK";
}

};
