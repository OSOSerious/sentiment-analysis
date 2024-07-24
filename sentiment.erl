-module(sentiment).
-export([start/0, stop/0, classify/1]).

-include_lib("erlport/include/erlport.hrl").

start() ->
    erlport:start(),
    Port = python:start(),
    register(python_port, Port).

stop() ->
    unregister(python_port),
    python:stop().

classify(Text) ->
    Port = whereis(python_port),
    python:call(Port, sentiment, classify, [Text]).
