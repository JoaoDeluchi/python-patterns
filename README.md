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
