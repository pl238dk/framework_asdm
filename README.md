# Cisco ASA ASDM Connection Proof of Concept

This is a framework that connects to the ASDM of a Cisco ASA firewall.

## Authentication

A hard-coded username is required and `getpass()` will prompt for a password, then appropriate HTTP headers will be generated for authentication.

## Getting Started

A variable named `command` is provided to pass a command into the ASDM for execution on the underlying firewall.

This is a proof of concept that ASDM can execute commands against a device in order to retrieve data.

To run interactively :

```
> python3 -i asdm.py
```