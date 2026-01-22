#pragma once
#include <string>
#include "Command.h"

// Handlers implementation */
namespace Handlers {
inline std::string ping(const Command&) {
    return "PONG";
}

inline std::string status(const Command&) {
    return "STATUS:OK";
}

inline std::string uptime(const Command&) {
    return "UPTIME:0";
}

inline std::string echo(const Command& command) {
    return command.getPayload();
}

}
