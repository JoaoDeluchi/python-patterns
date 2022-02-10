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
