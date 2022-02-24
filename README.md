# python-patterns

## projects made in the course [Python Design Patterns Playbook] at Plural Sight courses platform

# Factory

## Encapsulates object instantiation

## Supports debendecy inversion

## Clients Dont depend on implementation

## Depend on abstraction instead

## Simple Factory Pattern - one factory

### Often just what you need

# Classic Factory Pattern - one or more

## must get an instance of the factory then Make the object

## Most Flexible

## Great when you dont know which concrete classes you'll need

# Abstract Factory

## Encapsulates object instantiation

## Supports dependency inversion

## Clients can write to an abstraction

## Useful when you have families of objects

# Builder

## Separates the "HOW" from the "WHAT"

## Assembly separate from components

## Encapsulates what varies

## Permits different representation

## Client creates director object

## Director uses concrete builder

## builder adds parts to the product

## Client Receives the product from builder

# Prototype

## Decrease Number of Classes

## Compete with Abstract Factory

## Implementations

### Shallow cloning

### Deep cloning

### Prototype Manager

## Use deep Cloning carefully

## Custom cloning

# Singleton

## Controlled access to a single instance

## Reduces the global namespace

## Subclassible for extended user

## Variable number of instances on Base class and metaclass Variants

## More flexible than a static class

## MonoState shares all state

## Can also use a python module

## use sparingly - anti-pattern

# Adapter

## Adapt an interface to the one you need

## Create reusable code

## New unrelated or unforeseen interfaces

## Obj Adapter

### Composition over inheritance

### Delegate to the adaptee

### Works with all adaptee subclasses

## Class Adapter

### Subclassing

### Override adaptee methods

### Committed to one adaptee subclass

# Bridge

## Solve exponential class growth problem using composition

## Extensible by adding "spans"

# Composite

## Single interface to tree structure

## uniform access to subtrees and leaf nodes

## No need to do run time type checking

## Easy to add new kinds of components

## Follows Open/Closed principle

## Violates the single responsability principle

## Use when your data naturally fits a tree-like structure

## children can maintain parent references

## Possible to share components

# Decorator Pattern

## More flaxible than static inheritance

## respect KISS principle

## use when you want add new functionality to existing objects

## Better than many subclasses

## Better than many properties

## Consider look for Factory, Builder or Prototype

# Façade

## Reduces complexity

## Unified interface to a set of interfaces making easier to use

## Shields Clients from subsystem details

## Reduces the objects to handle

# Flyweight

## Centralize state for many objects

## Reduce required object instances

## Single instance are no longer independent

## All instances controlled the same

# Proxy

## Keeps a reference to the subject and expose an identical interface

## Control access to the real object

## Implementations:

### Protection Proxy to controls access

### Virtual Proxy to lazy instantiation or cache results

#### @functools.lru_cache -- cache decorator

### Remote proxy to hide communication details

### Smart proxy can add housekeeping

#### Locking

# Strategy

## Also know as the Policy Pattern

## No SOLID violations

## Can be use function or lambda instead class implementation

## Encapsulate algorithms

## resolve sequences of conditional(if, elif) problem

# Command

## Also known as Action Pattern and Transaction Pattern

## Encapsulate a request as an object

## Queues and log operations

## Great way to encapsulate behavior

## Separate command logic from the client

## Usefull on Command line programs and to build menus

## Easy to add additional capabilities like:

### Validation

### Undo
