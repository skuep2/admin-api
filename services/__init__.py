# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 grommunio GmbH


class ServiceUnavailableError(Exception):
    """Service not available.

    Thrown to indicate that the service is not available,
    either because initialization failed or an error occured
    that is typically caused by the external service being unreachable
    (in contrast to errors caused by e.g. faulty data).

    When thrown in a service constructor to indicate that reloading
    at a later time may resolve the issue
    (putting the service in SUSPENDED state)."""
    pass

class ServiceDisabledError(Exception):
    """Service is manually disabled.

    Should be thorwn in service constructor to indicate
    that the service is theoretically available,
    but was disabled manually and can be reactivated later."""
    pass


class _ServiceHubMeta(type):
    def __contains__(cls, value):
        return value in cls._services

    def __iter__(cls):
        return iter(cls._services.values())

    def __getitem__(cls, item):
        return cls._services[item]


class ServiceHub(metaclass=_ServiceHubMeta):
    _services = {}

    UNINITIALIZED = -1  # State has not been set
    LOADED = 0          # Service is available
    UNAVAILABLE = 1     # Temporarily unavailable, might become available automatically
    SUSPENDED = 2       # Needs to be reloaded in order to work
    ERROR = 3           # Fatal error
    DISABLED = 4        # Ok, but disabled manually

    class ServiceInfo:
        def __init__(self, name, mgrclass, exchandler, maxreloads, maxfailures):
            self.mgrclass = mgrclass
            self.state = ServiceHub.UNINITIALIZED
            self.exc = None
            self._name = name
            self.exchandler = exchandler
            self.manager = None
            self._reloads = 0
            self._maxreloads = maxreloads
            self._failures = 0
            self._maxfailures = maxfailures

        def __str__(self):
            statename = {-1: "UNINITIALIZED", 0: "LOADED", 1: "UNAVAILABLE", 2: "SUSPENDED", 3: "ERROR"}
            return "<Service '{}' state {}>".format(self._name, statename.get(self._state))

        def disable(self):
            self.state = ServiceHub.DISABLED
            self.exc = ServiceDisabledError("Service disabled manually")

        def failed(self, newstate, exception):
            self._failures += 1
            self.exc = exception
            if self._maxfailures is not None  and self._failures > self._maxfailures:
                self.state = ServiceHub.ERROR
                self._failures = self._maxfailures
                return False
            self.state = newstate
            return True

        def load(self, force_reload=False):
            if self._state not in (ServiceHub.UNINITIALIZED, ServiceHub.SUSPENDED) and not force_reload:
                    return
            self._reloads += 1
            try:
                self.manager = self.mgrclass()
                self._state = ServiceHub.LOADED
                self._reloads = 0
                return
            except ServiceUnavailableError as err:
                self.exc = err
                self._state = ServiceHub.SUSPENDED if self._reloads <= self._maxreloads else ServiceHub.ERROR
                self._reloads = min(self._reloads, self._maxreloads)
            except ServiceDisabledError as err:
                self.exc = err
                self._state = ServiceHub.DISABLED
            except Exception as err:
                self.exc = err
                self._state = ServiceHub.ERROR
            self.manager = None

        @property
        def available(self):
            return self.state not in (ServiceHub.SUSPENDED, ServiceHub.ERROR, ServiceHub.DISABLED)

        @property
        def failures(self):
            return self._failures

        @property
        def maxfailures(self):
            return self._maxfailures

        @property
        def maxreloads(self):
            return self._maxreloads

        @property
        def name(self):
            return self._name

        @property
        def reloads(self):
            return self._reloads

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            self._state = value if ServiceHub.UNINITIALIZED <= value <= ServiceHub.DISABLED else ServiceHub.ERROR

    @classmethod
    def register(cls, name, exchandler=lambda *args, **kwargs: None, maxreloads=0, maxfailures=None):
        def inner(mgrclass):
            cls._services[name] = cls.ServiceInfo(name, mgrclass, exchandler, maxreloads, maxfailures)
            return mgrclass
        return inner

    @classmethod
    def get(cls, name):
        if name not in cls._services:
            raise ServiceUnavailableError("Service '{}' does not exist.".format(name))
        service = cls._services[name]
        service.load()
        return service

    @classmethod
    def load(cls, *services, force_reload=False):
        if len(services):
            for service in services:
                if service in cls._services:
                    cls._services[service].load(force_reload)
        else:
            for service in cls._services.values():
                service.load()


class Service:
    SUPPRESS_NONE = 0   # All exceptions are passed to the calling function
    SUPPRESS_INOP = 1   # Suppress exceptions indicating service unavailability
    SUPPRESS_ALL = 2    # Suppress all exceptions

    class Stub:
        def __init__(self, name):
            self.name = name

        def __getattr__(self, name):
            raise ServiceUnavailableError("Service '{}' is currently not available".format(self.name))

    def __init__(self, name, suppress=0):
        try:
            self.__suppress = suppress
            self.__service = ServiceHub.get(name)
            self.plugin = self.__service.mgrclass
            self.__mgr = self.__service.manager if self.__service.available else self.Stub(name)
        except Exception:
            if suppress == self.SUPPRESS_ALL:
                self.__service = None
                self.__mgr = self.Stub(name)
            else:
                raise

    def __enter__(self):
        return self.__mgr

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None or isinstance(exc_value, ServiceUnavailableError):
            return self.__suppress != 0
        excresult = self.__service.exchandler(self.__service, exc_value)
        if isinstance(excresult, tuple):
            newstate, msg = excresult
        else:
            newstate, msg = excresult, "Service '{}' is currently not available".format(self.__service.name)
        if newstate is not None:
            self.__service.failed(newstate, exc_value)
            if self.__suppress:
                return True
            raise ServiceUnavailableError(msg)
        if self.__suppress == Service.SUPPRESS_ALL:
            return True

    @staticmethod
    def available(name):
        return name in ServiceHub and ServiceHub[name].available

from . import chat, exmdb, ldap, redis, systemd
