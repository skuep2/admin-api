#pragma once

#include <string>
#include <vector>
#include <functional>

#include "IOBuffer.h"
#include "requests.h"

namespace exmdbpp
{

class ExmdbClient
{
    class Connection
    {
    public:
        Connection();
        ~Connection();

        void connect(const std::string&, uint16_t);
        void close();
        void send(IOBuffer&);

    private:
        int sock = -1; ///< TCP socket to send and receive data
    };

public:

    ExmdbClient() = default;
    ExmdbClient(const std::string&, uint16_t, const std::string&, bool);

    void connect(const std::string&, uint16_t, const std::string&, bool);

    template<class Request>
    Response<Request> send(const Request&);

    template<class Request, typename... Args>
    Response<Request> send(const Args&...);
private:
    Connection connection; ///< Connection used to send and receive data
    IOBuffer buffer; ///< Buffer managing data to send / received data
};

/**
 * @brief      Send request and parse response
 *
 * @param      request  Request to send
 *
 * @tparam     Request  Type of the request
 *
 * @return     Parsed response object
 */
template<class Request>
inline Response<Request> ExmdbClient::send(const Request& request)
{
    buffer.clear();
    buffer.start();
    buffer << request;
    buffer.finalize();
    connection.send(buffer);
    return Response<Request>(buffer);
}

/**
 * @brief      Send request and parse response
 *
 * Provides the same functionality as send(const Request&) without the creation
 * of an intermediate object, directly serializing the arguments instead.
 *
 * See documentation of the specific Request constructor for a description of
 * possible parameters.
 *
 * @param      args     Values to serialize
 *
 * @tparam     Request  Type of the request
 * @tparam     Args     Constructor arguments
 *
 * @return     Parsed response object
 */
template<class Request, typename... Args>
inline Response<Request> ExmdbClient::send(const Args&... args)
{
    buffer.clear();
    buffer.start();
    Request::serialize(buffer, args...);
    buffer.finalize();
    connection.send(buffer);
    return Response<Request>(buffer);
}

}

