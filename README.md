---------------------------LOGGING IN DJANGO------------------------------

Python Logging Configuration components are Loggers, Handlers, Filters, Formatters.

1. LOGGERS -> Loggers provide initial entry points to group log messages. A logger is configure to have a log level. This log level describes the severity of the messages that the logger will handle.

Python defines the following log levels:
DEBUG -> Low level system information for debugging purposes
INFO -> General system information
WARNING -> Information describing a minor problem that has occurred.
ERROR -> Information describing a major problem that has occurred.
CRITICAL -> Information describing a critical problem that has occurred.

2. HANDLERS -> The handler is the engine that determines what happens to each message in a logger. Handler are responsible for a particular logging behavior, such as writing a message to the screen, to a file, or to a network socket.

A logger can have multiple handlers, and each handler can have a different log level. In this way, it is possible to provide different forms of notification depending on the importance of a message.

3. FILTERS -> A filter is used to provide additional control over which log records are passed from logger to handler.

Filter log messages based on various log levels such as log levels not all the messages need to store or transmit.
Filters can be applied to both loggers and handlers.

4. FORMATTERS -> Ultimately, a log record needs to be rendered as text. Formatters describe the exact format of that text. A formatter usually consists of a Python formatting string containing LogRecord attributes; however, you can also write custom formatters to implement specific formatting behavior.

----------------------------------Custom User model in Django----------------------------------

There are 2 way to create Custom User model in Django.

1. Abstract User
2. Abstract Base User(Here we use this)
